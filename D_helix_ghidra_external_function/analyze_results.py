import os
import sys
import math
import time
from time import sleep
import numpy as np
import re
import convert
import signal
import subprocess
import platform

directname_originalc = "./test_muqi/originalc"
directname_lifterbc = "./test_muqi/lifterbc"
directname_generatedc = "./test_muqi/generatedc"
directname_generatedbc = "./test_muqi/generatedbc"


directname_diff = "./test_muqi/diff"
directname_z3 = "./test_muqi/z3"
directname_log = "./test_muqi/log"


def pkiller():
    from ctypes import cdll
    import ctypes
    # PR_SET_PDEATHSIG, SIG_KILL --> kill child when parent dies
    cdll['libc.so.6'].prctl(1, 9)

#'''
#https://blog.csdn.net/jiandanokok/article/details/103644902
def run_cmd(cmd_string, timeout):
    p = subprocess.Popen(cmd_string, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True, close_fds=True,
                         start_new_session=True,preexec_fn=pkiller)
    try:
        p.communicate(timeout=timeout)
        p.poll()
    except subprocess.TimeoutExpired:
        #p.kill()
        #p.terminate()A
        os.killpg(p.pid, signal.SIGKILL)
    except Exception as e:
        pass
            
def filter_instruction_in_function(filepath,filepath_out,function_name,exclude_function_name):
    fin = open(filepath,'r')
    linelist = fin.readlines()
    fin.close()
    contain_symbol = np.zeros((len(linelist)),dtype=bool)
    for k in range(len(function_name)):
        for i in range(len(linelist)):
            exclude_line = False
            for l in range(len(exclude_function_name)):
                    if exclude_function_name[l] in linelist[i] :
                        exclude_line = True

            if 'Function start: ' in linelist[i] and function_name[k].replace(".","_") in linelist[i] and not exclude_line:
                contain_symbol[i] = True
                index_dump_start = i
                index_dump_end = -1

                for j in range(len(linelist)-i):
                    if 'Function end' in linelist[i+j]:
                        index_dump_end = i+j
                        break
                if index_dump_end+2 <= len(linelist):
                    if '----dump expr start----' in linelist[index_dump_end+2]:
                        for j in range(len(linelist)-(index_dump_end+2)):
                
                            if 'Function start: ' in linelist[index_dump_end+2+j]:
                                index_dump_end = index_dump_end+2+j
                                break
                            if j == len(linelist)-(index_dump_end+2) -1:
                                index_dump_end = index_dump_end+2+j
                                break

                if index_dump_start == -1 or index_dump_end == -1:
                    print( 'something wrong inside filter_instruction_in_function')
                    fout.close()
                    return
                
                #print (len(linelist))
                #print('['+str(index_dump_start-1) + ',' + str(index_dump_end+1) +']')
                for j in range(index_dump_start-1,index_dump_end+1): 
                    contain_symbol[j] = True
    fout = open(filepath_out,'w')
    for i in range(len(linelist)):
        if contain_symbol[i] == True:
            fout.write(linelist[i])
    fout.close()            
    

def output_z3_test(f1path,f2path):
    fin1 = open(f1path,'r')
    linelist1 = fin1.readlines()
    fin1.close()
    fin2 = open(f2path,'r')
    linelist2 = fin2.readlines()
    fin2.close()
    
    count1 = 0;
    count2 = 0;    
    
    for i in range(len(linelist1)) : 
        if '----dump z3 start----' in linelist1[i]:
            count1 = count1 + 1

    for i in range(len(linelist2)) : 
        if '----dump z3 start----' in linelist2[i]:
            count2 = count2 + 1
    
    if count1 == count2:
        return True
    else:
        return False
                
            
            

def output_z3_compare(f1path,f2path,foutpath):
    fin1 = open(f1path,'r')
    linelist1 = fin1.readlines()
    fin1.close()
    fin2 = open(f2path,'r')
    linelist2 = fin2.readlines()
    fin2.close()

    fout = open(foutpath,'w')
    start2 = 0;
    for i in range(len(linelist1)) : 
        if '----dump z3 start----' in linelist1[i]:
            for j in range(len(linelist1)-i):
                if '----dump z3 end----' in linelist1[i+j]:
                    fout.write("(assert (forall ((stdin0 (Array (_ BitVec 32) (_ BitVec 8))))\n")
                    fout.write("(= \n")
                    for temp in range(i+2,i+j):
                        fout.write(linelist1[temp])
                    fout.write("\n")
                    for i2 in range(start2,len(linelist2),1):
                        if '----dump z3 start----' in linelist2[i2]:
                            for j2 in range(len(linelist2)-i2):
                                if '----dump z3 end----' in linelist2[i2+j2]:
                                    start2 = i2+j2+1
                                    for temp in range(i2+2,i2+j2):
                                        fout.write(linelist2[temp])
                                    break
                            break

                    fout.write(")))\n(check-sat)\n")
                    fout.write("(reset)\n")
                    #i = i+j+1
                    break
    fout.close()
def write_three_lines_to_cfg (fout,index,linelist):
    fout.write("\n")            
    fout.write(linelist[index-1])
    fout.write(linelist[index])
    fout.write(linelist[index+1]) 

def write_expression_to_cfg (fout,index,linelist):
    if '----dump expr start----' in linelist[index] :
        start_index = index                
        end_index = index
        for j in range(len(linelist)-1 -(index) +1) :
            if '----dump z3 end----' in linelist[index+j] :
                end_index = index+j
                break
        fout.write("\n")
        for k in range(end_index-start_index+1) :
            fout.write(linelist[index+k])    
        fout.write("\n")



def output_cfg_lifter(function_name,finpath,foutpath):

    fin = open(finpath,'r')
    linelist = fin.readlines()
    fout = open(foutpath,'w')

    for i in range(len(linelist)-1) :
        first_line = re.search(function_name,linelist[i]) 
        second_line = "TransferTobasic (used for lifter.ll)" in linelist[i+1]    
        if first_line and second_line:
            block_start = re.search("BB from (.+?) to (.+?) ",linelist[i+1]).group(1)
            block_end = re.search("BB from (.+?) to (.+?) ",linelist[i+1]).group(2)
            fout.write("BB:["+block_start+"->"+block_end+"]\n")
        
        add_truestatment = "Add constraint for trueStatement" in linelist[i] and "----dump expr start----" in linelist[i+3]
        if add_truestatment :
            write_three_lines_to_cfg(fout,i,linelist)    #write whole Add constraint for trueStatement to cfg
            write_expression_to_cfg(fout,i+3,linelist)

        add_direct_truefalsestatment = ("Add direct constraint for trueStatement" in linelist[i] or "Add direct constraint for falseStatement" in linelist[i])and "----dump expr start----" in linelist[i+3]
        if add_direct_truefalsestatment : 
            write_three_lines_to_cfg(fout,i,linelist)    #write whole Add direct constraint for true/falseStatement to cfg
            write_expression_to_cfg(fout,i+3,linelist)

        #print(str(i)+":"+linelist[i])
        #print(len(linelist))
        add_return = "Inside Ret state.pc ++" in linelist[i] and "----dump expr start----" in linelist[i+3]
        if add_return :
            write_three_lines_to_cfg(fout,i,linelist)    #write Ret to cfg
            write_expression_to_cfg(fout,i+3,linelist)  
    fout.close()


#naive checking num in which range provided by list_num
def return_num_in_list_num(num,list_num):
    result = -1
    i = 0
    while i < (len(list_num) - 1) :
        if num > int(list_num[i]) and num < int(list_num[i+1]) :
            result = i
            break
        else :
            i += 1
                    
    return result     

def output_cfg_generated(function_name,finsource,finpath,foutpath):
    fsource = open(finsource,'r')
    sourcelist = fsource.readlines()
    
    fin = open(finpath,'r')
    linelist = fin.readlines()
    fout = open(foutpath,'w')
    
    #to have the block layout from source file
    comment_string = "//# Function name "+function_name+" ,Start of Block"
    i = 0
    block_start_num = []
    block_start_line = -1
    block_end_line = -1
    while i < len(sourcelist) :
        find_block = re.search(comment_string,sourcelist[i]) 
        if find_block :
            block_start_line = i
            block_num = int(re.search("Start of Block (.+?)",sourcelist[i]).group(1))
            block_end = re.search("//# End of Block "+str(block_num), sourcelist[i])

            while not block_end:
                i += 1  
                block_end = re.search("//# End of Block "+str(block_num), sourcelist[i])

            block_end_line = i
            block_start_num.append(block_start_line)
            #fout.write("BB "+ str(block_num) +" : " +str(block_start_line)+" - " + str(block_end_line) + "\n")
            #print (block_num)
            #print (block_start_line)
            #print (block_end_line)

        else :
            i += 1

    block_start_num.append(block_end_line)
    #print (block_start_num)
    
    i = 0
    for i in range(len(linelist)-1) :
        #this block transfer the linenumber to block in lifter.bc
        first_line = re.search(function_name,linelist[i]) 
        second_line = "TransferTobasic (used for generatedc.ll)" in linelist[i+1]    
        if first_line and second_line:
            line_src = int(re.search("Linenumber of instruction in c file from (.+?) to (.+?) ",linelist[i+1]).group(1))
            line_des = int(re.search("Linenumber of instruction in c file from (.+?) to (.+?) ",linelist[i+1]).group(2))
            block_start = return_num_in_list_num(line_src,block_start_num)
            block_end = return_num_in_list_num(line_des,block_start_num)
            fout.write("BB_lifter:["+str(block_start)+"->"+str(block_end)+"]\n")
        
        #just output the block in generated.bc being executed
        first_line = re.search(function_name,linelist[i]) 
        second_line = "TransferTobasic (used for lifter.ll)" in linelist[i+1]    
        if first_line and second_line:
            block_start = re.search("BB from (.+?) to (.+?) ",linelist[i+1]).group(1)
            block_end = re.search("BB from (.+?) to (.+?) ",linelist[i+1]).group(2)
            fout.write("BB_decompile:["+block_start+"->"+block_end+"]\n")
        
        add_truestatment = "Add constraint for trueStatement" in linelist[i] and "----dump expr start----" in linelist[i+3]
        if add_truestatment :
            write_three_lines_to_cfg(fout,i,linelist)    #write whole Add constraint for trueStatement to cfg
            write_expression_to_cfg(fout,i+3,linelist)


        add_direct_truefalsestatment = ("Add direct constraint for trueStatement" in linelist[i] or "Add direct constraint for falseStatement" in linelist[i])and "----dump expr start----" in linelist[i+3]
        if add_direct_truefalsestatment : 
            write_three_lines_to_cfg(fout,i,linelist)    #write whole Add direct constraint for true/falseStatement to cfg
            write_expression_to_cfg(fout,i+3,linelist)


        add_return = "Inside Ret state.pc ++" in linelist[i] and "----dump expr start----" in linelist[i+11]
        if add_return :
            write_three_lines_to_cfg(fout,i,linelist)    #write Ret to cfg
            write_expression_to_cfg(fout,i+11,linelist)  #11 means skip two transfertobasic            
    fout.close()

def analyze_results(i,filename,function_name):
    function_name = function_name[:-1]
    klee_log_filepath_no_suffix='/tmp/klee_'+filename +'_'+ function_name
    angr_log_filepath_no_suffix='/tmp/angr_'+filename +'_'+ function_name
    
    
    filename_z3 = filename+"_" +function_name+"_z3"
    filepath_z3 = os.path.join(directname_z3, filename_z3)
    filename_txt = filename+"_diff.txt"
    filepath_generatedc = os.path.join(directname_generatedc, filename+".c")
    
    klee_decompile_path = klee_log_filepath_no_suffix

    
    file_name_decompiler = klee_decompile_path +"_cfg.txt"
    file_reorder_decompiler = klee_decompile_path +"_cfg_decompiler_reorder.txt"
    file_ir_decompiler = klee_decompile_path +"_ir_decompiler.txt"
    file_ir_lifter = angr_log_filepath_no_suffix+"_ir_third_flip.txt"

    #filter the symbol generated from uclibc durin symbolic comparison
    #function_list = [function_name,"__klee_posix_wrapped_main"]
    function_list = [function_name]
    exclude_function_list = ["__user_main","__uClibc_main"]
    print("start analyzing results")
    filter_instruction_in_function(klee_decompile_path +"_test.txt",klee_decompile_path + "_symbolic_executation.txt",function_list,exclude_function_list)
    print("finished decompile analysis")
    #use lifter here since we do not need block comparison now
    output_cfg_lifter(function_name,klee_decompile_path +"_symbolic_executation.txt",klee_decompile_path +"_cfg.txt")
    print("finished cfg decompile")
    print("start converting cfg to ir")

    #set lifter as true here since we do not need block comparison now
    convert.cfg_to_ir(file_name_decompiler,file_reorder_decompiler,file_ir_decompiler,True)
    print("finished decompiler cfg to ir")
    convert.ir_reorder(file_ir_decompiler)
    sat_unsat = convert.ir_to_z3(angr_log_filepath_no_suffix+".txt",file_ir_lifter,file_ir_decompiler,filepath_z3)
    '''
    if sat_unsat == True:
        #run_cmd("z3 "+ filepath_z3+"_unsat" + " > "+directname_diff + "/" + filename_z3+"_unsat", 30)
        #os.system("timeout 30s z3 "+ filepath_z3+"_unsat" + " > "+directname_diff + "/" + filename_z3+"_unsat")    
    else:
        #run_cmd("z3 "+ filepath_z3 + " > "+directname_diff + "/" + filename_z3, 30)
        #os.system("timeout 30s z3 "+ filepath_z3 + " > "+directname_diff + "/" + filename_z3)
    '''
    #os.system("cat " + directname_diff + "/" + filename_z3)
    
def main():
    i = 0
    '''
    for filename_c in os.listdir(directname_originalc):
        analyze_results(i,filename_c)
    '''
    i += 1

if __name__ == "__main__":
    main()


