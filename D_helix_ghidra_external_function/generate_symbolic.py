import os
import sys
import math
import time
from time import sleep
import numpy as np
import re
import analyze_results
import analyze_angr
import angr
import traceback
import claripy
import sys
import multiprocessing
import time
from multiprocessing import Pool
import threading
import signal
import subprocess
import platform
import atexit
from func_timeout import func_set_timeout, FunctionTimedOut
#import timeout_decorator
from claripy.backends.backend_smtlib_solvers import *
from angr.analyses import (
    VariableRecoveryFast,
    CallingConventionAnalysis,
    CompleteCallingConventionsAnalysis,
    CFGFast,
    Decompiler,
)
import pickle


foreverloop = False
time_out_num = 30
directname_originalclang = "./test_muqi/originalclang"
directname_generated_whole_c = "./test_muqi/generated_whole_c"
directname_generated_html = "./test_muqi/generated_html"
directname_folder_for_project="./test_muqi/generated_function_c/project_folder"
directname_folder_for_log = "./test_muqi/generated_function_c/log_for_compile"
directname_generatedbc = "./test_muqi/generatedbc"
directname_generatedll = "./test_muqi/generatedll"
directname_generatedklee = "./test_muqi/generatedklee"
directname_model = "./test_muqi/model_prompt"
directname_log_klee = "./test_muqi/log_klee"

directname_diff = "./test_muqi/diff"
directname_z3 = "./test_muqi/z3"
directname_log = "./test_muqi/log"
directname_cfg = "/home/muqi/cfg"

directname_function_name = "./function_name"
directname_function_address = "./function_address"
angrlog_file = "./log_angr"
kleelog_file = "./log_klee"
bothwork_file = "./both_work"

bits_version = 64

angr_log = "/tmp/angr.txt"
angr_ir_first = "/tmp/angr_ir_first.txt"
angr_ir_second = "/tmp/angr_ir_second.txt"
angr_ir_third = "/tmp/angr_ir_third.txt"
angr_ir_third_flip = "/tmp/angr_ir_third_flip.txt"

log_file = 'angrlog_pcode'

llvm_dis_addr = "/home/muqi/llvm-3.8/llvm-src/build/bin/llvm-dis"

avoid_function_list=[
    "_init","free","abort","strtoimax","__errno_location","strncmp","_exit","__fpending","strcpy","puts","reallocarray","textdomain","fclose","bindtextdomain","__ctype_get_mb_cur_max",
    "strlen","__stack_chk_fail","getopt_long","mbrtowc","gettext","strchr","printf","strrchr","lseek","memset","memcmp","fputs_unlocked","ferror_unlocked","calloc","strcmp","fputc_unlocked",
    "fprintf","strtol","memcpy","kill","fileno","malloc","fflush","nl_langinfo","__freading","strsignal","setlocale","error","fseeko","__libc_current_sigrtmin","sprintf","exit","fwrite","__libc_current_sigrtmax",
    "mbsinit","iswprint","__ctype_b_loc","__cxa_finalize","_start","deregister_tm_clones","register_tm_clones","__do_global_dtors_aux","frame_dummy","__libc_csu_init","__libc_csu_fini","atexit","_fini",
    "fdopen","fopen","stpcpy","setlocale_null_unlocked_z3","memchr","rawmemchr","strspn","xrealloc","mempcpy","strtoumax","strpbrk","gl_scratch_buffer_dupfree", "memrchr","lcm","localeconv","strftime",
    "stpncpy","timegm","strftime","getdelim"
    ,"__snprintf_chk","chroot","__fprintf_chk","__vfprintf_chk","__assert_fail","__asprintf_chk","ioctl"," __libc_start_main","warnx","mkdir","strstr","getpid"
    ,"ceil","cos","sin","fmpz_add","floor","tan"
    ,"isatty","towlower","iswspace","setenv","strncasecmp","unsetenv",
    "__sched_cpucount","towupper","inet_pton","regcomp","g_sinf","g_log2f",
    "pthread_setspecific", "nearbyint", "pthread_cond_init","floorf","cfsetispeed","sigdelset",
    "pthread_condattr_setclock", "getnameinfo","sigaddset",
    "BN_sub","trunc","BIO_ctrl","ttyname_r","iswalnum","EVP_PKEY_derive_set_peer",
    "fnmatch","settimeofday","EC_POINT_cmp","EVP_PKEY_keygen","pthread_mutexattr_settype",
    "iswctype","EVP_PKEY_derive","BN_num_bits","EVP_PKEY_derive_init","pthread_mutexattr_settype",
    "EVP_CIPHER_CTX_set_padding","EVP_PKEY_keygen_init","EC_GROUP_cmp","execlp","EVP_DecryptUpdate"
    
    ]    #this is a list of functions which are system functions

checked_function_list = ["set_char_quoting","raw_hasher","locale_charset","xmax","strcspn","freadahead","iso_week_days","mbs_align_pad","fileinfo_name_width","ino_map_insert",
"idle_string", "argv_iter_n_args","key_init","base64_encode_alloc", "fread_unlocked","tm_year_str","xstrmode","wcslen","split","replay_step_get_filename","wmemset"
"ul_pty_get_child"
]

dic_funcname_funcargs = {}
def find_functionargs(filename_c):
    filename_whole_decompiled_c = filename_c
    filepath_function_namec= os.path.join(directname_function_name,filename_whole_decompiled_c.replace(".c",""))
    
    function_name_list = []
    first_function_name = ""
    try:
        fin = open(filepath_function_namec,'r')
        linelist = fin.readlines()
        fin.close()
        first_function_name = linelist[0][:-1]
        for i in range(len(linelist)) :
            if linelist[i][:-1] in avoid_function_list or  linelist[i][:-1] in checked_function_list:
                continue
            function_name_list.append(linelist[i][:-1])
    except:
        print(filename_c+" not work!!!")
    
    for i in range(len(function_name_list)):
        braket_count = 0
        start_function = False
        k = 0

        function_folder_name = filename_whole_decompiled_c.replace(".c","")+ "_folder"
        filepath_folder_for_project = os.path.join(directname_folder_for_project,function_folder_name)
        filepath_function_decompiled_c = os.path.join(filepath_folder_for_project,filename_whole_decompiled_c.replace(".c","")+"_"+function_name_list[i]+".c")
        fin = open( filepath_function_decompiled_c,'r')
        originalc_linelist = fin.readlines()
        fin.close()
        while k < len(originalc_linelist):
            if  (";" not in  originalc_linelist[k] )and ( (  function_name_list[i].replace(".","_")+"\n" in originalc_linelist[k][0:len(function_name_list[i])+1] and "(" in  originalc_linelist[k+1]) or ( function_name_list[i].replace(".","_")+"(" in originalc_linelist[k][0:len(function_name_list[i])+1])or (" "+function_name_list[i].replace(".","_")+"(" in originalc_linelist[k]) or ( " "+function_name_list[i].replace(".","_")+"\n" in originalc_linelist[k] and "(" in originalc_linelist[k+1] )) :
                #print("!!!!!!!!!code" +str(k)+" : "+originalc_linelist[k])
                function_declare_start = k
                function_declare_end = k

                while function_declare_start > 0:
                     if "\n" in originalc_linelist[function_declare_start][0] :
                        function_declare_start += 1
                        break
                     function_declare_start -= 1

                while function_declare_end < len(originalc_linelist):
                    if ")" in originalc_linelist[function_declare_end] :
                        break
                    function_declare_end += 1
                
                function_declare_string = ""
                for function_iter in range(function_declare_start,function_declare_end + 1):
                    function_declare_string += originalc_linelist[function_iter].replace("\n","")
                global dic_funcname_funcargs 
                dic_funcname_funcargs[function_name_list[i]] = function_declare_string
                print("In find_functionargs")
                print(function_declare_start)
                print(function_declare_end)
                print(function_name_list[i])
                print(function_declare_string)

                
                if "{" == originalc_linelist[function_declare_end+1][0] and ";" not in originalc_linelist[function_declare_end]:
                    braket_count = 1
                    start_function = True
                    temp_value = function_declare_start
                    while temp_value <= function_declare_end:
                        temp_value += 1
                    k = function_declare_end + 3
                
            if "{" in originalc_linelist[k] :
                braket_count += 1
            
            if braket_count > 0 and start_function == True:
                #print(originalc_linelist[k])
                #comment out FS_OFFSET
                if ")(in_FS_OFFSET + 0x28);" in originalc_linelist[k] :
                    #print(originalc_linelist[k] )
                    originalc_linelist[k] = "//comment in_FS_OFFSET\n"
                elif ")(in_FS_OFFSET + 0x28))" in originalc_linelist[k] :
                    #print(originalc_linelist[k] )
                    originalc_linelist[k] = "if (1) {\n"
                else:
                    #print(originalc_linelist[i] )
                    originalc_linelist[k] = originalc_linelist[k]
            
            if "}" in originalc_linelist[k] :
                braket_count -= 1
                
            if braket_count == 0 and start_function == True:
                break
            
            k += 1
    
directname_objdump = "./test_muqi/objdump"
def angr_running_pointer(arg1,arg2,angr_project,pcfg_input,filename,concrete_input_num):

    filepath_originalclang = arg1
    required_function = arg2
    log_filepath='/tmp/angr_'+filename +'_'+ required_function +'.txt'
    
    
    
    p = angr_project
    function_for_explore = p.kb.functions.function(name=required_function)
    required_address = 0

    filepath_originalclang = os.path.join(directname_originalclang, filename)
    filepath_objdump = os.path.join(directname_objdump, filename)
    try :
        required_address = p.loader.find_symbol(required_function).rebased_addr
    except:
        os.system("objdump -t " +filepath_originalclang +">"+filepath_objdump)
        with open(filepath_objdump,'r') as objdump_file:
            objdump_lines = objdump_file.readlines()
            for i in range(len(objdump_lines)):
                if required_function+"." in objdump_lines[i] :
                    fullname_required_function = objdump_lines[i].split(" ")[-1]
                    try:
                        required_address = p.loader.find_symbol(fullname_required_function[:-1]).rebased_addr
                    except:
                        pass
                    break

    if "FUN_" in required_function and required_address == 0:
        required_address = int(re.search("FUN_(.+?)_",required_function+"_").group(1),16)

    print("In angr running Pointer")
    print(hex(required_address))
    print(arg1)
    print(arg2)

    #use cfgfast to identify the boundry of basic block
    #pcfg = p.analyses.CFGFast(normalize = True)
    pcfg = pcfg_input
    try:
        pcfg = pcfg.functions.get(required_address).transition_graph
    except:
        pass
    #write basic block info to file
    #with open('/tmp/angr.txt','w') as muqi_file:
    with open(log_filepath,'w') as muqi_file:
        print('Filename: ',filepath_originalclang, file=muqi_file)
        print('Function: ',required_function, file=muqi_file)

        for node in pcfg.nodes():
            if node.addr >= required_address:
                print("BasicBlock_cfg:["+str(hex(node.addr))+" -> "+ str(hex(node.addr+node.size))+"]", file=muqi_file)

    #p = angr.Project(filepath_originalclang)
    #p.factory.entry_state().block().vex.pp()
    args = []
    '''
    for i in range(20):
        #args.append(claripy.BVS('angr_arg'+str(i), 8*8))
         args.append(claripy.BVV(concrete_input_num, 64))
    '''
    for i in range(20):
        args.append(claripy.BVS('angr_arg'+str(i), 8*8))

    global dic_funcname_funcargs 
    function_declare_string = dic_funcname_funcargs[required_function]

    #print("In angr_running_pointer before, printing function_args_string:")
    #print(function_declare_string)
    #print(dic_funcname_funcargs)
    try:
        function_args_string = re.search("\((.+?)\)", function_declare_string).group(1)
    except:
        function_args_string = ""
    #print(filename + "_" + required_function)
    #print("In angr_running_pointer, printing function_args_string:")
    print(function_args_string)
    function_args_list = function_args_string.split(",")
    for i in range(len(function_args_list)):
        if "*" in function_args_list[i] :
            args[i] = claripy.BVS('angr_arg'+str(i), 256*8)
            args[i] = angr.PointerWrapper(args[i],buffer=True)
            print("inside functionargslist")
            print("i is: "+ str(i)) 
    try:
        state = p.factory.call_state(log_filepath, required_address,args[0],args[1],args[2],args[3],args[4],args[5],args[6],args[7],args[8],args[9],args[10],add_options={angr.options.CALLLESS,angr.options.STRINGS_ANALYSIS,angr.options.ZERO_FILL_UNCONSTRAINED_MEMORY,angr.options.ZERO_FILL_UNCONSTRAINED_REGISTERS},remove_options=angr.options.simplification)
        sm = p.factory.simulation_manager(state)
    except:
        print("call state parameter error: " + filepath_originalclang + " function:" + required_function + "\n")
        with open(log_file, "a") as myfile:
            myfile.write("call state parameter error: " + filepath_originalclang + " function:" + required_function + "\n")
            return 
            #myfile.write("not working\n")
    

    
    '''
    simgr = p.factory.simulation_manager(state)
    simgr.use_technique(angr.exploration_techniques.LoopSeer(cfg=cfg, functions='main', bound=None))
    simgr.run()
    '''
    
    try:
        print("working on " +filepath_originalclang + " function:" + required_function + "\n")
        with open(log_file, "a") as myfile:
            myfile.write("working on" + filepath_originalclang + " function:" + required_function + "\n")
        #sm.explore(cfg=pcfg)
        '''
        if foreverloop == False:
            sm.use_technique(angr.exploration_techniques.LoopSeer(cfg=pcfg_input, functions=[required_function],bound=2,use_header = True))
        '''
        #sm.use_technique(angr.exploration_techniques.LoopSeer(cfg=pcfg_input, functions=[required_function],bound=1))
        os.system("rm /tmp/call_count_"+filename+"_"+required_function+"_angr_args.txt")
        sm.run(read_args_txt ="/tmp/call_count_"+filename+"_angr_numargs.txt",
                call_count_path = "/tmp/call_count_"+filename+"_"+required_function+"_angr_args.txt")
        with open(log_file, "a") as myfile:
            myfile.write("worked\n")
    except:
        with open(log_file, "a") as myfile:
            myfile.write("not working\n")



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

def main_each_function_klee(i,function_name_list,filename,filepath_originalclang,concrete_input_num):

    function_name = function_name_list[i]
    filepath_generatedbc = os.path.join(directname_generatedbc, filename+"_"+function_name[:-1]+".bc")

    if os.path.isfile(filepath_generatedbc)  :
        #run prompt for symbolic execution
        #generate model.txt for prompt for that function
        #print(filepath_generatedbc)
        model_function_name = "model"+filename+"_"+function_name[:-1] +".txt"
        filepath_prompt_model_on_function = os.path.join(directname_model, model_function_name)
        log_klee_function_name = "log_klee"+filename+"_"+function_name[:-1] +".txt"
        log_klee_function_name_error = "log_klee"+filename+"_"+function_name[:-1] +"_error.txt"
        filepath_log_klee = os.path.join(directname_log_klee,log_klee_function_name)
        filepath_log_klee_error = os.path.join(directname_log_klee,log_klee_function_name_error)
        #os.system("rm /tmp/klee_"+filename+"_"+function_name[:-1] +"_test.txt")

        #'''
        try:
            fopen = open (filepath_log_klee,'r')
            fopenlines = fopen.read().splitlines()
            last_line = fopenlines[-1]
        except:
            last_line = "NONE"


        if 'terminating state' in last_line :
            return
        #else:
        #'''
        os.system("rm /tmp/klee_"+filename+"_"+function_name[:-1] +"_test.txt")
        os.system("rm /tmp/klee_"+filename+"_"+function_name[:-1] +"_external_function.txt")
        #os.system("rm /tmp/klee_"+filename+"_"+function_name[:-1] +"_external_input.txt")
        os.system("rm /tmp/klee_"+filename+"_"+function_name[:-1] +"_external_input_bool.txt")
        #'''
        f = open(filepath_prompt_model_on_function, "w")
        f.write("global settings:\ndata models:\nfunction models:\nlifecycle model:\n    entry-point "+ function_name.replace(".","_"))
        #f.write("global settings: array size 0;\ndata models:(0 = w) where w is argsize "+function_name+" arg 0;\nfunction models:\nlifecycle model:\n    entry-point "+ function_name)
        f.close()
        #'''
        #f = open("/tmp/klee_"+filename+"_"+function_name[:-1] +"_external_input.txt", "w")
        f = open("/tmp/klee_"+filename+"_"+function_name[:-1] +"_external_input_bool.txt", "w")
        f.write(str(concrete_input_num))
        #f.write("global settings: array size 0;\ndata models:(0 = w) where w is argsize "+function_name+" arg 0;\nfunction models:\nlifecycle model:\n    entry-point "+ function_name)
        f.close()
        
        if foreverloop == False:
            print("\ntimeout 30s /home/muqi/PROMPT_external_function/PROMPT/build/bin/klee  -prose-api-model="+filepath_prompt_model_on_function+ " --search=bfs --loop-bound=2 --solver-backend=z3 --posix-runtime " + filepath_generatedbc + " > "+ filepath_log_klee + " 2> "+ filepath_log_klee_error)
        else:
            print("\ntimeout 30s /home/muqi/PROMPT_external_function/PROMPT/build/bin/klee  -prose-api-model="+filepath_prompt_model_on_function+ " --search=bfs  --solver-backend=z3 --posix-runtime " + filepath_generatedbc + " > "+ filepath_log_klee + " 2> "+ filepath_log_klee_error)
    
        if foreverloop == False:
            run_cmd("/home/muqi/PROMPT_external_function/PROMPT/build/bin/klee -prose-api-model="+filepath_prompt_model_on_function+ "  --loop-bound=2  --search=bfs --solver-backend=z3 --posix-runtime " + filepath_generatedbc + " > "+ filepath_log_klee + ' 2> '+ filepath_log_klee_error,time_out_num)
        else:
            run_cmd("/home/muqi/PROMPT_external_function/PROMPT/build/bin/klee -prose-api-model="+filepath_prompt_model_on_function+ "   --search=bfs --solver-backend=z3 --posix-runtime " + filepath_generatedbc + " > "+ filepath_log_klee + ' 2> '+ filepath_log_klee_error,time_out_num)
        #os.system("rm /tmp/klee_"+filename+"_"+function_name[:-1] +"_external_input.txt")
        os.system("rm /tmp/klee_"+filename+"_"+function_name[:-1] +"_external_input_bool.txt")
@func_set_timeout(120)
#@timeout_decorator.timeout(time_out_num, use_signals=False)
def main_each_function_angr(i,function_name_list,filename,pcfg_angr,angr_project,filepath_originalclang,concrete_input_num):
    print("99999")
    angr_work = True
    klee_work = True
    angr_log_work = True
    klee_log_work = True
    function_name = function_name_list[i]
    filepath_generatedbc = os.path.join(directname_generatedbc, filename+"_"+function_name[:-1]+".bc")
    
    filepath_functionc = os.path.join(directname_folder_for_project,filename+"_folder/"+filename+"_"+function_name[:-1]+".c")

    model_function_name = "model"+filename+"_"+function_name[:-1] +".txt"
    filepath_modelprompt = os.path.join(directname_model, model_function_name)


    angr_filepath = os.path.join(directname_z3, filename+"_"+function_name[:-1]+"_angr")
    klee_filepath = os.path.join(directname_z3, filename+"_"+function_name[:-1]+"_klee")
    angr_external_filepath = '/tmp/call_count_'+filename +'_'+ function_name[:-1] +'_angr_args.txt'
    klee_external_filepath = '/tmp/klee_'+filename+'_'+function_name[:-1] +'_external_function.txt'

    z3_filepath = os.path.join(directname_z3, filename+"_"+function_name[:-1]+"_z3")
    z3_filepath_unsat = os.path.join(directname_z3, filename+"_"+function_name[:-1]+"_z3_unsat")
    angr_log_filepath = '/tmp/angr_'+filename +'_'+ function_name[:-1] +'.txt'

    print("in main_each_function_angr")
    if os.path.isfile(z3_filepath) or os.path.isfile(z3_filepath_unsat)  :
        print(z3_filepath)
        return


    print("99999")
    if os.path.isfile(filepath_generatedbc) :
        log_klee_function_name = "log_klee"+filename+"_"+function_name[:-1] +"_error.txt"
        filepath_log_klee = os.path.join(directname_log_klee,log_klee_function_name)
        print("123")
        try:
            f = open( filepath_log_klee, 'r')
            print("124")
            log_lines = f.readlines()[-1]
            f.close()
            if 'KLEE: done:' not in log_lines:
                klee_work = False
                f = open(kleelog_file, "a")
                f.write(filename+": "+function_name + " is wrong! not terminated\n")
                f.close()
        except:
            klee_work = False
            f = open(kleelog_file, "a")
            f.write(filename+": "+function_name + " is wrong!  cannot open logfile\n")
            f.close()
        

        #'''
        if klee_work == True:
            #angr_running_pointer(filepath_originalclang,function_name[:-1],angr_project,pcfg_angr,filename,concrete_input_num)
            '''
            try:
                print("before angr_running_pointer")
                angr_running_pointer(filepath_originalclang,function_name[:-1],angr_project,pcfg_angr,filename,concrete_input_num)
            '''
            try:
                '''
                angr_running_pointer(filepath_originalclang,function_name[:-1],angr_project,pcfg_angr,filename)
                def angr_running_pointer(arg1,arg2,angr_project,pcfg_input,filename):
                '''
                arg1 = filepath_originalclang
                arg2 = function_name[:-1]
                pcfg_input = pcfg_angr
                #print("inside angr_running_pointer")
                #print(arg2)
                #print(filename)
                filepath_originalclang = arg1
                required_function = arg2
                log_filepath='/tmp/angr_'+filename +'_'+ required_function +'.txt'
                #print(log_filepath)
                p = angr_project
                required_address = 0

                filepath_originalclang = os.path.join(directname_originalclang, filename)
                filepath_objdump = os.path.join(directname_objdump, filename)
                try :
                    required_address = p.loader.find_symbol(required_function).rebased_addr
                except:
                    os.system("objdump -t " +filepath_originalclang +">"+filepath_objdump)
                    with open(filepath_objdump,'r') as objdump_file:
                        objdump_lines = objdump_file.readlines()
                        for i in range(len(objdump_lines)):
                            if required_function+"." in objdump_lines[i] :
                                fullname_required_function = objdump_lines[i].split(" ")[-1]
                                try:
                                    required_address = p.loader.find_symbol(fullname_required_function[:-1]).rebased_addr
                                except:
                                    pass
                                break
                    '''
                    os.system("objdump -t " +filepath_originalclang +">"+filepath_objdump)
                    with open(filepath_objdump,'r') as objdump_file:
                    '''
                if "FUN_" in required_function and required_address == 0:
                    required_address = int(re.search("FUN_(.+?)_",required_function+"_").group(1),16)

                #print(hex(required_address))

                if required_address == 0:
                    raise Exception('required_address is 0, cannot find function')
                #use cfgfast to identify the boundry of basic block
                #pcfg = p.analyses.CFGFast(normalize = True)
                pcfg = pcfg_input
                try:
                    pcfg = pcfg.functions.get(required_address).transition_graph
                except:
                    pass

                #write basic block info to file
                #with open('/tmp/angr.txt','w') as muqi_file:
                with open(log_filepath,'w') as muqi_file:
                    print('Filename: ',filepath_originalclang, file=muqi_file)
                    print('Function: ',required_function, file=muqi_file)

                    for node in pcfg.nodes():
                        #if node.addr >= required_address:
                        print("BasicBlock_cfg:["+str(hex(node.addr))+" -> "+ str(hex(node.addr+node.size))+"]", file=muqi_file)
                #p = angr.Project(filepath_originalclang)
                #p.factory.entry_state().block().vex.pp()
                args = []
                for i in range(20):
                    args.append(claripy.BVS('angr_arg'+str(i), 8*8))

                global dic_funcname_funcargs
                function_declare_string = dic_funcname_funcargs[required_function]
                try:
                    function_args_string = re.search("\((.+?)\)", function_declare_string).group(1)
                except:
                    function_args_string = ""
                print(function_args_string)
                function_args_list = function_args_string.split(",")
                for i in range(len(function_args_list)):
                    if "*" in function_args_list[i] :
                        args[i] = claripy.BVS('angr_arg'+str(i), 256*8)
                        args[i] = angr.PointerWrapper(args[i],buffer=True)
                        print("inside functionargslist")
                        print("i is: "+ str(i))

                try:
                    state = p.factory.call_state(log_filepath, required_address,args[0],args[1],args[2],args[3],args[4],args[5],args[6],args[7],args[8],args[9],args[10],add_options={angr.options.CALLLESS,angr.options.STRINGS_ANALYSIS,angr.options.ZERO_FILL_UNCONSTRAINED_MEMORY,angr.options.ZERO_FILL_UNCONSTRAINED_REGISTERS},remove_options=angr.options.simplification)

                    #state.add_log_path(log_filepath)
                    sm = p.factory.simulation_manager(state)
                except:
                    print("call state parameter error: " + filepath_originalclang + " function:" + required_function + "\n")
                    with open(log_file, "a") as myfile:
                        myfile.write("call state parameter error: " + filepath_originalclang + " function:" + required_function + "\n")
                        #myfile.write("not working\n")
                #state.add_log_path(log_filepath)

                for function in p.kb.functions:
                   func_name = pcfg_input.functions.get(function).name
                   if func_name == required_function :
                      sm.input_jumpout_edge(list(pcfg_input._get_jumpout_targets(pcfg_input.functions.get(function))))

                abort_address = []
                for function in p.kb.functions:
                   func_name = pcfg_input.functions.get(function).name
                   if func_name == "abort" :
                      #print(pcfg_input.functions.get(function))
                      abort_address.append(pcfg_input.functions.get(function).addr)
                sm.input_abort_edge(abort_address)

                try:
                    print("working on " +filepath_originalclang + " function:" + required_function + "\n")
                    with open(log_file, "a") as myfile:
                        myfile.write("working on" + filepath_originalclang + " function:" + required_function + "\n")
                    #sm.explore(cfg=pcfg)
                    '''
                    if foreverloop == False:
                        sm.use_technique(angr.exploration_techniques.LoopSeer(cfg=pcfg_input, functions=[required_function],bound=2,use_header = True))
                    '''
                    #sm.use_technique(angr.exploration_techniques.LoopSeer(cfg=pcfg_input, functions=[required_function],bound=1))
                    print("before sm.run()")
                    sm.run()
                    with open(log_file, "a") as myfile:
                        myfile.write("worked\n")
                except:
                    with open(log_file, "a") as myfile:
                        myfile.write("not working\n")

            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                f = open(angrlog_file, "a")
                f.write(filename+": "+function_name + " is wrong!\n")
                f.write(str(exc_type))
                f.write(fname)
                f.write(str(exc_tb.tb_lineno))
                f.close()
                angr_work = False
        #'''
        print("finished angr running pointer\n")
        print(klee_work)
        print(angr_work)
                
        #'''
        #start analyzing
        if klee_work == True and angr_work == True:
            try:
                print("Inside analysis of z3 \n")
                log_filepath_no_suffix='/tmp/angr_'+filename +'_'+ function_name[:-1] 
                print(log_filepath_no_suffix)
                angr_log = log_filepath_no_suffix+".txt"
                angr_ir_first = log_filepath_no_suffix+ "_ir_first.txt"
                angr_ir_second = log_filepath_no_suffix+"_ir_second.txt"
                angr_ir_third = log_filepath_no_suffix +"_ir_third.txt"
                angr_ir_third_flip = log_filepath_no_suffix+"_ir_third_flip.txt"
                
                analyze_angr.reset_global(angr_log,angr_ir_first,angr_ir_second,angr_ir_third,angr_ir_third_flip)
                analyze_angr.build_basic_block(angr_log,angr_ir_first,angr_ir_second,angr_ir_third,angr_ir_third_flip)
                analyze_angr.generate_ir_first_version(angr_log,angr_ir_first,angr_ir_second,angr_ir_third,angr_ir_third_flip)
                analyze_angr.generate_father_block_second_version(angr_log,angr_ir_first,angr_ir_second,angr_ir_third,angr_ir_third_flip)
                analyze_angr.generate_children_block_second_version(angr_log,angr_ir_first,angr_ir_second,angr_ir_third,angr_ir_third_flip)
                analyze_angr.cfg_to_ir(angr_ir_third,angr_ir_third_flip)
                analyze_angr.ir_reorder(angr_ir_third_flip)
                
            
            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                f = open(angrlog_file, "a")
                f.write(filename+": "+function_name + " is wrong during analyzing!\n")
                f.write(str(exc_type))
                f.write(fname)
                f.write(str(exc_tb.tb_lineno))
                f.close()
                angr_log_work = False
             #'''
                    
            #generate klee result
            if angr_log_work == True:
                try: 
                    analyze_results.analyze_results(i,filename,function_name)
                except:
                    klee_log_work = False 
                    f = open(kleelog_file, "a")
                    f.write(filename+": "+function_name + " is wrong during z3 analyzing!\n")
                    f.close()
                
            if klee_log_work == True and angr_log_work == True:
                f = open(bothwork_file, "a")
                f.write(filename+": "+function_name + " worked !\n")
                f.close()
'''
def correct_angr_numargs_using_ghidra(angr_args,filename,filepath_folder_for_project):
    try:
        read_binary_file = open(angr_args,"r")
        binary_function_call = read_binary_file.readlines()
        read_binary_file.close()
    except:
        binary_function_call = []
        return 
        
    write_binary_file = open(angr_args,"w")

    #print(filepath_folder_for_project)
    for i in range(len(binary_function_call)):
        
        func_addr_num =binary_function_call[i][:-1].split("|")
        function_name = func_addr_num[0]
        at_function_name_brack = "@"+function_name+"("
        required_calling_func_name = func_addr_num[1]
        required_calling_func_addr = func_addr_num[2]
        #print(at_function_name_brack)

        file_function_name = filename +"_"+ function_name
        try:
            file_function_name_bc = file_function_name+".bc"
            file_function_name_ll = file_function_name+".ll"
            filepath_generatedll = os.path.join(directname_generatedll, file_function_name_ll)
            filepath_generatedbc = os.path.join(directname_generatedbc,file_function_name_bc)

            os.system(llvm_dis_addr+" "+filepath_generatedbc+" -o "+filepath_generatedll)

            ghidra_code_file =  open(filepath_generatedll,"r")
            ghidra_code=ghidra_code_file.readlines()
            ghidra_code_file.close()
        except:
            print("Cannot open"+filepath_folder_for_project+"/"+file_function_name+"_modified.c")
            ghidra_code = []
            #return
        j = 0
        start_index = 0
        end_index = 0
        while j < len(ghidra_code):
            if at_function_name_brack in ghidra_code[j] and "define " in  ghidra_code[j]:

                start_index = j
                end_index = start_index
                #print(start_index)

                while end_index < len(ghidra_code) -2:
                    #we do not care how ghidra declare this function
                    if "}" in ghidra_code[end_index]:
                        j = len(ghidra_code)
                        break
                    end_index += 1
            j += 1

        print(start_index)
        print(end_index)
        print("---------------")
        if start_index == 0:
            print("We dont find following function in its modefiedc")
            print(file_function_name)
            continue

        for k in range(start_index,end_index+1):
            if "= call "in ghidra_code[k]:
                call_message = ghidra_code[k].replace(", ...","")
                calling_func_name = ""
                if "bitcast" in call_message:
                    try:
                        calling_func_name = re.search("@(.+?) ",call_message).group(1)
                    except:
                        print("forget about following stupid function")
                        print(call_message)
                        continue
                else:
                    try:
                        calling_func_name = re.search("@(.+?)\(",call_message).group(1)
                    except:
                        print("forget about following stupid function")
                        print(call_message)
                        continue
                print(calling_func_name)
                print(call_message)
                print(k)
                if required_calling_func_name == calling_func_name: 
                    try:
                        arglist = re.search("\((.+?)\)",call_message).group(1)
                    except:
                        arglist = ""
                    append_pointer = ""
                    num_of_args_ghidra = 0
                    if arglist != "":
                        num_of_args_ghidra = arglist.count(',') + 1
                        if num_of_args_ghidra > 0:
                            #add append_pointer
                            args_array = arglist.split(',')

                            for arg_i in range(num_of_args_ghidra):
                                append_pointer += str(args_array[arg_i].count('*'))
                    #print(arglist)
                    #print(num_of_args_ghidra)
                    #print(append_pointer)
                    #we just provide some fake function address
                    write_binary_file.write(function_name+"|"+required_calling_func_name+"|"+
                            required_calling_func_addr+
                            "|"+ str(num_of_args_ghidra)+"|"+append_pointer +"\n")
    write_binary_file.close()
'''

def correct_angr_numargs_using_ghidra(angr_project,angr_args,filename,filepath_folder_for_project):

    write_binary_file = open(angr_args,"w")

    #print(filepath_folder_for_project)
    for file_function_modefiedc in os.listdir(filepath_folder_for_project):

        if "_modified.c" not in file_function_modefiedc:
            continue

        function_name = file_function_modefiedc[len(filename)+1:].replace("_modified.c","")
        at_function_name_brack = "@"+function_name+"("
        print(at_function_name_brack)

        file_function_name = filename +"_"+ function_name
        try:
            file_function_name_bc = file_function_name+".bc"
            file_function_name_ll = file_function_name+".ll"
            filepath_generatedll = os.path.join(directname_generatedll, file_function_name_ll)
            filepath_generatedbc = os.path.join(directname_generatedbc,file_function_name_bc)

            os.system(llvm_dis_addr+" "+filepath_generatedbc+" -o "+filepath_generatedll)

            ghidra_code_file =  open(filepath_generatedll,"r")
            ghidra_code=ghidra_code_file.readlines()
            ghidra_code_file.close()
        except:
            print("Cannot open"+filepath_folder_for_project+"/"+file_function_name+"_modified.c")
            ghidra_code = []
            #return
        j = 0
        start_index = 0
        end_index = 0
        while j < len(ghidra_code):
            if at_function_name_brack in ghidra_code[j] and "define " in  ghidra_code[j]:

                start_index = j
                end_index = start_index
                #print(start_index)

                while end_index < len(ghidra_code) -2:
                    #we do not care how ghidra declare this function
                    if "}" in ghidra_code[end_index]:
                        j = len(ghidra_code)
                        break
                    end_index += 1
            j += 1

        #print(start_index)
        #print(end_index)
        #print("---------------")
        if start_index == 0:
            print("We dont find following function in its modefiedc")
            print(file_function_name)
            continue

        for k in range(start_index,end_index+1):
            if "= call "in ghidra_code[k]:
                call_message = ghidra_code[k].replace(", ...","").replace("(...)","(three_dot)")
                calling_func_name = ""
                if "bitcast" in call_message:
                    try:
                        calling_func_name = re.search("@(.+?) ",call_message).group(1)
                    except:
                        print("forget about following stupid function")
                        print(call_message)
                        continue
                else:
                    try:
                        calling_func_name = re.search("@(.+?)\(",call_message).group(1)
                    except:
                        print("forget about following stupid function")
                        print(call_message)
                        continue
                print(calling_func_name)
                print(call_message)
                print(k)
                if "bitcast" in call_message:
                    try:
                        arglist = re.search("bitcast (.+?)\*\)\((.*)",call_message).group(2)
                    except:
                        arglist = "three_dot"
                else:
                    try:
                        arglist = re.search("\((.*)",call_message).group(1)
                    except:
                        arglist = "three_dot"
                print("arglist")
                print(arglist)
                
                append_pointer = ""
                num_of_args_ghidra = 0
                if arglist != "three_dot":
                    #remove last bracket
                    arglist = arglist[:-1]
                    print(arglist.count('getelementptr'))
                    print(arglist)
                    for arg_i in range(arglist.count('getelementptr inbounds \(')):
                        print(arglist)
                        print(arg_i)
                        try:
                            replacement = re.search("getelementptr inbounds \((.+?)\)",arglist).group(1)
                            arglist = arglist.replace("("+replacement+")",'three_dot')
                        except:
                            print("this stupid function")
                            print(arglist)
                            print(arg_i)
                            continue
                    #print("arglist2")
                    #print(arglist)

                    num_of_args_ghidra = arglist.count(',') + 1
                    if num_of_args_ghidra > 0:
                        #add append_pointer
                        args_array = arglist.split(',')

                        for arg_i in range(num_of_args_ghidra):
                            if '*' in args_array[arg_i]:
                                if '* getelementptr' in  args_array[arg_i] or '* @' in  args_array[arg_i]:
                                    append_pointer += "999,"
                                else:
                                    append_pointer += str(args_array[arg_i].count('*'))+","
                            else:
                                append_pointer += str(args_array[arg_i].count('*'))+","
                #print("arglist:|"+arglist+"|")
                #print(arglist != "")
                #print("num of args_ghidra"+str(num_of_args_ghidra))
                #print(append_pointer)
                #we just provide some fake function address
                required_address = 0
                try:
                    required_address = angr_project.loader.main_object.plt[calling_func_name]
                except:
                    try :
                        required_address = angr_project.loader.find_symbol(calling_func_name).rebased_addr
                        '''
                        print("required_address = angr_project.loader.find_symbol(calling_func_name).rebased_addr")
                        tmp_address = angr_project.loader.find_symbol("reallocarray").rebased_addr
                        print("reallocarray")
                        print(tmp_address)
                        print(angr_project.loader.find_symbol("reallocarray").linked_addr)
                        print(angr_project.loader.find_symbol("reallocarray").relative_addr)
                        print(angr_project.loader.main_object.plt)
                        tmp_address2 = 0x4020d0
                        print(angr_project.loader.main_object.reverse_plt[tmp_address2])
                        '''
                    except:
                        pass
                write_binary_file.write(function_name+"|"+calling_func_name+"|"+
                        str(hex(required_address))+
                        "|"+ str(num_of_args_ghidra)+"|"+append_pointer +"\n")
    write_binary_file.close()

def main_each_program(filename):

    #reset dictionary
    global dic_funcname_funcargs 
    dic_funcname_funcargs = {}
        
        
    filename_c = filename + ".c"
    filename_html = filename + ".html"
    filename_bc = filename +".bc"
    filename_clang = filename
    filename_ll = filename+".ll"
    filepath_originalclang = os.path.join(directname_originalclang,filename_clang)
    filepath_generated_whole_c = os.path.join(directname_generated_whole_c, filename_c)
    filepath_generated_html = os.path.join(directname_generated_html, filename_html)
    filepath_generatedll = os.path.join(directname_generatedll, filename_ll)

    filepath_generated_function_name= os.path.join(directname_function_name,filename_clang)
    

    '''
    angr_project = angr.Project(filepath_originalclang, auto_load_libs=False, load_debug_info=True)
    pcfg_angr = angr_project.analyses[CFGFast].prep()(normalize=True, data_references=True)
    os.system("rm /tmp/call_count_"+filename+"_angr_numargs.txt")
    angr_project.analyses[angr.analyses.CompleteCallingConventionsAnalysis].prep()(recover_variables=True,analyze_callsites=True,num_args_path ="/tmp/call_count_"+filename+"_angr_numargs.txt")
    '''
    
    #'''
    try:
        angr_project = angr.Project(filepath_originalclang, auto_load_libs=False, load_debug_info=True)
        pcfg_angr = angr_project.analyses[CFGFast].prep()(normalize=True, data_references=True)
        os.system("rm /tmp/call_count_"+filename+"_angr_numargs.txt")
        angr_project.analyses[angr.analyses.CompleteCallingConventionsAnalysis].prep()(recover_variables=True,analyze_callsites=True,num_args_path ="/tmp/call_count_"+filename+"_angr_numargs.txt")
    except:
        f = open(angrlog_file, "a")
        f.write(filename+":  is wrong during cfg analyzing!\n")
        f.close()
        return 
    #'''


    '''
    print("start of cfg")
    filepath_cfg = os.path.join(directname_cfg,filename)
    
    if os.path.isfile(filepath_cfg) : 
        print("Inside open cfg")
        with open(filepath_cfg, "rb") as f:
            print("Inside open cfg")
            angr_project, pcfg_angr = pickle.load(f)
    else:
        #angr_project = angr.Project(filepath_originalclang, auto_load_libs=False, load_debug_info=True)
        #pcfg_angr = angr_project.analyses[CFGFast].prep()(normalize=True, data_references=True)
        try:
            angr_project = angr.Project(filepath_originalclang, auto_load_libs=False, load_debug_info=True)
            #pcfg_angr = angr_project.analyses.CFG(normalize=True)
            #pcfg_angr = angr_project.analyses.CFGFast(normalize = True)
            pcfg_angr = angr_project.analyses[CFGFast].prep()(normalize=True, data_references=True)
        except:
            f = open(angrlog_file, "a")
            f.write(filename+":  is wrong during cfg analyzing!\n")
            f.close()
            return
        
        with open(filepath_cfg, "wb") as f:
            print("Inside storing cfg")
            pickle.dump((angr_project, pcfg_angr), f)

    os.system("rm /tmp/call_count_"+filename+"_angr_numargs.txt")
    angr_project.analyses[angr.analyses.CompleteCallingConventionsAnalysis].prep()(recover_variables=True,analyze_callsites=True,num_args_path ="/tmp/call_count_"+filename+"_angr_numargs.txt")
    '''
    #write decompiled code 
    
    #generate function_folder
    function_folder_name = filename+ "_folder"
    filepath_folder_for_project = os.path.join(directname_folder_for_project,function_folder_name)
    filepath_folder_for_project_log = os.path.join(directname_folder_for_log,function_folder_name)
    os.system("mkdir "+filepath_folder_for_project)
    os.system("mkdir "+filepath_folder_for_project_log)
    
    function_filename_file = open(filepath_generated_function_name, 'r')
    function_name_list = function_filename_file.readlines()
    function_filename_file.close()
    
    
    concrete_input_num = 345
    #'''
    print("before correct_angr_numargs_using_ghidra")
    #return
    correct_angr_numargs_using_ghidra(angr_project,"/tmp/call_count_"+filename+"_angr_numargs.txt",filename,filepath_folder_for_project)
    #'''

    #write decompiled code 
    #return 
    #'''
    for i in range(len(function_name_list)):
        main_each_function_klee(i,function_name_list,filename,filepath_originalclang,concrete_input_num)
    
    print(function_name_list)
    #'''
    #'''
    print("before find_functionargs")
    find_functionargs(filename_c)
    print("after find_functionargs")
    
    print(function_name_list)
    for i in range(len(function_name_list)):
        #main_each_function_angr(i,function_name_list,filename,pcfg_angr,angr_project,filepath_originalclang,concrete_input_num)
        try:
            main_each_function_angr(i,function_name_list,filename,pcfg_angr,angr_project,filepath_originalclang,concrete_input_num)
        except :
            print("000000")
            #pass
        
    #'''
    

def z3_each_file(filename):
    filepath_z3 = os.path.join(directname_z3,filename)
    filepath_diff = os.path.join(directname_diff,filename)
    run_cmd("z3 "+filepath_z3+" > "+filepath_diff, 30)

def main():
    '''
    os.system("rm "+ angrlog_file)
    os.system("rm "+ kleelog_file)
    os.system("rm "+ bothwork_file)
    os.system("rm log_klee.txt")
    '''
    os.system("rm -r ./test_muqi/generatedbc/klee-out*")
    #os.system("rm -r ./test_muqi/generatedbc/*")
    i = 0
    filenames = []
   
    pool = Pool()
    pool.map(main_each_program, os.listdir(directname_originalclang)) 
    j = 0
    
    '''
    pool = Pool()
    pool.map(z3_each_file, os.listdir(directname_z3))
    '''
    #os.system("clear")
    #os.system("cat "+ directname_diff+"/*")

if __name__ == "__main__":
    main()

