
import os
import sys
import math
import time
from time import sleep
import numpy as np
import re
import analyze_results
import analyze_angr
#import angr
import traceback
'''
import claripy
import angr
'''
import sys
import multiprocessing
import time
from multiprocessing import Pool
import threading
import signal
import subprocess
import platform
import atexit
'''
import timeout_decorator
from claripy.backends.backend_smtlib_solvers import *
from angr.analyses import (
    VariableRecoveryFast,
    CallingConventionAnalysis,
    CompleteCallingConventionsAnalysis,
    CFGFast,
    Decompiler,
)
'''
directfuncname = "./function_name2/"
directoriginal = "./test_muqi/originalclang"
transferfuncname = "/home/muqi/pthread_Angr_Prompt_after_abort_sibling/function_name/"
transfertestmuqi = "/home/muqi/pthread_Angr_Prompt_after_abort_sibling/test_muqi/"
directoriginclang = "./test_muqi/originalclang/"
transferfunccount = "/home/muqi/pthread_Angr_Prompt_after_abort_sibling/function_count/"

'''
terminate_count 
segment 
function_not_found 
abort 
wrapper 
not_terminate_count
'''
def main_each_program(filename):
    count = 0
    terminate_count = 0
    wrapper = 0
    not_terminate_count = 0
    function_not_found = 0
    segment = 0
    multiple_symbol = 0
    abort = 0
    switch = 0
    terminted_functions =["NONE"]
    fopen = open (directfuncname+filename,'r')
    functionnames = fopen.readlines()
    fopen.close()

    fopen_count =open (transferfunccount+filename,'w')
    fopen_write = open (transferfuncname+filename,'w')
    filepathcfolder = transfertestmuqi+"generated_function_c/project_folder/" +filename+"_folder"
    os.system("mkdir "+ filepathcfolder)
    os.system("cp "+ "./test_muqi/generated_html/" +filename+".html "+transfertestmuqi+"generated_html/")
    filepath_originalclang = directoriginclang + filename
    print(filepath_originalclang)
    
    '''
    try:
        angr_project = angr.Project(filepath_originalclang, auto_load_libs=False, load_debug_info=True)
        pcfg_angr = angr_project.analyses[CFGFast].prep()(normalize=True, data_references=True)
        #print("finish analysis of angr")
    except:
        print("error")
        return
    '''
    for i in range(len(functionnames)):
        function_name = functionnames[i][:-1]
        filepathbc = "./test_muqi/generatedbc/"+filename+"_"+function_name+".bc"
        filepathc = "./test_muqi/generated_function_c/project_folder/"+filename+"_folder/"+filename+"_"+function_name+".c"
        filepath_modeified_c = "./test_muqi/generated_function_c/project_folder/"+filename+"_folder/"+filename+"_"+function_name+"_modified.c"
        filepathz3 = "./test_muqi/z3/"+filename+"_"+function_name+"_z3"
        filepathz3_unsat = "./test_muqi/z3/"+filename+"_"+function_name+"_z3_unsat"
        if os.path.isfile(filepathbc) == True:
            if os.path.isfile(filepathz3) == True or os.path.isfile(filepathz3_unsat) == True :
                '''
                print("should not write following")
                print(filepathbc)
                print(filepathz3_unsat)
                print(filepathz3)
                '''
                pass
            else:
                count += 1
                '''
                wrapper_function = False
                for function in angr_project.kb.functions:
                    if angr_project.kb.functions[function].is_plt:
                        if pcfg_angr.functions.get(function).name == function_name :
                            #print("wrapper")
                            #print(function_name)
                            wrapper += 1
                            wrapper_function = True
                            break
                if wrapper_function == True:
                    continue
                '''
                try:
                    fopen_modefified_c = open(filepath_modeified_c, "r")
                    functionc_lines = fopen_modefified_c.readlines()
                    fopen_modefified_c.close()
                except:
                    print("fopen_modefified_c  not found")
                    continue
            
                for j in range(len(functionc_lines)):
                    if 'abort' in functionc_lines[j]:
                        abort += 1
                        break
                    if 'switch' in functionc_lines[j]:
                        switch += 1
                        break

                try:
                    fopen_klee = open ("./test_muqi/log_klee/log_klee"+filename+"_"+function_name+"_error.txt", "r")
                    lines = fopen_klee.read().splitlines()
                    fopen_klee.close()
                except:
                    continue
                try:
                    last_line = lines[-1]
                except:
                    last_line = ""
                if 'KLEE: done:' in last_line :
                    terminate_count += 1
                    print("klee done")
                    print(filename+"_"+function_name)
                    terminted_functions.append(filename+"_"+function_name)
                elif 'KLEE: ERROR:' in last_line :
                    function_not_found += 1
                    continue
                elif 'error: Linking globals named' in last_line :
                    multiple_symbol +=1
                    continue
                elif 'core dumped' in last_line :
                    segment += 1
                    continue
                else:
                    not_terminate_count += 1
                    #print(filename+"_"+function_name)

                #'''
                fopen_write.write(functionnames[i])
                os.system("cp "+ filepathbc +" "+ transfertestmuqi+"generatedbc/")
                os.system("cp "+ filepathc +" "+ filepathcfolder+"/")
                os.system("cp "+ filepath_modeified_c +" "+ filepathcfolder+"/")
                #'''
    #'''
    fopen_write.close()
    fopen_count.write(str(count)+"\n")
    fopen_count.write(str(terminate_count)+"\n")
    fopen_count.write(str(wrapper)+"\n")
    fopen_count.write(str(not_terminate_count)+"\n")
    fopen_count.write(str(function_not_found)+"\n")
    fopen_count.write(str(multiple_symbol)+"\n")
    fopen_count.write(str(segment)+"\n")
    fopen_count.write(str(abort)+"\n")
    fopen_count.write(str(switch)+"\n")
    fopen_count.write(terminted_functions[-1])
    fopen_count.close()
    #'''
def main():
    print("start of main")
    global terminate_count
    global wrapper
    global not_terminate_count
    global function_not_found
    global segment
    global abort

    terminate_count = 0
    wrapper = 0
    not_terminate_count = 0
    function_not_found = 0
    segment = 0
    abort = 0

    print("start of program")
    #'''
    pool = Pool()
    pool.map(main_each_program, os.listdir(directfuncname)) 
    #'''
    '''
    for filename in os.listdir(directfuncname):
        main_each_program(filename)
    '''
    print("finally")
    print(terminate_count)
    print(wrapper)
    print(not_terminate_count)
    print(function_not_found)

if __name__ == "__main__":
    main()

