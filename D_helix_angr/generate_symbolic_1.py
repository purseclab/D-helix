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

directname_originalclang = "./test_muqi/originalclang"
directname_generated_whole_c = "./test_muqi/generated_whole_c"
directname_folder_for_project="./test_muqi/generated_function_c/project_folder"
directname_folder_for_log = "./test_muqi/generated_function_c/log_for_compile"
directname_generatedbc = "./test_muqi/generatedbc"
directname_generatedll = "./test_muqi/generatedll"
directname_generatedklee = "./test_muqi/generatedklee"
directname_model = "./test_muqi/model_prompt"

directname_diff = "./test_muqi/diff"
directname_z3 = "./test_muqi/z3"
directname_log = "./test_muqi/log"

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

log_compile = "./log_compile"
log_file = 'angrlog_pcode'
'''
ghidra_address = "/home/muqi/decompile_tool/ghidra/ghidra/build/dist/ghidra_last/ghidra_10.0_DEV/support/analyzeHeadless "
ghidra_repo_address = "/home/muqi/pcode_test/code_A_calls_B/ghidra_project.bak/ ghidra_project.gpr "
ghidra_decompiled_java_script = "/home/muqi/ghidra_scripts/Decompile.java "
ghidra_get_function_name_java_script = "/home/muqi/ghidra_scripts/List_functions_name.py "
ghidra_get_function_address_java_script = "/home/muqi/ghidra_scripts/List_functions_address.py  "
compiler = "/media/muqi/more/llvm-3.8/llvm-src/tool/clang/cfe-3.8.0.src/build/bin/clang"
'''

ghidra_address = "/home/friends/muqi/ghidra/ghidra/build/dist/ghidra_last/ghidra_10.0_DEV/support/analyzeHeadless "
ghidra_repo_address = "/home/friends/ muqi_ghidra2.gpr " #notice that there is a space between path and name of project
ghidra_decompiled_java_script1 = "/home/friends/muqi/ghidra_scripts/ "
ghidra_decompiled_java_script2 = "Decompile.java "
ghidra_get_function_name_java_script = "//home/friends/muqi/ghidra_scripts/List_functions_name.py "
ghidra_get_function_address_java_script = "/home/friends/muqi/ghidra_scripts/List_functions_address.py  "


compiler = "/home/friends/muqi/llvm-3.8/llvm-src/tool/clang/cfe-3.8.0.src/build/bin/clang"

avoid_function_list=[
    "_init","free","abort","strtoimax","__errno_location","strncmp","_exit","__fpending","strcpy","puts","reallocarray","textdomain","fclose","bindtextdomain","__ctype_get_mb_cur_max",
    "strlen","__stack_chk_fail","getopt_long","mbrtowc","gettext","strchr","printf","strrchr","lseek","memset","memcmp","fputs_unlocked","ferror_unlocked","calloc","strcmp","fputc_unlocked",
    "fprintf","strtol","memcpy","kill","fileno","malloc","fflush","nl_langinfo","__freading","strsignal","setlocale","error","fseeko","__libc_current_sigrtmin","sprintf","exit","fwrite","__libc_current_sigrtmax",
    "mbsinit","iswprint","__ctype_b_loc","__cxa_finalize","_start","deregister_tm_clones","register_tm_clones","__do_global_dtors_aux","frame_dummy","__libc_csu_init","__libc_csu_fini","atexit","_fini",
    "fdopen","fopen","stpcpy","setlocale_null_unlocked_z3","memchr","rawmemchr","strspn","xrealloc","mempcpy","strtoumax","strpbrk","gl_scratch_buffer_dupfree", "memrchr","lcm","localeconv","strftime",
    "stpncpy","timegm","strftime","getdelim"
    ,"__snprintf_chk","chroot","__fprintf_chk","__vfprintf_chk","__assert_fail","__asprintf_chk","ioctl"," __libc_start_main","warnx","mkdir","strstr","getpid"
    ]    #this is a list of functions which are system functions

checked_function_list = ["set_char_quoting","raw_hasher","locale_charset","xmax","strcspn","freadahead","iso_week_days","mbs_align_pad","fileinfo_name_width","ino_map_insert",
"idle_string", "argv_iter_n_args","key_init","base64_encode_alloc", "fread_unlocked","tm_year_str","xstrmode","wcslen","split","replay_step_get_filename","wmemset"
"ul_pty_get_child"
]
def automatic_compilation(arg1,arg2,function_name):
    #print(arg1)
    filepath_generatedc = arg1
    filepath_generatedc_modified = filepath_generatedc.replace(".c","_modified.c")
    filepath_generatedbc = arg2
    
    fin = open(filepath_generatedc,'r')
    linelist = fin.readlines()
    fin.close()
    
    fout = open(filepath_generatedc_modified,'w')
    fout.write("#include <stdio.h>\n #include <stdbool.h>\n #include <stdint.h>\n")
    fout.write("typedef unsigned char    undefined1;\n")
    fout.write("typedef unsigned short    undefined2;\n")
    fout.write("typedef unsigned int    uint;\n")
    fout.write("typedef unsigned char    undefined1;\n")
    fout.write("typedef unsigned short    undefined2;\n")
    fout.write("typedef unsigned int    uint;\n")
    fout.write("typedef unsigned int    undefined4;\n")
    fout.write("typedef unsigned long    undefined8;\n")
    fout.write("typedef unsigned long    ulong;\n")
    fout.write("typedef unsigned char   undefined;\n")
    fout.write("typedef int code;\n")
    fout.write("typedef float   float10;\n")
    
    i = 0
    while i < len(linelist) :
        fout.write(linelist[i])
        i+=1
        
    if "main" not in function_name:
        fout.write("\nint main(int param_1, const char *param_2[]){}\n")
    fout.close()
    
    flog = open (log_compile,'w')
    flog.write("first time")
    flog.close()
    
    flog = open (log_compile,'r')
    loglist = flog.readlines()
    flog.close()
    
    
    max_iteration = 10
    #'''
    #print (compiler + " -emit-llvm -O0  -c -Wl,--demangle -Wno-everything " + filepath_generatedc_modified + " -o " + filepath_generatedbc +"  2> " + log_compile) 
    all_declared_global_name_list = []
    while len(loglist) != 0 and max_iteration > 0:
        max_iteration -= 1
        declare_global_name_list = []
        change_to_array = []
        #try compile the modified code
        #print (compiler + " -emit-llvm -O0  -c -Wl,--demangle -Wno-everything " + filepath_generatedc_modified + " -o " + filepath_generatedbc +"  2> " + log_compile) 
        os.system(compiler + " -emit-llvm -O0  -c -Wl,--demangle -Wno-everything " + filepath_generatedc_modified + " -o " + filepath_generatedbc +"  2> " + log_compile)
        
        #check the error from compilation of modified code
        flog = open (log_compile,'r')
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
        fin = open(filepath_generatedc_modified,'r')
        modified_list = fin.readlines()
        fin.close()
        
        #declare all global variables first
        fout = open(filepath_generatedc_modified,'w')
        declare_global_name_list = list(set(declare_global_name_list))
        '''
        if change_to_array :
            print(declare_global_name_list)
            print(change_to_array)
        '''
        for i in range(len(declare_global_name_list)):
            fout.write("int " + declare_global_name_list[i] + "; //add global variable by muqi\n")
        
        all_declared_global_name_list.extend(declare_global_name_list)
        
        declare_global_name_is_pointer = False
        
        #wrote the remaining cotent to file
        i = 0
        #print(change_to_array)
        while i < len(modified_list) :
            if any(ele in modified_list[i] for ele in change_to_array) :
                try: 
                    #case "x= xxx._0_8_;"
                    prefix = re.search("(.+?)\._(.+?)_(.+?)_;",modified_list[i]).group(1)
                    suffix = re.search("(.+?)\._(.+?)_(.+?)_;",modified_list[i]).group(2)
                    modified_list[i] = prefix+"["+suffix+"];"+"\n"
                    '''
                    print(prefix)
                    print(suffix)
                    print(modified_list[i] )
                    '''
                except:
                    try:
                        #case "xxx._0_8_ = x"
                        prefix = re.search("(.+?)\._(.+?)_(.+?)_ = (.+?)\n",modified_list[i]).group(1)
                        suffix = re.search("(.+?)\._(.+?)_(.+?)_ = (.+?)\n",modified_list[i]).group(2)
                        final = re.search("(.+?)\._(.+?)_(.+?)_ = (.+?)\n",modified_list[i]).group(4)
                        modified_list[i] = prefix+"["+suffix+"]="+final +"\n"
                        '''
                        print(prefix)
                        print(suffix)
                        print(final)
                        print(modified_list[i] )
                        '''
                    except:
                        print("not an array in: "+modified_list[i])
            
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
        
    #'''
    #os.system(compiler + " -emit-llvm -O0  -c -Wl,--demangle -Wno-everything " + filepath_generatedc_modified + " -o " + filepath_generatedbc +"  2> " + log_compile)
    if max_iteration <= 0 :
        raise Exception('During compilation, we reach the maximum number of trials')

dic_funcname_funcargs = {}

def seperate_function_compilation(filepath_generated_whole_c,filename_c):
    comment_struct_list = ["struct _IO_FILE {","struct _IO_marker {","struct anon_struct.conflict","union anon_union.conflict","struct Test.conflict","struct route_info.conflict"]
    direct_comment_list = ["typedef struct __mbstate_t __mbstate_t, *P__mbstate_t;","typedef struct __fsid_t __fsid_t, *P__fsid_t;","typedef enum anon_enum_32.conflict",
    "typedef struct __va_list_tag __builtin_va_list[1];","typedef struct anon_struct.conflict","typedef union anon_union.conflict","typedef unsigned char    bool;", "typedef bool _Bool;"
    ,"typedef enum enum_1434","typedef struct route_info.conflict route_info.conflict, *Proute_info.conflict", "typedef struct Test.conflict Test.conflict, *PTest.conflict","typedef void * __gnuc_va_list"]
    comment_with_double_slides = ["struct blk_zone[0] zones;","char[0] name;","ERROR=22,"]
    
    filename_whole_decompiled_c = filename_c
    filepath_whole_decompiled_c= filepath_generated_whole_c
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
        #continue
           
    #generate function_folder 
    function_folder_name = filename_whole_decompiled_c.replace(".c","") + "_folder"
    filepath_folder_for_project = os.path.join(directname_folder_for_project,function_folder_name)
    filepath_folder_for_project_log = os.path.join(directname_folder_for_log,function_folder_name)
    os.system("mkdir "+filepath_folder_for_project)
    os.system("mkdir "+filepath_folder_for_project_log)
    
    #print("after mkdir")
    filepath_basec= os.path.join(directname_generated_whole_c,filename_whole_decompiled_c.replace(".c","")+"_base.c")
    fin = open(filepath_whole_decompiled_c,'r')
    originalc_linelist = fin.readlines()
    fin.close()
    
    #generate base for each function
    comment_count = 0
    direct_comment_count = 0
    variable_count = 0
    fout = open(filepath_basec,'w')
    for i in range(len(originalc_linelist)):
        if first_function_name in originalc_linelist[i] and "{" in originalc_linelist[i+2] :
            break
        
        #comment out uselee struct 
        if any(phrase in  originalc_linelist[i] for phrase in comment_struct_list ) and "typedef" not in originalc_linelist[i] and ";" not in originalc_linelist[i]:
            fout.write ("/*\n")
            comment_count += 1
        
        if any(phrase in  originalc_linelist[i] for phrase in comment_struct_list ) and "typedef" not in originalc_linelist[i]  and ";" in originalc_linelist[i]:
            fout.write ("//")
            variable_count += 1
        
        if any(phrase in  originalc_linelist[i] for phrase in comment_with_double_slides ) :
            fout.write("//")
        
        if any(phrase in  originalc_linelist[i] for phrase in direct_comment_list ) :
            fout.write ("/*\n")
            direct_comment_count += 1
         
        #comment out FS_OFFSET
        if ")(in_FS_OFFSET + 0x28);" in originalc_linelist[i] :
            originalc_linelist[i] = "//comment in_FS_OFFSET\n"
        elif ")(in_FS_OFFSET + 0x28))" in originalc_linelist[i] :
            originalc_linelist[i] = "if (1) {\n"
        else:
            originalc_linelist[i] = originalc_linelist[i]
        fout.write(originalc_linelist[i])
        
        if comment_count > 0 and "};" in originalc_linelist[i]:
            fout.write ("*/")
            comment_count -= 1
        
        if variable_count > 0 and ";" in originalc_linelist[i]:
            variable_count -= 1
            
        if direct_comment_count > 0 and ";" in originalc_linelist[i]:
            fout.write ("*/\n")
            direct_comment_count -= 1
            

        
    fout.close()
        
    fbase = open(filepath_basec,'r')
    base_linelist = fbase.readlines()
    fbase.close()
    
    comment_count = 0
    #print("in seperate_function_compilation:")
    #print(function_name_list)
    for i in range(len(function_name_list)):
        filepath_individual_function = os.path.join(filepath_folder_for_project,filename_whole_decompiled_c.replace(".c","")+"_"+function_name_list[i]+".c")
        filepath_individual_function_bc = os.path.join(directname_generatedbc,filename_whole_decompiled_c.replace(".c","")+"_"+function_name_list[i]+".bc")
        filepath_individual_function_log = os.path.join(filepath_folder_for_project_log,filename_whole_decompiled_c.replace(".c","")+"_"+function_name_list[i]+".txt")
        fproject_function = open(filepath_individual_function,'w')
        #print(filepath_individual_function)
        #first write structure info to file
        for j in range(len(base_linelist)):
            fproject_function.write(base_linelist[j])
        
        #then we write the function info to file
        braket_count = 0
        start_function = False
        k = 0
        while k < len(originalc_linelist):
            if " " + function_name_list[i]+"(" in originalc_linelist[k]:
                #print("!!!!!!!!!code" +str(k)+" : "+originalc_linelist[k])
                function_declare_start = k
                function_declare_end = k
                while function_declare_end < len(originalc_linelist):
                    if ")" in originalc_linelist[function_declare_end] :
                        break
                    function_declare_end += 1
                
                function_declare_string = ""
                for function_iter in range(function_declare_start,function_declare_end + 1):
                    function_declare_string += originalc_linelist[function_iter].replace("\n","")
                global dic_funcname_funcargs 
                dic_funcname_funcargs[function_name_list[i]] = function_declare_string
                
                if "{" == originalc_linelist[function_declare_end+2][0] and ";" not in originalc_linelist[function_declare_end]:
                    braket_count = 1
                    start_function = True
                    temp_value = function_declare_start
                    while temp_value <= function_declare_end:
                        fproject_function.write(originalc_linelist[temp_value])
                        temp_value += 1
                    fproject_function.write(originalc_linelist[function_declare_end+1])
                    fproject_function.write(originalc_linelist[function_declare_end+2])
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
                fproject_function.write(originalc_linelist[k])
            
            if "}" in originalc_linelist[k] :
                braket_count -= 1
                
            if braket_count == 0 and start_function == True:
                break
            
            k += 1
        fproject_function.close()
        
        #print("before automatic compile")
        #finally, we try to automatically compile this file
        try:
            automatic_compilation(filepath_individual_function,filepath_individual_function_bc,function_name_list[i])
        except:
            os.system("cp "+log_compile+" "+filepath_individual_function_log) 
    


def angr_running_pointer(arg1,arg2,angr_project,pcfg_input):

    filepath_originalclang = arg1
    required_function = arg2
    p = angr_project
    required_address = p.loader.find_symbol(required_function).rebased_addr

    print(hex(required_address))

    #use cfgfast to identify the boundry of basic block
    #pcfg = p.analyses.CFGFast(normalize = True)
    pcfg = pcfg_input
    pcfg = pcfg.functions.get(required_address).transition_graph

    #write basic block info to file
    with open('/tmp/angr.txt','w') as muqi_file:
        print('Filename: ',filepath_originalclang, file=muqi_file)
        print('Function: ',required_function, file=muqi_file)

        for node in pcfg.nodes():
            if node.addr >= required_address:
                print("BasicBlock_cfg:["+str(hex(node.addr))+" -> "+ str(hex(node.addr+node.size))+"]", file=muqi_file)

    #p = angr.Project(filepath_originalclang)
    #p.factory.entry_state().block().vex.pp()
    args = []
    for i in range(20):
        args.append(claripy.BVS('angr_arg'+str(i), 8*8))

    global dic_funcname_funcargs 
    function_declare_string = dic_funcname_funcargs[required_function]
    function_args_string = re.search("\((.+?)\)", function_declare_string).group(1)
    print(function_args_string)
    function_args_list = function_args_string.split(",")
    for i in range(len(function_args_list)):
        if "*" in function_args_list[i] :
            args[i] = claripy.BVS('angr_arg'+str(i), 256*8)
            args[i] = angr.PointerWrapper(args[i])
            print("inside functionargslist")
            print("i is: "+ str(i)) 
            
    state = p.factory.call_state(required_address,args[0],args[1],args[2],args[3],args[4],args[5],args[6],args[7],args[8],args[9],args[10],add_options={angr.options.CALLLESS,angr.options.STRINGS_ANALYSIS,angr.options.ZERO_FILL_UNCONSTRAINED_MEMORY,angr.options.ZERO_FILL_UNCONSTRAINED_REGISTERS})
     
    sm = p.factory.simulation_manager(state)

    try:
        print("working on " +filepath_originalclang + " function:" + required_function + "\n")
        with open(log_file, "a") as myfile:
            myfile.write("working on" + filepath_originalclang + " function:" + required_function + "\n")
        #sm.explore(cfg=pcfg)
        sm.run()
        with open(log_file, "a") as myfile:
            myfile.write("worked\n")
    except:
        with open(log_file, "a") as myfile:
            myfile.write("not working\n")

def main():
    os.system("rm "+ angrlog_file)
    os.system("rm "+ kleelog_file)
    os.system("rm "+ bothwork_file)
    os.system("rm log_klee.txt")
    #os.system("rm -r ./test_muqi/generatedbc/klee-out*")
    os.system("rm -r ./test_muqi/generatedbc/*")
    i = 0
    filenames = []
    for filename in os.listdir(directname_originalclang):
    
        #reset dictionary
        global dic_funcname_funcargs 
        dic_funcname_funcargs = {}
        
        
        filename_c = filename + ".c"
        filename_bc = filename +".bc"
        filename_clang = filename
        filename_ll = filename+".ll"
        
        filepath_originalclang = os.path.join(directname_originalclang,filename_clang)
        
        filepath_generated_whole_c = os.path.join(directname_generated_whole_c, filename_c)
        
        filepath_generatedll = os.path.join(directname_generatedll, filename_ll)

        #generate decompiled code, function_address in decompiled code, function name in decompiled code
        filepath_generated_function_name= os.path.join(directname_function_name,filename_clang)
        filepath_generated_function_address= os.path.join(directname_function_address,filename_clang)
        print(ghidra_address+" "+ghidra_repo_address+" -import " + filepath_originalclang + " -overwrite -scriptPath " + ghidra_decompiled_java_script1 +" -postscript " + ghidra_decompiled_java_script2+" "+filepath_generated_whole_c +" ")
        continue
        #print(ghidra_address+" "+ghidra_repo_address+" -import " + filepath_originalclang + " -overwrite -postscript " + ghidra_decompiled_java_script+" "+filepath_generatedc +" ")
        #'''
        os.system(ghidra_address+" "+ghidra_repo_address+" -import " + filepath_originalclang + " -overwrite -postscript " + ghidra_get_function_name_java_script+" "+filepath_generated_function_name +" ")
        #os.system(ghidra_address+" "+ghidra_repo_address+" -import " + filepath_originalclang + " -overwrite -postscript " + ghidra_get_function_address_java_script+" "+filepath_generated_function_address +" ")
        
        os.system(ghidra_address+" "+ghidra_repo_address+" -import " + filepath_originalclang + " -overwrite -scriptPath " + ghidra_decompiled_java_script1 +" -postscript " + ghidra_decompiled_java_script2+" "+filepath_generated_whole_c +" ")
        #'''
        '''/home/friends/muqi/ghidra/ghidra/build/dist/ghidra_last/ghidra_10.0_DEV/support/analyzeHeadless  /home/friends/ muqi_ghidra2.gpr  -import ./test_muqi/originalclang/curl -overwrite -scriptPath /home/friends/muqi/ghidra_scripts/  -postscript Decompile.java  ./test_muqi/generated_whole_c/curl.c 
        '''
        print(ghidra_address+" "+ghidra_repo_address+" -import " + filepath_originalclang + " -overwrite -scriptPath " + ghidra_decompiled_java_script1 +" -postscript " + ghidra_decompiled_java_script2+" "+filepath_generated_whole_c +" ")
        #'''
        angr_project = angr.Project(filepath_originalclang, engine=angr.engines.UberEnginePcode)
        pcfg_angr = angr_project.analyses.CFGFast(normalize = True)
        #'''
        function_filename_file = open(filepath_generated_function_name, 'r')
        function_name_list = function_filename_file.readlines()
        function_filename_file.close()
        
        print("before seperate_function_compilation")
        
        seperate_function_compilation(filepath_generated_whole_c,filename_c)
        
        print("after seperate_function_compilation")
        print(function_name_list)
        #continue
        for i in range(len(function_name_list)):
            angr_work = True
            klee_work = True
            angr_log_work = True
            klee_log_work = True
            function_name = function_name_list[i]
            filepath_generatedbc = os.path.join(directname_generatedbc, filename+"_"+function_name[:-1]+".bc")
            
            if os.path.isfile(filepath_generatedbc)  :
                #run prompt for symbolic execution
                #generate model.txt for prompt for that function
                print(filepath_generatedbc)
                model_function_name = "model.txt"
                os.system("rm /tmp/klee_test.txt")

                filepath_prompt_model_on_function = os.path.join(directname_model, model_function_name)
                f = open(filepath_prompt_model_on_function, "w")
                f.write("global settings:\ndata models:\nfunction models:\nlifecycle model:\n    entry-point "+ function_name)
                f.close()
                
                print("timeout 60s /home/friends/muqi/PROMPT/build2/bin/klee -prose-api-model="+filepath_prompt_model_on_function+ " --search=bfs --solver-backend=z3 --posix-runtime " + filepath_generatedbc + " > log_klee.txt")
                
                #'''
                os.system("timeout 60s /home/friends/muqi/PROMPT/build2/bin/klee  -prose-api-model="+filepath_prompt_model_on_function+ " --search=bfs --solver-backend=z3 --posix-runtime " + filepath_generatedbc + " > log_klee.txt")
                
                try:
                    f = open( "log_klee.txt" , 'r')
                    log_lines = f.readlines()[-1]
                    f.close()
                    if 'terminating state' not in log_lines:
                        klee_work = False
                        f = open(kleelog_file, "a")
                        f.write(filename+": "+function_name + " is wrong!\n")
                        f.close()
                except:
                    klee_work = False
                    f = open(kleelog_file, "a")
                    f.write(filename+": "+function_name + " is wrong!\n")
                    f.close()
                #'''

                #run angr for symbolic execution
                
                '''
                process_angr_running = multiprocessing.Process(target=angr_running_pointer, name="angr_running_pointer", args=(filepath_originalclang,function_name[:-1],angr_project,pcfg_angr))
                #process_angr_running = multiprocessing.Process(target=angr_running, name="angr_running", args=(filepath_originalclang,function_name[:-1],angr_project,pcfg_angr))
                process_angr_running.start()
                process_angr_running.join(300)
                # If thread is active
                if process_angr_running.is_alive():
                    # Terminate foo
                    process_angr_running.terminate()
                    process_angr_running.join()
                '''
                #'''
                #'''
                try:
                    if klee_work == True:
                        process_angr_running = multiprocessing.Process(target=angr_running_pointer, name="angr_running_pointer", args=(filepath_originalclang,function_name[:-1],angr_project,pcfg_angr))
                        #process_angr_running = multiprocessing.Process(target=angr_running, name="angr_running", args=(filepath_originalclang,function_name[:-1],angr_project,pcfg_angr))
                        process_angr_running.start()
                        process_angr_running.join(300)
                        # If thread is active
                        if process_angr_running.is_alive():
                            # Terminate foo
                            process_angr_running.terminate()
                            process_angr_running.join()
                        #angr_running(filepath_originalclang,function_name[:-1],angr_project,pcfg_angr)
                        #os.system("timeout 300s python -O angr_running.py "+ filepath_originalclang +" 0 " + function_name[:-1])
                        #os.system("timeout 1200s python -O angr_running.py "+ filepath_originalclang +" 0 " + function_name[:-1])
                except:
                    f = open(angrlog_file, "a")
                    f.write(filename+": "+function_name + " is wrong!\n")
                    f.close()
                    angr_work = False
                #'''
                #'''
                #'''
                
                #'''
                #start analyzing
                if klee_work == True and angr_work == True:
                    '''
                    analyze_angr.reset_global() 
                    analyze_angr.build_basic_block()
                    analyze_angr.generate_ir_first_version()
                    analyze_angr.generate_father_block_second_version()
                    analyze_angr.generate_children_block_second_version()
                    analyze_angr.cfg_to_ir(angr_ir_third,angr_ir_third_flip)
                    analyze_angr.ir_reorder(angr_ir_third_flip)
                    '''
                    #generate angr result
                    try:
                        analyze_angr.reset_global()
                        analyze_angr.build_basic_block()
                        analyze_angr.generate_ir_first_version()
                        analyze_angr.generate_father_block_second_version()
                        analyze_angr.generate_children_block_second_version()
                        analyze_angr.cfg_to_ir(angr_ir_third,angr_ir_third_flip)
                        analyze_angr.ir_reorder(angr_ir_third_flip)
                    except:
                        angr_log_work = False
                        f = open(angrlog_file, "a")
                        f.write(filename+": "+function_name + " is wrong during analyzing!\n")
                        f.close()
                    
                    #generate klee result
                    #analyze_results.analyze_results(i,filename_c,function_name)
                    if angr_log_work == True:
                        try: 
                            analyze_results.analyze_results(i,filename_c,function_name)
                        except:
                            klee_log_work = False 
                            f = open(kleelog_file, "a")
                            f.write(filename+": "+function_name + " is wrong during analyzing!\n")
                            f.close()
                    
                    
                    if klee_log_work == True and angr_log_work == True:
                        f = open(bothwork_file, "a")
                        f.write(filename+": "+function_name + " worked !\n")
                        f.close()
                '''
                if "main" in function_name :
                    break
                '''
        
        
        i = i + 1
        filenames.append(filename_c)
        
    j = 0
    #os.system("clear")
    #os.system("cat "+ directname_diff+"/*")

if __name__ == "__main__":
    main()
