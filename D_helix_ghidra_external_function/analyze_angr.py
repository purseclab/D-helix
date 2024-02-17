import os
import sys
import math
import time
from time import sleep
import numpy as np
import re

'''
angr_log = "/tmp/angr.txt"
angr_ir_first = "/tmp/angr_ir_first.txt"
angr_ir_second = "/tmp/angr_ir_second.txt"
angr_ir_third = "/tmp/angr_ir_third.txt"
angr_ir_third_flip = "/tmp/angr_ir_third_flip.txt"
'''
angr_z3 = "/tmp/angr_z3.txt"

block_start_dic = {}    #given start address, return block_#
block_end_dic = {}    #given end address, return block_#
block_start_to_end_dic = {}   #given start address, return end address
block_end_to_start_dic = {}   #given end address, return start address
block_id_start_dic = {}
block_id_end_dic = {}

#because we cfgfast is the result from static analysis, it is possible that some block will never be reached
block_start_dic_cfg = {}
block_end_dic_cfg = {}    
block_start_to_end_dic_cfg = {}
block_end_to_start_dic_cfg = {}
block_id_start_dic_cfg = {}
block_id_end_dic_cfg = {}

state_state_id_dic = {}
state_id_state_dic = {}
overlapping_block_start_end = {} #given start id of overlapping block, output the id of ending block, for example: Block4 [a->b] Block5[b->c] is considered as one block Block45[a->c] in lifter, then we have  overlapping_block_start_end[5] = 4
bb_count_cfg = 0

cbranch_count = 0

Father_block_dic = {} #given a block tracing info B_aaa_bbb_ccc_ddd, find its father block tracing (B_aaa_bbb_ccc) generates it
#CB_father_block_dic = {}#given a block tracing info B_aaa_bbb_ccc_ddd, find the last cbranch block tracing (B_aaa_bbb_ ,if there is a branch) generates it
CB_block = ['0']
def reset_global (angr_log,angr_ir_first,angr_ir_second,angr_ir_third,angr_ir_third_flip):
    global block_start_dic 
    global block_end_dic 
    global block_start_to_end_dic 
    global block_end_to_start_dic 
    global block_id_start_dic 
    global block_id_end_dic 
    global block_start_dic_cfg
    global block_end_dic_cfg    
    global block_start_to_end_dic_cfg
    global block_end_to_start_dic_cfg
    global block_id_start_dic_cfg
    global block_id_end_dic_cfg 
    global bb_count_cfg 
    global cbranch_count
    global CB_block
    global Father_block_dic
    global state_state_id_dic
    global overlapping_block_start_end
    global state_id_state_dic

    block_start_dic = {}    #given start address, return block_#
    block_end_dic = {}    #given end address, return block_#
    block_start_to_end_dic = {}   #given start address, return end address
    block_end_to_start_dic = {}   #given end address, return start address
    block_id_start_dic = {}
    block_id_end_dic = {}
    block_start_dic_cfg = {}
    block_end_dic_cfg = {}    
    block_start_to_end_dic_cfg = {}
    block_end_to_start_dic_cfg = {}
    block_id_start_dic_cfg = {}
    block_id_end_dic_cfg = {}

    Father_block_dic = {}
    state_state_id_dic = {}
    overlapping_block_start_end = {}
    state_id_state_dic = {}
    CB_block = ['0']
    bb_count_cfg = 0
    cbranch_count = 0

def build_basic_block (angr_log,angr_ir_first,angr_ir_second,angr_ir_third,angr_ir_third_flip):
    fin = open(angr_log,'r')
    linelist = fin.readlines()
    fin.close()

    fout = open(angr_ir_first, 'w')
    
    global bb_count_cfg
    first_block_address = 0xe0003888888 #set default as 0xe00038
    for i in range(len(linelist)):
        if "successors transfer:[" in linelist[i]:
            first_block_address =  int(re.search('successors transfer:\[ (.+?) -> (.+?) \]',linelist[i]).group(1),16)
            #this is trying to fix the bug that block0 will be used later in the block transfer!
            linelist[i] = linelist[i].replace(str(hex(first_block_address)),str(hex(first_block_address << 20 | 0x88888)))
            first_block_address = first_block_address << 20 | 0x88888
            break
    #fout.write("block_0:[first_block_address->first_block_address]\n")
    #print("in build_basic_block")
    #print(hex(first_block_address))
    block_start_dic[hex(first_block_address)]='block_0'
    block_end_dic[hex(first_block_address)]='block_0'
    block_start_to_end_dic[hex(first_block_address)] = hex(first_block_address)
    block_end_to_start_dic[hex(first_block_address)] = hex(first_block_address)
    block_id_start_dic['block_0'] = hex(first_block_address)
    block_id_end_dic['block_0'] = hex(first_block_address)
    state_state_id_dic['Unknown'] = 'block_0'
    state_id_state_dic['block_0'] = 'Unknown'
    
    for i in range(len(linelist)) : 
        if 'BasicBlock_cfg' in linelist[i]:
            block_start = int(re.search('BasicBlock_cfg:\[(.+?) -> (.+?)\]',linelist[i]).group(1),16)
            block_end = int(re.search('BasicBlock_cfg:\[(.+?) -> (.+?)\]',linelist[i]).group(2),16)
            bb_count_cfg = bb_count_cfg + 1

            block_start_dic_cfg[hex(block_start)] = 'block_' + str(bb_count_cfg)
            block_end_dic_cfg[hex(block_end)] = 'block_' + str(bb_count_cfg)    
            block_start_to_end_dic_cfg[hex(block_start)] = hex(block_end)
            block_end_to_start_dic_cfg[hex(block_end)] = hex(block_start)
            block_id_start_dic_cfg['block_' + str(bb_count_cfg)] = hex(block_start)
            block_id_end_dic_cfg['block_' + str(bb_count_cfg)] = hex(block_end)

    '''
    for i, (k, v) in enumerate(block_start_to_end_dic_cfg.items()):
        print(block_start_dic_cfg[k]+":["+k +"->"+v+"]\n")        
    '''        

    for i in range(len(linelist)) : 
        if 'block range' in linelist[i]:
            block_start = int(re.search('block range:\[ (.+?) -> (.+?) \]',linelist[i]).group(1),16)
            block_end = int(re.search('block range:\[(.+?) -> (.+?)\]',linelist[i]).group(2),16)
            try:
                block_non_overlap_end = int(block_start_to_end_dic_cfg[hex(block_start)],16)
            except:
                #this exception is handling the basic block that is not inclueded by angr cfg, but appears during the symbolic execution running
                bb_count_cfg = bb_count_cfg + 1
                block_start_dic_cfg[hex(block_start)] = 'block_' + str(bb_count_cfg)
                block_end_dic_cfg[hex(block_end)] = 'block_' + str(bb_count_cfg)
                block_start_to_end_dic_cfg[hex(block_start)] = hex(block_end)
                block_end_to_start_dic_cfg[hex(block_end)] = hex(block_start)
                block_id_start_dic_cfg['block_' + str(bb_count_cfg)] = hex(block_start)
                block_id_end_dic_cfg['block_' + str(bb_count_cfg)] = hex(block_end)
                bb_from_cfg_start = block_start_dic_cfg[hex(block_start)]
                block_non_overlap_end = block_end

            bb_from_cfg_start = block_start_dic_cfg[hex(block_start)]
            bb_from_cfg_nonoverlap_end =  block_end_dic_cfg[hex(block_non_overlap_end)]
            


            #because we cfgfast is the result from static analysis, it is possible that some block will never be reached
            block_start_dic[hex(block_start)] = bb_from_cfg_start
            block_end_dic[hex(block_non_overlap_end)] = bb_from_cfg_nonoverlap_end
            block_start_to_end_dic[hex(block_start)] = hex(block_non_overlap_end)
            block_end_to_start_dic[hex(block_non_overlap_end)] = hex(block_start)
            block_id_start_dic[bb_from_cfg_start] = hex(block_start)
            block_id_end_dic[bb_from_cfg_nonoverlap_end] = hex(block_non_overlap_end)

            if block_end != block_non_overlap_end:
                try: 
                    block_start_for_end = block_end_to_start_dic_cfg[hex(block_end)]
                except:
                    block_start_for_end = block_end_to_start_dic_cfg[hex(block_non_overlap_end)]
                bb_from_cfg_start_for_end = block_start_dic_cfg[block_start_for_end]
                try:
                    bb_from_cfg_end = block_end_dic_cfg[hex(block_end)]
                except:
                    bb_from_cfg_end = block_end_dic_cfg[hex(block_non_overlap_end)]
                '''
                block_start_for_end = block_end_to_start_dic_cfg[hex(block_end)]
                bb_from_cfg_start_for_end = block_start_dic_cfg[block_start_for_end]
                bb_from_cfg_end = block_end_dic_cfg[hex(block_end)]
                
                print(bb_from_cfg_end)
                print(bb_from_cfg_start_for_end)
                print(hex(block_end))
                print(hex(block_non_overlap_end))
                print("========")
                '''
                block_start_dic[block_start_for_end] = bb_from_cfg_start_for_end
                block_end_dic[hex(block_end)] = bb_from_cfg_end
                block_start_to_end_dic[block_start_for_end] = hex(block_end)
                block_end_to_start_dic[hex(block_end)] = block_start_for_end
                block_id_start_dic[bb_from_cfg_start_for_end] = block_start_for_end
                block_id_end_dic[bb_from_cfg_end] = hex(block_end)

    '''
    for i, (k, v) in enumerate(block_end_dic.items()):
        print(block_end_dic[k]+":["+k +"->"+v+"]\n")
    '''
            
    for i in range(len(linelist)) : 
        if 'block range' in linelist[i]:
            block_start = int(re.search('block range:\[ (.+?) -> (.+?) \]',linelist[i]).group(1),16)
            block_end = int(re.search('block range:\[(.+?) -> (.+?)\]',linelist[i]).group(2),16)
            block_id_start = int(re.search('block_(.+?)\n',block_start_dic[hex(block_start)]+"\n").group(1),10)
            block_id_end = int(re.search('block_(.+?)\n',block_end_dic[hex(block_end)]+"\n").group(1),10)
            
            if 'current state is:' in linelist[i+1] :
                state_num = re.search('current state is:\[ \<SimState @ (.+?)\> \]',linelist[i+1]).group(1)
                state_state_id_dic[state_num] = 'block_' + str(block_id_start)
                state_id_state_dic['block_' + str(block_id_start)] = state_num

            #now we know the range of overlapping
            if block_id_start != block_id_end:
                '''
                print(hex(block_start))
                print(hex(block_end))
                print(block_end_dic[hex(block_end)])
                print(linelist[i])        
                print(block_id_start)
                print(block_id_end)
                '''
                overlapping_block_start_end[block_id_start]=block_id_end
                #raise Exception('Block overlapping!')
            
    #record BB for debug    
    #print(overlapping_block_start_end)
    for i, (k, v) in enumerate(block_start_to_end_dic.items()):
        fout.write(block_start_dic[k]+":["+k +"->"+v+"]\n")
            
    fout.close()
    
    #print(block_start_dic)
    #print(block_end_dic)

def generate_ir_first_version (angr_log,angr_ir_first,angr_ir_second,angr_ir_third,angr_ir_third_flip):
    fout = open(angr_ir_first, 'a')
    fin = open(angr_log,'r')
    linelist = fin.readlines()
    fin.close()
    
    
    #this is trying to fix the bug that block0 will be used later in the block transfer!
    for i in range(len(linelist)):
        if "successors transfer:[" in linelist[i]:
            first_block_address =  int(re.search('successors transfer:\[ (.+?) -> (.+?) \]',linelist[i]).group(1),16)
            #print(str(first_block_addres))
            linelist[i] = linelist[i].replace(str(hex(first_block_address)),str(hex(first_block_address << 20 | 0x88888)))
            #print(linelist[i])
            break

    
    global bb_count_cfg
    
    global cbranch_count
    i = 0
    while i != len(linelist) : 
        if 'successors transfer' in linelist[i]:
            transfer_start = int(re.search('successors transfer:\[ (.+?) -> (.+?) \]',linelist[i]).group(1),16)
            transfer_end = int(re.search('successors transfer:\[ (.+?) -> (.+?) \]',linelist[i]).group(2),16)
            
            transfer_start_str = block_start_dic[hex(transfer_start)]
            

            try:
                transfer_end_str = block_start_dic[hex(transfer_end)]
            except: 
                #print(i)
                #print(linelist[i])
                #we may face situation like:
                #    successors transfer:[ 0x4000f6 -> 0xb01038 ]
                #    successors transfer:[ 0xb01038 -> 0xb01038 ]
                #    successors transfer:[ 0xb01038 -> 0x4001fe ]
                #where b01038 is not in function block, but it is fine, we need to track until the end.
                j = 2
                #print(i)    
                #print(linelist[i+j])
                #print(linelist[i+j-2])
                #make sure next is successors transfer and next is linked
                while i+j+2 < len(linelist) and 'successors transfer' in linelist[i+j] and int(re.search('successors transfer:\[ (.+?) -> (.+?) \]',linelist[i+j]).group(1),16) == int(re.search('successors transfer:\[ (.+?) -> (.+?) \]',linelist[i+j-2]).group(2),16) :
                    j += 2
                
                if i+j+2 >= len(linelist):
                    #we can skip few lines of block transfer at very last
                    i = len(linelist)
                    transfer_end_str = 'block_0'
                else:
                    transfer_end = int(re.search('successors transfer:\[ (.+?) -> (.+?) \]',linelist[i+j-2]).group(2),16)
                    transfer_end_str = block_start_dic[hex(transfer_end)]
                    i = i+j-2
            #print(overlapping_block_start_end)
            if int(re.search('block_(.+?)\n',transfer_start_str+'\n').group(1),10) in overlapping_block_start_end.keys():
                #print(transfer_start_str)
                transfer_start_str = transfer_start_str +'_' +str(overlapping_block_start_end[int(re.search('block_(.+?)\n',transfer_start_str+'\n').group(1),10)])

            if int(re.search('block_(.+?)\n',transfer_end_str+'\n').group(1),10) in overlapping_block_start_end.keys():
                #print(transfer_end_str)
                transfer_end_str = transfer_end_str +'_' +str(overlapping_block_start_end[int(re.search('block_(.+?)\n',transfer_end_str+'\n').group(1),10)])

            fout.write('Trans:['+transfer_start_str+' -> '+transfer_end_str+']\n')

            if i == len(linelist):
                break


        if 'In cbranch' in linelist[i]:
            cb_block_addr = int(re.search('block range:\[ (.+?) -> (.+?) \]',linelist[i-2]).group(1),16)
            #cb_block_1 = block_start_to_end_dic[hex(cb_block_addr)]
            cb_block_1 = re.search('block range:\[ (.+?) -> (.+?) \]',linelist[i-2]).group(2)
            
            
            
                        
            cb_block_2 = int(re.search('address added is:\[ (.+?)\]',linelist[i+1]).group(1),16)

            #here we deal with the cbranch that does goto one of its branch, because the evaluation of the condition for this cbranch is either false or true
            try:
                cb_block_2_str = block_start_dic[hex(cb_block_2)]
    
                if int(re.search('block_(.+?)\n',cb_block_2_str+'\n').group(1),10) in overlapping_block_start_end.keys():
                    cb_block_2_str = cb_block_2_str +'_' +str(overlapping_block_start_end[int(re.search('block_(.+?)\n',cb_block_2_str+'\n').group(1),10)])

            except:
                cb_block_2_str = 'unknown'
            try:
                cb_block_1_str = block_start_dic[cb_block_1]
                
                if int(re.search('block_(.+?)\n',cb_block_1_str+'\n').group(1),10) in overlapping_block_start_end.keys():
                    cb_block_1_str = cb_block_1_str +'_' +str(overlapping_block_start_end[int(re.search('block_(.+?)\n',cb_block_1_str+'\n').group(1),10)])
            except:
                cb_block_1_str = 'unknown'
            
            #if the conditon of cbranch is True or False, that is same as saying this cbranch is a branch.
            #if '(_ bv1 8)' in linelist[i+4] : #True statment, z3 will dump nothing instead of assert true.
            '''
            if '(check-sat)' in linelist[i+5] : 
                cb_block_2_str = 'unknown'
            #if '(_ bv0 8)' in linelist[i+4] : # False
            if '(assert' in linelist[i+5] and 'false)' in linelist[i+6]:
                cb_block_1_str = 'unknown'
            '''
            if '(_ bv1 1)' in linelist[i+4] : 
                if "flip" in linelist[i]:
                    cb_block_2_str = 'unknown'
                else:
                    cb_block_1_str = 'unknown'
            #if '(_ bv0 8)' in linelist[i+4] : # False
            if '(_ bv0 1)' in linelist[i+4] : 
                if "flip" in linelist[i]:
                    cb_block_1_str = 'unknown'
                else:
                    cb_block_2_str = 'unknown'

            #add condition for cbranch with specific condition results
            if cb_block_2_str == 'unknown' or cb_block_1_str =='unknown' :
                if cb_block_2_str == 'unknown' and cb_block_1_str =='unknown':
                    fout.close()
                    raise Exception('CBranch both unreachable!')
                if cb_block_2_str == 'unknown':
                    cb_block_src_str = block_start_dic[hex(cb_block_addr)]
                    if int(re.search('block_(.+?)\n',cb_block_src_str+'\n').group(1),10) in overlapping_block_start_end.keys():
                        cb_block_src_str = cb_block_src_str +'_' +str(overlapping_block_start_end[int(re.search('block_(.+?)\n',cb_block_src_str+'\n').group(1),10)])
                    fout.write("Branch:["+cb_block_src_str+"->"+cb_block_1_str+"]\n")
                else:
                    cb_block_src_str = block_start_dic[hex(cb_block_addr)]
                    if int(re.search('block_(.+?)\n',cb_block_src_str+'\n').group(1),10) in overlapping_block_start_end.keys():
                        cb_block_src_str = cb_block_src_str +'_' +str(overlapping_block_start_end[int(re.search('block_(.+?)\n',cb_block_src_str+'\n').group(1),10)])
                    fout.write("Branch:["+cb_block_src_str+"->"+cb_block_2_str+"]\n")
            else:
                cbranch_count += 1
                cb_block_src_str = block_start_dic[hex(cb_block_addr)]
                if int(re.search('block_(.+?)\n',cb_block_src_str+'\n').group(1),10) in overlapping_block_start_end.keys():
                    cb_block_src_str = cb_block_src_str +'_' +str(overlapping_block_start_end[int(re.search('block_(.+?)\n',cb_block_src_str+'\n').group(1),10)])
                if "flip" in linelist[i]:
                    fout.write("CB_"+str(cbranch_count)+":["+cb_block_src_str +","+ cb_block_1_str +","+ cb_block_2_str +"]\n")
                else:
                    fout.write("CB_"+str(cbranch_count)+":["+cb_block_src_str +","+ cb_block_2_str +","+ cb_block_1_str +"]\n")
                
        if 'In branchind' in linelist[i]:
            fout.write("BranchInd\n")
            fout.close()
            raise Exception('BranchInd is currently not supported for analysing')
        
        if 'In callind' in linelist[i]:
            fout.write("CallInd\n")
            fout.close()
            raise Exception('CallInd is currently not supported for analysing')

        if 'In branch' in linelist[i] and 'In branchind' not in linelist[i]:
            b_block_addr = int(re.search('current address is:\[ (.+?) \]',linelist[i+1]).group(1),16)
            b_block_des_addr = int(re.search('address added is:\[ (.+?) \]',linelist[i+2]).group(1),16)
            try:
                b_block_des_str = block_start_dic[hex(b_block_des_addr)]
                #print("111"+b_block_des_str)
                if int(re.search('block_(.+?)\n',b_block_des_str+'\n').group(1),10) in overlapping_block_start_end.keys():
                    #print(b_block_des_str)
                    b_block_des_str = b_block_des_str +'_' +str(overlapping_block_start_end[int(re.search('block_(.+?)\n',b_block_des_str+'\n').group(1),10)])
            except:
                fout.close()
                raise Exception('Branch goes unreachable!')

            b_block_src_str = block_start_dic[hex(b_block_addr)]
            if int(re.search('block_(.+?)\n',b_block_src_str+'\n').group(1),10) in overlapping_block_start_end.keys():
                    b_block_src_str = b_block_src_str +'_' +str(overlapping_block_start_end[int(re.search('block_(.+?)\n',b_block_src_str+'\n').group(1),10)])
            fout.write("Branch:["+b_block_src_str+"->"+b_block_des_str+"]\n")
        
        if 'In call' in linelist[i] and 'In callind' not in linelist[i]:
            b_block_addr = int(re.search('current address is:\[ (.+?) \]',linelist[i+1]).group(1),16)
            b_block_des_addr = int(re.search('address added is:\[ (.+?) \]',linelist[i+2]).group(1),16)
            
            '''
            try:
                b_block_des_str = block_start_dic[hex(b_block_des_addr)]
            except:
                #since in our system internal/external call will return 0 directly, check Callless in angr.engines.pcode
                b_block_des_str = block_start_dic[block_start_to_end_dic[hex(b_block_addr)]]
            '''
            #since in our system internal/external call will return 0 directly, check Callless in angr.engines.pcode
            b_block_des_str = block_start_dic[block_start_to_end_dic[hex(b_block_addr)]]

            if int(re.search('block_(.+?)\n',b_block_des_str+'\n').group(1),10) in overlapping_block_start_end.keys():
                #print(b_block_des_str)
                b_block_des_str = b_block_des_str +'_' +str(overlapping_block_start_end[int(re.search('block_(.+?)\n',b_block_des_str+'\n').group(1),10)])    
            
            #treat call as branch
            call_block_src_str = block_start_dic[hex(b_block_addr)]
            if int(re.search('block_(.+?)\n',call_block_src_str+'\n').group(1),10) in overlapping_block_start_end.keys():
                call_block_src_str = call_block_src_str +'_' +str(overlapping_block_start_end[int(re.search('block_(.+?)\n',call_block_src_str+'\n').group(1),10)])
            fout.write("Branch:["+call_block_src_str+"->"+b_block_des_str+"]\n")
        
        if 'In ret' in linelist[i] or 'In fakeret' in linelist[i]:
            fout.write(linelist[i])
            

        if '----dump z3 start----' in linelist[i]:
            fout.write("----dump z3 start----\n")
            for j in range(len(linelist)) :
                if "----dump z3 end----" in linelist[i+1+j]:
                    break
                else:
                    fout.write(linelist[i+1+j])
            fout.write("----dump z3 end----\n")

        if 'parent state is' in linelist[i]:
            father_state_num_str = re.search('parent state is:\[ \<StateHistory @ (.+?)\> \]',linelist[i]).group(1)
            father_state_id = state_state_id_dic[father_state_num_str]
            father_state_id_num = int(re.search('block_(.+?)',father_state_id).group(1),10)
            if father_state_id_num in overlapping_block_start_end.keys():
                father_state_id = 'block_'+ str(father_state_id_num)+ '_' + str(overlapping_block_start_end[father_state_id_num])

            fout.write('Father state:['+father_state_id+']\n')
        i += 1
    fout.close()
 

def generate_father_block_second_version (angr_log,angr_ir_first,angr_ir_second,angr_ir_third,angr_ir_third_flip):
    fout = open(angr_ir_second, 'w')
    fin = open(angr_ir_first,'r')
    linelist = fin.readlines()
    fin.close()
    Process_block_queue = ['block_0_last_0_end']
    First_reachment = True 
    for i in range(len(linelist)-2) :
        if 'Trans' in linelist[i]:
            #print(Process_block_queue) 
            Process_block = Process_block_queue.pop(0)
            Previous_block_num = re.search('block_(.+?)_last_(.+?)_end',Process_block).group(1)
            Should_be_current_block_id = re.search('block_(.+?)_last_(.+?)_end',Process_block).group(2)
            Current_block_id = re.search('Trans:\[block_(.+?) -> block_(.+?)\]',linelist[i]).group(2)
            
            if 'fakeret' in linelist[i+2]:
                if Current_block_id[:len(Should_be_current_block_id)]  == Should_be_current_block_id :
                    pass
                else:
                    Process_block_queue.insert(0,Process_block)
                    Process_block_last = Process_block_queue.pop() #output last element
                    Previous_block_num = re.search('block_(.+?)_last_(.+?)_end',Process_block_last).group(1)
                    Should_be_current_block_id = re.search('block_(.+?)_last_(.+?)_end',Process_block_last).group(2)
                    Current_block_id = re.search('Trans:\[block_(.+?) -> block_(.+?)\]',linelist[i]).group(2)
                    if Current_block_id[:len(Should_be_current_block_id)]  == Should_be_current_block_id :
                        Process_block = Process_block_last
                    else:
                        Process_block_last_second = Process_block_queue.pop()
                        Process_block_queue.append(Process_block_last)
                        Previous_block_num = re.search('block_(.+?)_last_(.+?)_end',Process_block_last_second).group(1)
                        Should_be_current_block_id = re.search('block_(.+?)_last_(.+?)_end',Process_block_last_second).group(2)
                        Current_block_id = re.search('Trans:\[block_(.+?) -> block_(.+?)\]',linelist[i]).group(2)
                        Process_block =Process_block_last_second

            if Current_block_id[:len(Should_be_current_block_id)] != Should_be_current_block_id and Should_be_current_block_id != '0':
                print("error!! current block id is not same as should be")
                print(Process_block_queue)
                print (Current_block_id)
                print(Should_be_current_block_id)
                print(Process_block)
                print(linelist[i])
                fout.close()
                return

            if 'Father state' not in linelist[i+1]:
                fout.close()
                raise Exception('Father state is not the next line of Trans') 
            else:
                Father_state_num = re.search('Father state:\[block_(.+?)\]',linelist[i+1]).group(1)

            if 'Unknown' in Process_block:
                #to handle branchind, here is the what happens and what we try to do:
                #branchind will generate a switch-like statement based on its expr, what we can do is split this switch into several CB, for example:
                # switch (a) needs to be converted to:
                # if (a == 1){ 
                # }else { 
                #       if (a == 2) {
                #       }else {
                #       }
                # } 
                # the number of switch child can only be known until now.
                
                #print(Process_block)
                Branchind_id = re.search('block_(.+?)_last_Unknown_(.+?)_Unknown_end',Process_block).group(2)    #we have the block id of branchind
                #print(Branchind_id)

            
            
            #handle _0_last_0_end issue
            if '_' in Previous_block_num:
                Process_block_num = re.search('block_(.+?)_last_(.+?)_end',Process_block).group(1) +'_'+ re.search('block_(.+?)_last_(.+?)_end',Process_block).group(2)
            else:
                #this case should be just for 0
                Process_block_num = re.search('block_(.+?)_last_(.+?)_end',Process_block).group(1)

            
                        
            
            #this if handle the first block reachment issue
            if Current_block_id == Should_be_current_block_id and First_reachment == False :
                Current_block_num = Process_block_num            
                
            else:
                Current_block_num = Process_block_num+'_'+Current_block_id
                First_reachment = False        
            
            #show here for debug father block tracking
            #fout.write('Previous_block_num is: '+ Previous_block_num +'\n')            
            #fout.write('Track:[block_' +Previous_block_num+' -> block_' + Current_block_num + ']\n')
            
            #we check our own father block finding system is same as what angr has
            #print(Previous_block_num)
            #print(Father_state_num)
            #'''            
            if '_' in Father_state_num:
                print("123")
                print(Father_state_num)
                Father_state_num = re.search('(.+?)_(.+?)\n',Father_state_num+'\n').group(2)
            #'''
            Father_state_num_len = len(Father_state_num)
            Previous_block_last_num = Previous_block_num[-Father_state_num_len:]
            
            
            #'''
            if Father_state_num != Previous_block_last_num :
                print(Father_state_num_len)
                print(overlapping_block_start_end)
                print(i)
                print(linelist[i+1])
                print(Father_state_num)
                print(Previous_block_num)
                print(Previous_block_last_num)
                
                Father_state_num = Father_state_num.replace("_","")
                Previous_block_last_num = Previous_block_last_num.replace("_","")
                if int(Father_state_num,10) not in overlapping_block_start_end.values() and int(Previous_block_last_num,10) not in overlapping_block_start_end.values():
                    fout.close()
                    raise Exception('our own father block finding system is NOT same as angrs !!!') 
                #else:
                    #Previous_block_num = Previous_block_num + "_" + Father_state_num
            #'''    
            Father_block_dic[Current_block_num] = Previous_block_num
            
            
            if 'CB_' in linelist[i+2]:
                fout.write('Current: block_'+Current_block_num+'\n')
                Father_block_num = Father_block_dic[Current_block_num]
                #print(Father_block_num)
                while Father_block_num not in CB_block:
                    Father_block_num = Father_block_dic[Father_block_num]
                fout.write('Father block is:block_'+Father_block_num+'\n')
                CB_block.append(Current_block_num)
                CB_block_id_1 = re.search('CB_(.+?):\[block_(.+?),block_(.+?),block_(.+?)\]',linelist[i+2]).group(3)
                CB_block_id_2 = re.search('CB_(.+?):\[block_(.+?),block_(.+?),block_(.+?)\]',linelist[i+2]).group(4)
                if 'flip' in linelist[i+2]:
                    Process_block_queue.append('block_'+Current_block_num+'_last_'+CB_block_id_2+'_end')
                    Process_block_queue.append('block_'+Current_block_num+'_last_'+CB_block_id_1+'_end')
                else:
                    Process_block_queue.append('block_'+Current_block_num+'_last_'+CB_block_id_1+'_end')
                    Process_block_queue.append('block_'+Current_block_num+'_last_'+CB_block_id_2+'_end')
                
                #we only print condition in cbranch and result from return
                for j in range(len(linelist)) :
                    if "----dump z3 end----" in linelist[i+1+j]:
                        fout.write(linelist[i+1+j])
                        break
                    else:
                        fout.write(linelist[i+1+j])
                
            elif 'BranchInd' in linelist[i+2]:
                Current_block_id = re.search('Trans:\[block_(.+?) -> block_(.+?)\]',linelist[i]).group(2)
                Branch_dest_id = 'Unknown_'+ Current_block_id+ '_Unknown'
                Process_block_queue.append('block_'+Current_block_num+'_last_'+Branch_dest_id+'_end')

            elif 'Branch' in linelist[i+2] and 'BranchInd' not in linelist[i+2]:
                Branch_dest_id = re.search('Branch:\[block_(.+?)->block_(.+?)\]',linelist[i+2]).group(2)
                Process_block_queue.append('block_'+Current_block_num+'_last_'+Branch_dest_id+'_end')

            elif 'fakeret' in linelist[i+2]:
                fout.write('Current: block_'+Current_block_num+'\n')
                #Process_block_queue.append('block_'+Current_block_num+'_end')
                #Process_block_queue.append('block_'+Previous_block_num+'_last_'+Current_block_id+'_end')                
                Father_block_num = Father_block_dic[Current_block_num]
                while Father_block_num not in CB_block:
                    Father_block_num = Father_block_dic[Father_block_num]
                fout.write('Father block is:block_'+Father_block_num+'\n')
                #we only print condition in cbranch and result from return
                for j in range(len(linelist)) :
                    if "----dump z3 end----" in linelist[i+1+j]:
                        fout.write(linelist[i+1+j])
                        break
                    else:
                        fout.write(linelist[i+1+j])
            elif 'ret' in linelist[i+2] and 'fakeret' not in linelist[i+2]:
                fout.write('Current: block_'+Current_block_num+'\n')
                #Process_block_queue.append('block_'+Current_block_num+'_end')
                #Process_block_queue.append('block_'+Previous_block_num+'_last_'+Current_block_id+'_end')                
                Father_block_num = Father_block_dic[Current_block_num]
                while Father_block_num not in CB_block:
                    Father_block_num = Father_block_dic[Father_block_num]
                fout.write('Father block is:block_'+Father_block_num+'\n')
                #we only print condition in cbranch and result from return
                for j in range(len(linelist)) :
                    if "----dump z3 end----" in linelist[i+1+j]:
                        fout.write(linelist[i+1+j])
                        break
                    else:
                        fout.write(linelist[i+1+j])

            else: #this means block runs to end and keep going
                #we may have overlapping block there, check ir_first log generated from /tmp/angr_masscan_blackrock2_benchmark, its block_9_10 has issues.
                #check ir_second log generated from du_new_exclude_segment, its block_11_12 has issues.
                last_block_id = Current_block_id.split("_")[-1]
                Block_dest_addr = block_id_end_dic['block_'+last_block_id]
                '''
                if Current_block_id != Should_be_current_block_id : 
                    #we may have overlapping block there, check ir_first log generated from /tmp/angr_masscan_blackrock2_benchmark, its block_9_10 has issues.
                    Block_dest_addr = block_id_end_dic['block_'+Current_block_id.replace(Should_be_current_block_id+"_","")]
                else:
                    Block_dest_addr = block_id_end_dic['block_'+Current_block_id]
                '''
                Block_dest = block_start_dic[Block_dest_addr] + '_]' #add _] at the end of "block_xxx", since search directly on "block_xxx" will not return the correct xxx
                Block_dest_id = re.search('block_(.+?)_]',Block_dest).group(1)
                Process_block_queue.append('block_'+Current_block_num+'_last_'+Block_dest_id+'_end')
        else:
            #donothing, since the necessary info has been loaded.
            a=0
    fout.close()

def generate_children_block_second_version (angr_log,angr_ir_first,angr_ir_second,angr_ir_third,angr_ir_third_flip):
    fin = open(angr_ir_second,'r')
    linelist = fin.readlines()
    fin.close()
    #print("12332131321312")
    fout = open(angr_ir_third, 'w')
    i = 0
    while i < len(linelist)-3 : 
        print("generate_children_block_second_version:"+str(i))
        if 'CB_' in linelist[i+3]:
            Current_Block = re.search('Current: (.+?)\n',linelist[i]).group(1)
            #we want to make sure the order of children is correct
            #print(linelist[i+3])
            Correct_Children_0_last = re.search('CB_(.+?):\[block_(.+?),block_(.+?),block_(.+?)\]\n',linelist[i+3]).group(3)
            Correct_Children_1_last = re.search('CB_(.+?):\[block_(.+?),block_(.+?),block_(.+?)\]\n',linelist[i+3]).group(4)
            #print(Current_Block)
            Children_Block = []
            Children_Block_index = []
            for j in range(len(linelist)):
                #print(linelist[j])
                if 'Father block is:'+Current_Block+'\n' in linelist[j]:
                    Children_Block.append(re.search('Current: (.+?)\n',linelist[j-1]).group(1))
                    Children_Block_index.append(j)
                    
            if len(Children_Block) < 2:
                #print (linelist[i+2])
                print ("weird, Cbranch should not have only one child or no child!!!")
                #raise Exception('How can CBranch does not have two children!')
                
                #find
                Cbranch_start = i
                Cbranch_end = i
                while Cbranch_end < len(linelist) :
                    if 'dump z3 end' in linelist[Cbranch_end]:
                        break
                    else:
                        Cbranch_end += 1

                '''
                cbranch has no child, we just remove this cbranch
                cbranch has only one child, that means this cbranch is a branch only,few step we need to do here:
                1. replace the father block in its child to this cbranch's father block
                2. remove this cbranch 
                '''
                if len(Children_Block) == 0:
                    print(Cbranch_start)
                    print(Cbranch_end)
                    print("no child")
                    print(linelist[i+1])
                    if i < Cbranch_end + 1:
                        i = Cbranch_end + 1
                
                
                else:        
                    print("one child")    
                    print(linelist[i+1])
                    print(i)
                    print(Cbranch_end + 1)
                    print(angr_ir_second)
                    Father_block_cbranch = re.search('Father block is:(.+?)\n',linelist[i+1]).group(1)
                    linelist[Children_Block_index[0]] = 'Father block is:'+Father_block_cbranch+'\n'
                    if i < Cbranch_end + 1:
                        i = Cbranch_end + 1
                
                
                
            if len(Children_Block) > 2 :
                #print (linelist[i+2])
                #print (Children_Block)
                fout.close()
                raise Exception('How can CBranch has more than two different children!')
            
            print("before foutwrite")
            fout.write(linelist[i])
            print("after foutwrite")
            '''
            print(Correct_Children_0_last)
            print(Correct_Children_1_last)
            print(Current_Block)
            print("Children_Block[0]")
            print(Children_Block[0])
            print("Children_Block[1]")
            print(Children_Block)
            print(Children_Block[1])
            '''
            Current_Children_Block_0_last = ""
            Current_Children_Block_1_last = ""
            if len(Children_Block)== 2: 
                Current_Children_Block_0_last = Children_Block[0].replace(Current_Block+"_","")
                Current_Children_Block_1_last = Children_Block[1].replace(Current_Block+"_","")
            if len(Children_Block)== 1:
                Current_Children_Block_0_last = Children_Block[0].replace(Current_Block+"_","")

            '''
            print(Current_Children_Block_0_last)
            print(Current_Children_Block_1_last)
            print(Current_Children_Block_0_last[:len(Correct_Children_0_last)])
            print(Current_Children_Block_1_last[:len(Correct_Children_1_last)])
            '''
            print("after foutwrite2")
            if Current_Children_Block_0_last[:len(Correct_Children_0_last)] == Correct_Children_0_last and Current_Children_Block_1_last[:len(Correct_Children_1_last)] == Correct_Children_1_last :
                print("after foutwrite if1")
                fout.write('Children Block:['+Children_Block[0]+','+Children_Block[1]+']\n')
            elif Current_Children_Block_0_last[:len(Correct_Children_1_last)] == Correct_Children_1_last and Current_Children_Block_1_last[:len(Correct_Children_0_last)] == Correct_Children_0_last :
                print("after foutwrite if2")
                fout.write('Children Block:['+Children_Block[1]+','+Children_Block[0]+']\n')
            else:
                pass
                '''
                print("before raise children found")
                fout.close()
                raise Exception('children found are not the correct one!')
                '''
            print("in if first")
        else:
            print("in large else")
            fout.write(linelist[i])
        i+=1
    print("Finished run second")
    print(len(linelist))
    fout.write(linelist[len(linelist)-3])
    fout.write(linelist[len(linelist)-2])
    fout.write(linelist[len(linelist)-1])
    fout.close()
    print("Finished run second fout.write")

#we just convert our cfg file to a more "z3 like " readable code


def cfg_to_ir(finput,foutput):
        
    fin = open(finput,'r')
    linelist = fin.readlines()
    fin.close()

    fout = open(foutput,'w')
    i = 0
    while i < len(linelist) -4 :
        print("cfg_to_ir:"+str(i))
        func_start = 'Current:' in linelist[i]
        add_ite = 'CB_' in linelist[i+4]
        if add_ite and func_start:
            #print(linelist[i])
            Current_Block = re.search('Current: (.+?)\n',linelist[i]).group(1)
            Children_Block_1 = re.search('Children Block:\[(.+?),(.+?)\]',linelist[i+1]).group(1)
            Children_Block_2 = re.search('Children Block:\[(.+?),(.+?)\]',linelist[i+1]).group(2)
            
            fout.write("###start\n") 
            fout.write("(let (("+str(Current_Block)+"\n")            
            
            #3. output let constraint_a = things between ---dump z3 start--- and ---dump z3 end---
            fout.write("(let ((constraint_"+str(Current_Block)+"\n")
            dump_start = i
            dump_end = i
            for k in range(i,len(linelist)):    
                if '----dump z3 start----' in linelist[k]:
                    dump_start = k
                if '----dump z3 end----' in linelist[k]:
                    dump_end = k
                    break

            #here since in angr, we have two extra lines, try skip them:
            #; benchmark
            #(set-info :status unknown)
            #(declare-fun reg_18_25_8 () (_ BitVec 8))
            #(assert
            # (let ((?x24 ((_ extract 7 7) reg_18_25_8)))
            #    ...
            #(check-sat)

            for k in range(dump_start+1,dump_end) :
                #print("WWWWW")
                '''
                if k == dump_end -1 and 'ite' in linelist[k] and 'bv1' in linelist[k] and 'bv0' in linelist[k]:
                    fout.write(linelist[k].replace('(_ bv1 1)','true').replace('(_ bv0 1)','false').replace('\n',')\n'))
                '''
                if 'benchmark' not in linelist[k] and '(declare-fun' not in linelist[k] and 'set-info' not in linelist[k] and '(assert' not in  linelist[k] and '(check-sat)' not in linelist[k] :
                    fout.write(linelist[k])
                else:
                    pass
                    
            fout.write("))")
            #2. output ite constraint block_c block_b
            fout.write("(ite (= (_ bv1 1) constraint_"+str(Current_Block) + ") "+str(Children_Block_1)+ " "+str(Children_Block_2) +" )\n")
            fout.write(")))\n")                
            fout.write("###end\n")
        
        add_ret = 'In ret' in linelist[i+3] or 'In fakeret' in linelist[i+3] 
        if add_ret and func_start:
            #print(linelist[i])
            fout.write("###start\n") 
            Current_Block = re.search('Current: (.+?)\n',linelist[i]).group(1)
            
            #print(BB_info)
            #2. output let block_a =
            fout.write("(let (("+str(Current_Block)+"\n")
            #3. output things between ---dump z3 start--- and ---dump z3 end---
            dump_start = i
            dump_end = i
            for k in range(i,len(linelist)):    
                if '----dump z3 start----' in linelist[k]:
                    dump_start = k
                if '----dump z3 end----' in linelist[k]:
                    dump_end = k
                    break
            #just dump pure expression
            for k in range(dump_start+1,dump_end) :
                if ('benchmark' not in linelist[k] and '(declare-fun' not in linelist[k]) :
                    fout.write(linelist[k])
            fout.write("))\n")
            fout.write("###end\n")
        
        i += 1
    fout.close()


#Think about this, since we use bfs-klee to symbolic execute the bitcode, the info being dumped is from root to each leaves.
#However, when we run the z3, we need to define those leaf nodes first. Hence, we need to revert the order of whole ir file.

def ir_reorder(finput):
    block_list = []
    fin = open(finput,'r')
    linelist = fin.readlines()
    fin.close()
    i = 0
    while i < len(linelist) :
        if '###start' in linelist[i]:
            j = i
            while j < len(linelist) :
                if '###end' in linelist[j]:
                    result = []
                    result.append(i)
                    result.append(j)
                    block_list.append(result)
                    i = j
                    break
                else:
                    j += 1
        else:
            i += 1
    #print (block_list)
    fout = open(finput,'w')
    k = len(block_list) -1 
    while k >= 0 :
        for i in range(block_list[k][0],block_list[k][1]+1):
            fout.write(linelist[i])
        k -= 1
    fout.close()


def main():
    '''
    build_basic_block()
    generate_ir_first_version()
    generate_father_block_second_version()
    generate_children_block_second_version()
    '''
    cfg_to_ir(angr_ir_third,angr_ir_third_flip)
    ir_reorder(angr_ir_third_flip)


if __name__ == "__main__":
    main()
