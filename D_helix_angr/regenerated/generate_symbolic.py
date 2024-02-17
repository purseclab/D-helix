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
from multiprocessing import Pool
import threading
import signal
import subprocess
import platform
import atexit
#from func_timeout import func_set_timeout, FunctionTimedOut
#import timeout_decorator
from wrapt_timeout_decorator import *
from claripy.backends.backend_smtlib_solvers import *
from angr.analyses import (
    VariableRecoveryFast,
    CallingConventionAnalysis,
    CompleteCallingConventionsAnalysis,
    CFGFast,
    Decompiler,
)
import pickle

foreverloop = True

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


avoid_function_file = 'avoid_function_list.txt'
compiler = "/home/muqi/llvm-3.8/llvm-src/tool/clang/cfe-3.8.0.src/build/bin/clang"

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
        try:
            fin = open( filepath_function_decompiled_c,'r')
            originalc_linelist = fin.readlines()
            fin.close()
        except:
            continue
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
def angr_running_pointer(arg1,arg2,angr_project,pcfg_input,filename):

    filepath_originalclang = arg1
    required_function = arg2
    log_filepath='/tmp/angr_'+filename +'_'+ required_function +'.txt'
    p = angr_project
    required_address = 0
    try :
        required_address = p.loader.find_symbol(required_function).rebased_addr
    except:
        pass
    if "FUN_" in required_function and required_address == 0:
        required_address = int(re.search("FUN_(.+?)_",required_function+"_").group(1),16)

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
            #if node.addr >= required_address:
            print("BasicBlock_cfg:["+str(hex(node.addr))+" -> "+ str(hex(node.addr+node.size))+"]", file=muqi_file)

    #p = angr.Project(filepath_originalclang)
    #p.factory.entry_state().block().vex.pp()
    args = []
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
    #print(function_args_string)
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
    #state.add_log_path(log_filepath)
    
    '''
    simgr = p.factory.simulation_manager(state)
    simgr.use_technique(angr.exploration_techniques.LoopSeer(cfg=cfg, functions='main', bound=None))
    simgr.run()
    '''
    
    #'''
    for function in p.kb.functions:
        func_name = pcfg_input.functions.get(function).name
        if func_name == required_function :
            #get required_function's jumpout edges
            sm.input_jumpout_edge(list(pcfg_input._get_jumpout_targets(pcfg_input.functions.get(function))))
    
    abort_address = []
    for function in p.kb.functions:
       func_name = pcfg_input.functions.get(function).name
       if func_name == "abort" :
          #print(pcfg_input.functions.get(function))
          abort_address.append(pcfg_input.functions.get(function).addr)

    sm.input_abort_edge(abort_address)

            #sm.input_jumpout_edge(list(pcfg_input._get_jumpout_targets(pcfg_input.functions.get(function))))
    #'''
    try:
        print("working on " +filepath_originalclang + " function:" + required_function + "\n")
        with open(log_file, "a") as myfile:
            myfile.write("working on" + filepath_originalclang + " function:" + required_function + "\n")
        #sm.explore(cfg=pcfg)
        #'''
        if foreverloop == False:
            sm.use_technique(angr.exploration_techniques.LoopSeer(cfg=pcfg_input, functions=[required_function],bound=2,use_header = True))
        #'''
        #sm.use_technique(angr.exploration_techniques.LoopSeer(cfg=pcfg_input, functions=[required_function],bound=1))
        
        sm.run()
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

def main_each_function_klee(i,function_name_list,filename,filepath_originalclang):

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

        '''
        if os.path.isfile(filepath_prompt_model_on_function) :
            pass
        '''
        try:
            fopen = open (filepath_log_klee,'r')
            fopenlines = fopen.read().splitlines()
            last_line = fopenlines[-1]
        except:
            last_line = "NONE"


        if 'terminating state' in last_line :
            pass
        else:
            os.system("rm /tmp/klee_"+filename+"_"+function_name[:-1] +"_test.txt")
            f = open(filepath_prompt_model_on_function, "w")
            f.write("global settings:\ndata models:\nfunction models:\nlifecycle model:\n    entry-point "+ function_name.replace(".","_"))
            #f.write("global settings: array size 0;\ndata models:(0 = w) where w is argsize "+function_name+" arg 0;\nfunction models:\nlifecycle model:\n    entry-point "+ function_name)
            f.close()
            if foreverloop == False:
               print("\ntimeout 30s /home/muqi/PROMPT_loop_bound/build/bin/klee  -prose-api-model="+filepath_prompt_model_on_function+ "  --loop-bound=2  --search=bfs --solver-backend=z3 --posix-runtime " + filepath_generatedbc + ' 1> '+ filepath_log_klee +' 2> '+ filepath_log_klee_error)
            else:
               print("\ntimeout 30s /home/muqi/PROMPT/build/bin/klee  -prose-api-model="+filepath_prompt_model_on_function+ " --search=bfs --solver-backend=z3 --posix-runtime " + filepath_generatedbc + " > "+ filepath_log_klee + " 2> "+ filepath_log_klee_error)  
            #'''
            #os.system("timeout 30s /home/friends/muqi/PROMPT/build2/bin/klee  -prose-api-model="+filepath_prompt_model_on_function+ " --search=bfs --solver-backend=z3 --posix-runtime " + filepath_generatedbc + " > "+ filepath_log_klee + ' 2> '+ filepath_log_klee_error)
            if foreverloop == False:
               run_cmd("/home/muqi/PROMPT_loop_bound/build/bin/klee  -prose-api-model="+filepath_prompt_model_on_function+ "  --loop-bound=2  --search=bfs --solver-backend=z3 --posix-runtime " + filepath_generatedbc + ' 1> '+ filepath_log_klee +' 2> '+ filepath_log_klee_error,30)
            else:
               run_cmd("/home/muqi/PROMPT/build/bin/klee  -prose-api-model="+filepath_prompt_model_on_function+ "   --search=bfs --solver-backend=z3 --posix-runtime " + filepath_generatedbc + ' 1> '+ filepath_log_klee +' 2> '+ filepath_log_klee_error,30)

#@func_set_timeout(120)
#@timeout_decorator.timeout(30, use_signals=False)
@timeout(60, use_signals=False)
def main_each_function_angr(i,function_name_list,filename,pcfg_angr,angr_project,filepath_originalclang):

    angr_work = True
    klee_work = True
    angr_log_work = True
    klee_log_work = True
    function_name = function_name_list[i]
    filepath_generatedbc = os.path.join(directname_generatedbc, filename+"_"+function_name[:-1]+".bc")
    
    filepath_functionc = os.path.join(directname_folder_for_project,filename+"_folder/"+filename+"_"+function_name[:-1]+".c")

    model_function_name = "model"+filename+"_"+function_name[:-1] +".txt"
    filepath_modelprompt = os.path.join(directname_model, model_function_name)


    z3_filepath = os.path.join(directname_z3, filename+"_"+function_name[:-1]+"_z3")
    z3_filepath_unsat = os.path.join(directname_z3, filename+"_"+function_name[:-1]+"_z3_unsat")
    angr_log_filepath = '/tmp/angr_'+filename +'_'+ function_name[:-1] +'.txt'
    
    if os.path.isfile(z3_filepath) or os.path.isfile(z3_filepath_unsat)  :
        return

    if os.path.isfile(filepath_generatedbc) and os.path.isfile(filepath_modelprompt) :
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
        

        '''
        try:
            print(filepath_functionc)
            f = open(filepath_functionc, 'r')
            functionc_lines = f.readlines()
            f.close()
            
            
            if 'return;' in functionc_lines[-4] and ('void' in functionc_lines[-8] or 'void' in functionc_lines[-9]):
                klee_work = False
                f = open(angrlog_file, "a")
                f.write(filename+": "+function_name + " is wrong!  wrapperfunction\n")
                f.close()
            
        except:
            f = open(angrlog_file, "a")
            f.write(filename+": "+function_name + " is wrong!  cannotopen source code?\n")
            f.close()
            angr_work = False
        '''

        if klee_work == True:
            #angr_running_pointer(filepath_originalclang,function_name[:-1],angr_project,pcfg_angr,filename)
            try:
                '''
                print("before angr_running_pointer")
                angr_running_pointer(filepath_originalclang,function_name[:-1],angr_project,pcfg_angr,filename)
                print("after angr_running_pointer")
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
                if "sub_" in required_function and required_address == 0:
                    required_address = int(re.search("sub_(.+?)_",required_function+"_").group(1),16)
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

        print("finished angr running pointer\n")
        print(klee_work)
        print(angr_work)
                
        #'''
        #start analyzing
        if klee_work == True and angr_work == True:
            '''
            #generate angr result
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
            '''
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
            #analyze_results.analyze_results(i,filename,function_name)
            #'''
            if angr_log_work == True:
                try: 
                    analyze_results.analyze_results(i,filename,function_name)
                except:
                    klee_log_work = False 
                    f = open(kleelog_file, "a")
                    f.write(filename+": "+function_name + " is wrong during z3 analyzing!\n")
                    f.close()
            #'''
            print("both work")
            print(filename+": "+function_name)
            if klee_log_work == True and angr_log_work == True:
                f = open(bothwork_file, "a")
                f.write(filename+": "+function_name + " worked !\n")
                f.close()

def automatic_compilation(code,filepath_individual_function,func_name,filepath_individual_function_bc,filepath_individual_function_log):
    
    #'''
    with open(filepath_individual_function, "w") as file:
        file.write("#include <stdio.h>\n #include <stdbool.h>\n #include <stdint.h>\n")
        file.write("typedef unsigned int    BOT;\n")
        file.write("typedef unsigned int    uint;\n")
        file.write("typedef unsigned long    ulong;\n")
        file.write(code)
        if "main" not in func_name[0:4]:
            file.write("\nint main(int param_1, const char *param_2[]){}\n")
        file.close()
    #'''
    #return
    flog = open (filepath_individual_function_log,'w')
    flog.write("first time")
    flog.close()
    
    flog = open (filepath_individual_function_log,'r')
    loglist = flog.readlines()
    flog.close()
    max_iteration = 3

    all_declared_global_name_list = []
    #os.system(compiler + " -emit-llvm -O0  -c -Wl,--demangle -Wno-everything " + filepath_individual_function + " -o " + filepath_individual_function_bc +"  2> " + filepath_individual_function_log)
    #return
    while len(loglist) != 0 and max_iteration > 0:
        max_iteration -= 1
        declare_global_name_list = []
        change_to_array = []
        os.system(compiler + " -emit-llvm -O0  -c -Wl,--demangle -Wno-everything " + filepath_individual_function + " -o " + filepath_individual_function_bc +"  2> " + filepath_individual_function_log)

        #check the error from compilation of modified code
        flog = open (filepath_individual_function_log,'r')
        loglist = flog.readlines()
        flog.close()

        #find undeclared identifier error
        i = 0
        while i < len(loglist) :
            if 'use of undeclared identifier' in loglist[i] :
                global_variable_name = re.search("use of undeclared identifier \'(.+?)\'",loglist[i]).group(1)
                declare_global_name_list.append(global_variable_name)
            if 'error: member reference base type \'int\' is not a structure or union' in loglist[i] and '._' in loglist[i+1]:
                change_to_array.append(loglist[i+1][:-1].replace(" ","").replace("="," = "))
            i += 1

         #get content of original modified file
        fin = open(filepath_individual_function,'r')
        modified_list = fin.readlines()
        fin.close()

        #we first write the typedef undefined4, etc        then declare all global variables,
        fout = open(filepath_individual_function,'w')
        declare_global_name_list = list(set(declare_global_name_list))

        lengthof_modfied_head_before_global = 6
        #print(filepath_individual_function)
        #print(modified_list)
        for i in range(lengthof_modfied_head_before_global) :
            fout.write(modified_list[i])


        for i in range(len(declare_global_name_list)):
            fout.write("int " + declare_global_name_list[i] + "; //add global variable by muqi\n")

        all_declared_global_name_list.extend(declare_global_name_list)

        #wrote the remaining cotent to file
        i = lengthof_modfied_head_before_global
        #print(change_to_array)
        while i < len(modified_list) :
            if "<8>" in modified_list[i]:
                modified_list[i] = modified_list[i].replace("<8>" ,"")
            if "<16>" in modified_list[i]:
                modified_list[i] = modified_list[i].replace("<16>" ,"")
            if "add global variable by muqi" in modified_list[i]:
                change_global_name_to_pointer = False
                declare_global_name = re.search("int (.+?); //add global variable by muqi\n",modified_list[i]).group(1)
                for j in range(len(change_to_array)):
                    if declare_global_name in change_to_array[j] :
                        change_global_name_to_pointer = True
                if change_global_name_to_pointer == True:
                    #print(declare_global_name)
                    modified_list[i] ="int " + declare_global_name + "[100]; //add global variable by muqi\n"

            fout.write(modified_list[i])
            i += 1
        fout.close()

@timeout(900, use_signals=False)
def decompile_test(pcfg_angr,function,angr_project):
    #out =  angr_project.analyses.Decompiler(pcfg_angr.kb.functions[function],rules_txt="",flavor='pseudocode', cfg=pcfg_angr.model, optimization_passes=angr.analyses.decompiler.optimization_passes.get_default_optimization_passes(angr_project.arch, angr_project.simos.name))
    out =  angr_project.analyses.Decompiler(pcfg_angr.kb.functions[function],flavor='pseudocode', cfg=pcfg_angr.model, optimization_passes=angr.analyses.decompiler.optimization_passes.get_default_optimization_passes(angr_project.arch, angr_project.simos.name))
def main_each_program(filename):

    print("in main_each_program")
    print(filename)

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

    #generate decompiled code, function_address in decompiled code, function name in decompiled code
    filepath_generated_function_name= os.path.join(directname_function_name,filename_clang)
    

    '''
    filepath_cfg = os.path.join(directname_cfg,filename)
    if os.path.isfile(filepath_cfg) :
        with open(filepath_cfg, "rb") as f:
            print("Inside open cfg")
            angr_project, pcfg_angr = pickle.load(f)
    else:
        try:
            print("start angr project")
            angr_project = angr.Project(filepath_originalclang, auto_load_libs=False, load_debug_info=True)
            #pcfg_angr = angr_project.analyses.CFG(normalize=True)
            #pcfg_angr = angr_project.analyses.CFGFast(normalize = True)
            pcfg_angr = angr_project.analyses[CFGFast].prep()(normalize=True, data_references=True)
            print("end angr project")
        except:
            f = open(angrlog_file, "a")
            f.write(filename+":  is wrong during cfg analyzing!\n")
            f.close()
            return

        pickledumpfile = open(filepath_cfg, "wb")
        print("Inside storing cfg")
        pickle.dump((angr_project,pcfg_angr), pickledumpfile)
        pickledumpfile.close()
    angr_project.analyses[angr.analyses.CompleteCallingConventionsAnalysis].prep()(recover_variables=True)
    return
    
    angr_project = angr.Project(filepath_originalclang, auto_load_libs=False, load_debug_info=True)
    pcfg_angr = angr_project.analyses[CFGFast].prep()(normalize=True, data_references=True)
    angr_project.analyses[angr.analyses.CompleteCallingConventionsAnalysis].prep()(recover_variables=True)
    

    angr_project = angr.Project(filepath_originalclang, auto_load_libs=False, load_debug_info=True)
    pcfg_angr = angr_project.analyses[CFGFast].prep()(normalize=True, data_references=True)

    angr_project.analyses[angr.analyses.CompleteCallingConventionsAnalysis].prep()(recover_variables=True)
    '''
    try:

        angr_project = angr.Project(filepath_originalclang, auto_load_libs=False, load_debug_info=True)
        pcfg_angr = angr_project.analyses[CFGFast].prep()(normalize=True, data_references=True)

        angr_project.analyses[angr.analyses.CompleteCallingConventionsAnalysis].prep()(recover_variables=True,analyze_callsites=True)
    except:
        f = open(angrlog_file, "a")
        f.write(filename+":  is wrong during cfg analyzing!\n")
        f.close()
        return 
    #'''
    #'''    
    #write decompiled code 
    print("finish angr project")
    print(filename)
    #generate function_folder
    function_folder_name = filename+ "_folder"
    filepath_folder_for_project = os.path.join(directname_folder_for_project,function_folder_name)
    filepath_folder_for_project_log = os.path.join(directname_folder_for_log,function_folder_name)
    os.system("mkdir "+filepath_folder_for_project)
    os.system("mkdir "+filepath_folder_for_project_log)
    #return
    #'''
    file_function_name = open(filepath_generated_function_name, "w") 
    
    #for function in pcfg_angr.functions.values():
    for function in angr_project.kb.functions:
        if not angr_project.kb.functions[function].is_plt and not angr_project.kb.functions[function].is_simprocedure and not angr_project.kb.functions[function].alignment:
            func_name = pcfg_angr.functions.get(function).name
            #if "sub_" in func_name:
            #    continue
            func_addr = function
            filepath_individual_function = os.path.join(filepath_folder_for_project,filename+"_"+func_name+".c")
            filepath_individual_function_log = os.path.join(filepath_folder_for_project_log,filename+"_"+func_name+".txt")
            filepath_individual_function_bc = os.path.join(directname_generatedbc,filename+"_"+func_name+".bc")
            
            #decompile_test(pcfg_angr,function,angr_project)
            try:
                decompile_test(pcfg_angr,function,angr_project)
            except:
                f = open(angrlog_file, "a")
                f.write(filename+":  " + func_name+" is wrong during decompiler analyzing!\n")
                f.close()
                continue
            try:
                #dec = angr_project.analyses.Decompiler(pcfg_angr.kb.functions[function],rules_txt="",flavor='pseudocode', cfg=pcfg_angr.model, optimization_passes=angr.analyses.decompiler.optimization_passes.get_default_optimization_passes(angr_project.arch, angr_project.simos.name))
                dec = angr_project.analyses.Decompiler(pcfg_angr.kb.functions[function],flavor='pseudocode', cfg=pcfg_angr.model, optimization_passes=angr.analyses.decompiler.optimization_passes.get_default_optimization_passes(angr_project.arch, angr_project.simos.name))
            except:
                f = open(angrlog_file, "a")
                f.write(filename+":  " + func_name+" is wrong during decompiler analyzing!\n")
                f.close()
                continue 
            code = ""
            
            for node in pcfg_angr.kb.functions[function].transition_graph.nodes():
                if isinstance(node, angr.knowledge_plugins.functions.Function):
                    if node.prototype:
                        code +=  f"{node.prototype.c_repr(name=node.name)};\n"
            # externs
            if dec.codegen is not None :
                code += "\n"
                code += dec.codegen.text
                file_function_name.write(func_name+"\n")
                
                with open(filepath_individual_function, "w") as file:
                    file.write("#include <stdio.h>\n #include <stdbool.h>\n #include <stdint.h>\n")
                    file.write("typedef unsigned int    BOT;\n")
                    file.write("typedef unsigned int    uint;\n")
                    file.write("typedef unsigned long    ulong;\n")
                    file.write(code)
                    if "main" not in func_name[0:4]:
                        file.write("\nint main(int param_1, const char *param_2[]){}\n")
                    file.close()
                
                #os.system(compiler + " -emit-llvm -O0  -c -Wl,--demangle -Wno-everything " + filepath_individual_function + " -o " + filepath_individual_function_bc +"  2> " + filepath_individual_function_log)
                
                print("before automatic compilation")
                automatic_compilation(code,filepath_individual_function,func_name,filepath_individual_function_bc,filepath_individual_function_log)
                print("after automatic compilation")
    file_function_name.close()
    #'''
    return 
    #'''
    try:
        function_filename_file = open(filepath_generated_function_name, 'r')
        function_name_list = function_filename_file.readlines()
        function_filename_file.close()
    except:
        return
    
    print("finish recompiler")
    print(filename)

    for i in range(len(function_name_list)):
        main_each_function_klee(i,function_name_list,filename,filepath_originalclang)
    
    print(function_name_list)
    
    
    print("before find_functionargs")
    find_functionargs(filename_c)
    print("after find_functionargs")
    
    print(function_name_list)
    for i in range(len(function_name_list)):        
        try:
            print(i)
            print(function_name_list[i])
            main_each_function_angr(i,function_name_list,filename,pcfg_angr,angr_project,filepath_originalclang)
            print(i)
            print("111")
        except :
                pass
        
    print(filename)
    print("finished")
    

def z3_each_file(filename):
    filepath_z3 = os.path.join(directname_z3,filename)
    filepath_diff = os.path.join(directname_diff,filename)
    run_cmd("z3 "+filepath_z3+" > "+filepath_diff, 30)

def main():
    #'''
    os.system("rm "+ angrlog_file)
    os.system("rm "+ kleelog_file)
    os.system("rm "+ bothwork_file)
    os.system("rm log_klee.txt")
    os.system("rm -r ./test_muqi/generatedbc/klee-out*")
    #os.system("rm -r ./test_muqi/generatedbc/*")
    i = 0
    filenames = []
   
    
    pool = Pool()
    pool.map(main_each_program, os.listdir(directname_originalclang)) 
    j = 0
    '''

    for filename in os.listdir(directname_originalclang):
        main_each_program(filename)
    pool = Pool()
    pool.map(z3_each_file, os.listdir(directname_z3))
    '''
    #os.system("clear")
    #os.system("cat "+ directname_diff+"/*")

if __name__ == "__main__":
    main()
