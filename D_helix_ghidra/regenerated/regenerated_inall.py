import os
import sys
import math
import time
from time import sleep
import numpy as np
import re
import sys
import multiprocessing
import time
import threading
import angr
import analyze_results
import analyze_angr
import traceback
import claripy
from multiprocessing import Pool
import threading
import signal
import subprocess
import platform
import atexit
import time
from func_timeout import func_set_timeout, FunctionTimedOut


ghidra_decompiled_java_script_inall = "/home/muqi/ghidra_projects/"
ghidra_decompiled_java_script_base = "/home/muqi/ghidra_script_inall/ghidra_scripts/"

ghidra_decompiled_java_script2 = "Decompile.java"
ghidra_decompiled_java_script3 = "Decompile_pre.java"
ghidra_decompiled_java_script4 = "Decompile_pre_base.java"
ghidra_decompiled_java_script5 = "Decompilehtml.java "

directname_function_name_original = "./function_name_original"
directname_function_name_original_individual = "./function_name_original_individual"
directname_originalclang = "./test_muqi/originalclang"

archive_list_address = "/home/muqi/ghidra_log/archive_list.txt"
rules = "./test_muqi_base/rules"

output_diff = "./diff_result"
directname_regenerated_correct_result = "./correct_result"


#ghidra_address = "/home/muqi/ghidra/build/dist/ghidra_last/support/analyzeHeadless "
ghidra_address = "/home/muqi/ghidra/build/dist/ghidra_modefied_rules/support/analyzeHeadless "

ghidra_repo_address_folder = "/home/muqi/ghidra_projects/ "
ghidra_get_function_name_java_script = "/home/muqi/ghidra_scripts/List_functions_name.py "


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
    ]    #this is a list of functions which are system functions

checked_function_list = ["set_char_quoting","raw_hasher","locale_charset","xmax","strcspn","freadahead","iso_week_days","mbs_align_pad","fileinfo_name_width","ino_map_insert",
"idle_string", "argv_iter_n_args","key_init","base64_encode_alloc", "fread_unlocked","tm_year_str","xstrmode","wcslen","split","replay_step_get_filename","wmemset"
"ul_pty_get_child"
]

def ghidra_special_function_issue(fout):
    type_dictionary = {1:"unsigned char",2:"unsigned short",4:"unsigned int", 8: "unsigned long long",16 : "__uint128_t "}
    
    ##concat 11, 22, 44, 88 
    concat_list= [1,2,4,8]
    for i in range(len(concat_list)) :
        input_type = type_dictionary[concat_list[i]]
        output_type = type_dictionary[concat_list[i]*2]
        shift_bits = concat_list[i]*8
        fout.write(output_type+" CONCAT"+str(concat_list[i])+str(concat_list[i])+"("+input_type+" input1, "+input_type+" input2){\n")
        fout.write(output_type +" concateresult = ((("+output_type+") input1) << "+ str(shift_bits)+")  + ("+input_type+")input2;\n")
        fout.write("         return concateresult;\n")
        fout.write("}\n")
    
    extend_list=[1,2,4,8,16]
    for i in range(len(extend_list)) :
        input_type = type_dictionary[extend_list[i]]
        for j in range(i, len(extend_list)):
            output_type = type_dictionary[extend_list[j]]
            fout.write(output_type+" SEXT"+str(extend_list[i])+str(extend_list[j])+"("+input_type+" input){\n ")
            fout.write("unsigned b = "+str(extend_list[i]*8) +";\n")
            fout.write(input_type +" x = input;\n")
            fout.write(output_type +" r;\n")
            fout.write(input_type +" const m = 1U << (b - 1);\n")
            fout.write("x = x & ((1U << b) - 1);\n")
            fout.write("r = (x ^ m) - m;\n")
            fout.write("return r;\n")
            fout.write("}\n")
            fout.write(output_type+" ZEXT"+str(extend_list[i])+str(extend_list[j])+"("+input_type+" input){\n ")
            fout.write(output_type+" output = (("+output_type+") (("+input_type+") input));\n")
            fout.write("return output;\n")
            fout.write("}\n")
            
    sub_list=[16,8,4,2,1]
    for i in range(len(sub_list)) :
        input_type = type_dictionary[sub_list[i]]
        for j in range(i, len(sub_list)):
            output_type = type_dictionary[sub_list[j]]
            fout.write(output_type+" SUB"+str(sub_list[i])+str(sub_list[j])+" ("+input_type+" input, int index){\n")
            fout.write(output_type+" result = (input >> (8 * index));\n")
            fout.write("return result;\n")
            fout.write("}\n")


def automatic_compilation(arg1,arg2,function_name,filepath_individual_function_log,generated_html_filepath):
    #print(arg1)
    filepath_generatedc = arg1
    filepath_generatedc_modified = filepath_generatedc.replace(".c","_modified.c")
    filepath_generatedbc = arg2
    
    fin = open(filepath_generatedc,'r')
    linelist = fin.readlines()
    fin.close()
    
    fhtml = open (generated_html_filepath,'r')
    htmllinelist = fhtml.readlines()
    fhtml.close()
    
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
    fout.write("typedef unsigned short    ushort;\n")
    fout.write("typedef unsigned char    uchar;\n")
    fout.write("typedef unsigned char   undefined;\n")
    fout.write("typedef int code;\n")
    fout.write("typedef float   float10;\n")
    ghidra_special_function_issue(fout)

    i = 0
    while i < len(linelist) :
        fout.write(linelist[i])
        i+=1
    if "main" not in function_name[0:4]:
        fout.write("\nint main(int param_1, const char *param_2[]){}\n")
    fout.close()
    
    flog = open (filepath_individual_function_log,'w')
    flog.write("first time")
    flog.close()
    
    flog = open (filepath_individual_function_log,'r')
    loglist = flog.readlines()
    flog.close()
    
    
    max_iteration = 10
    #'''
    #print (compiler + " -emit-llvm -O0  -c -Wl,--demangle -Wno-everything " + filepath_generatedc_modified + " -o " + filepath_generatedbc +"  2> " + filepath_individual_function_log) 
    all_declared_global_name_list = []
    while len(loglist) != 0 and max_iteration > 0:
        max_iteration -= 1
        declare_global_name_list = []
        change_to_array = []
        #try compile the modified code
        #print (compiler + " -emit-llvm -O0  -c -Wl,--demangle -Wno-everything " + filepath_generatedc_modified + " -o " + filepath_generatedbc +"  2> " + filepath_individual_function_log) 
        os.system(compiler + " -emit-llvm -O0  -c -Wl,--demangle -Wno-everything " + filepath_generatedc_modified + " -o " + filepath_generatedbc +"  2> " + filepath_individual_function_log)
        
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
        fin = open(filepath_generatedc_modified,'r')
        modified_list = fin.readlines()
        fin.close()
        
        #we first write the typedef undefined4, etc        then declare all global variables,
        fout = open(filepath_generatedc_modified,'w')
        declare_global_name_list = list(set(declare_global_name_list))
        
        lengthof_modfied_head_before_global = 15
        for i in range(lengthof_modfied_head_before_global) :
            fout.write(modified_list[i])
        '''
        if change_to_array :
            print(declare_global_name_list)
            print(change_to_array)
        '''
        htmllinecount = 0
        #print(filepath_generatedc_modified)
        #print(len(htmllinelist))
        #print(declare_global_name_list)
        #'''
        can_be_declared_by_ghidra_global_name_list = []
        for i in range(len(declare_global_name_list)):
            while htmllinecount < len(htmllinelist):
                htmllinelist[htmllinecount] = htmllinelist[htmllinecount].replace(".","_")
                if declare_global_name_list[i]+":" in htmllinelist[htmllinecount] :
                    
                    #print(htmllinelist[htmllinecount] )
                    htmllinecount += 1 #go to next line.
                    while "HREF" in htmllinelist[htmllinecount] : 
                        htmllinecount += 1
                    if  ".data" in htmllinelist[htmllinecount]:
                        if "undefine..." in htmllinelist[htmllinecount] :  #handling undefined array, make it byte string, 
                            array_size = 0
                            value_list = []
                            htmllinecount += 1
                            while "["+str(array_size)+"]" in htmllinelist[htmllinecount]:
                                #'''
                                try :
                                    #print(htmllinelist[htmllinecount].split())
                                    type_info = htmllinelist[htmllinecount].split()[4]
                                    value_info = htmllinelist[htmllinecount].split()[5]
                                    if "h" in  value_info:
                                        value_info = "0x"+value_info.replace("h","")
                                    value_list.append(value_info)
                                    htmllinecount += 1
                                    array_size += 1
                                except:
                                    pass
                                #'''
                            if "??" in type_info:
                                    fout.write("int " + declare_global_name_list[i] + "; //add global variable by muqi\n")
                            else:
                                if array_size > 0 :
                                    fout.write(type_info +" "+ declare_global_name_list[i] +"[] = {")
                                    for len_value_list in range(len(value_list)-1):
                                        fout.write(value_list[len_value_list]+",")
                                    fout.write(value_list[len(value_list)-1])
                                    fout.write(" }; //based on value of ghidra, add global variable tagged by muqi\n")
                                else:
                                    fout.write("int " + declare_global_name_list[i] + "; //add global variable by muqi\n")
                            can_be_declared_by_ghidra_global_name_list.append(declare_global_name_list[i])
                        else :
                            try :
                                type_info = htmllinelist[htmllinecount].split()[2]
                                value_info = htmllinelist[htmllinecount].split()[3]
                                if "h" in  value_info:
                                    value_info = "0x"+value_info.replace("h","")
                                
                                
                                if "??" in type_info:
                                    fout.write("int " + declare_global_name_list[i] + "; //add global variable by muqi\n")
                                else:
                                    fout.write(type_info +" " + declare_global_name_list[i] + " = "+value_info +" ; //based on value of ghidra, add global variable tagged by muqi\n")
                                
                                can_be_declared_by_ghidra_global_name_list.append(declare_global_name_list[i])
                                #print("removing element from list finished")
                            except:
                                pass
                else:
                    pass
                #print(htmllinecount)
                htmllinecount += 1
        #'''
        #remove the global variable can be initilized based on ghidra
        #print("looping of finding info in ghidra finished1")
        for i in range(len(can_be_declared_by_ghidra_global_name_list)):
            declare_global_name_list.remove(can_be_declared_by_ghidra_global_name_list[i])
            
            
        #print("looping of finding info in ghidra finished2")
        #print(declare_global_name_list)
        for i in range(len(declare_global_name_list)):
            fout.write("int " + declare_global_name_list[i] + "; //add global variable by muqi\n")
        
        all_declared_global_name_list.extend(declare_global_name_list)
        
        declare_global_name_is_pointer = False
        
        #wrote the remaining cotent to file
        i = lengthof_modfied_head_before_global
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
def find_functionargs(filepath_generated_whole_c,filename_c):
    filepath_whole_decompiled_c= filepath_generated_whole_c
    filename_whole_decompiled_c = filename_c
    filepath_function_namec= os.path.join(directname_function_name,filename_whole_decompiled_c.replace(".c",""))
    
    fin = open(filepath_whole_decompiled_c,'r')
    originalc_linelist = fin.readlines()
    fin.close()
    
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
        k = 0
        while k < len(originalc_linelist):
            if  (";" not in  originalc_linelist[k] )and ( (  function_name_list[i].replace(".","_")+"\n" in originalc_linelist[k][0:len(function_name_list[i])+1] and "(" in  originalc_linelist[k+1]) or ( function_name_list[i].replace(".","_")+"(" in originalc_linelist[k][0:len(function_name_list[i])+1])or (" "+function_name_list[i].replace(".","_")+"(" in originalc_linelist[k]) or ( " "+function_name_list[i].replace(".","_")+"\n" in originalc_linelist[k] and "(" in originalc_linelist[k+1] )) :
                #print("!!!!!!!!!codeeee" +str(k)+" : "+originalc_linelist[k])
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
                #print("In find_functionargs")
                #print(function_name_list[i])
                #print(function_declare_string)

                
                if "{" == originalc_linelist[function_declare_end+2][0] and ";" not in originalc_linelist[function_declare_end]:
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

def seperate_function_compilation(filepath_generated_whole_c,filename_c,filepath_generated_html,filepath_generated_function_name,directname_folder_for_project,directname_folder_for_log,directname_generated_whole_c,directname_generatedbc,trigger_long_to_char_star):
    comment_struct_list = ["struct _IO_FILE {","struct _IO_marker {","struct anon_struct.conflict","union anon_union.conflict","struct Test.conflict","struct route_info.conflict"]
    direct_comment_list = ["typedef struct __mbstate_t __mbstate_t, *P__mbstate_t;","typedef struct __fsid_t __fsid_t, *P__fsid_t;","typedef enum anon_enum_32.conflict",
    "typedef struct __va_list_tag __builtin_va_list[1];","typedef struct anon_struct.conflict","typedef union anon_union.conflict","typedef unsigned char    bool;", "typedef bool _Bool;"
    ,"typedef enum enum_1434","typedef struct route_info.conflict route_info.conflict, *Proute_info.conflict", "typedef struct Test.conflict Test.conflict, *PTest.conflict","typedef void * __gnuc_va_list",
    "typedef char __int8_t"]
    comment_with_double_slides = ["struct blk_zone[0] zones;","char[0] name;","ERROR=22,","jmp_buf b;","jmp_buf * bailout;"]
    
    filename_whole_decompiled_c = filename_c
    filepath_whole_decompiled_c= filepath_generated_whole_c
    #filepath_function_namec= os.path.join(directname_function_name,filename_whole_decompiled_c.replace(".c",""))
    filepath_function_namec = filepath_generated_function_name
    filepath_whole_decompiled_html =filepath_generated_html
    function_name_list = []
    first_function_name = ""
    fin = open("../function_name/"+filename_c.replace(".c",""),'r')
    linelist_original = fin.readlines()
    fin.close()
    first_function_name = linelist_original[0][:-1]
    
    try:
        fin = open(filepath_function_namec,'r')
        linelist = fin.readlines()
        fin.close()
        #first_function_name = linelist[0][:-1]
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
    for i in range(len(originalc_linelist)-1):
        if first_function_name in originalc_linelist[i+1]:
            if ("{" in originalc_linelist[i+3]  and "\n" in originalc_linelist[i+2][0] ) or ("{" in originalc_linelist[i+4]  and "\n" in originalc_linelist[i+3][0] ) or ("{" in originalc_linelist[i+5]  and "\n" in originalc_linelist[i+4][0]) or ("{" in originalc_linelist[i+6]  and "\n" in originalc_linelist[i+5][0]) :
                if "\n" not in originalc_linelist[i][0]:
                    break
                else:
                    fout.write("\n")
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
    print("in seperate_function_compilation:")
    print(function_name_list)
    
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
            
            
                print(function_declare_start)
                print(function_declare_end)
            
                function_declare_string = ""
                for function_iter in range(function_declare_start,function_declare_end + 1):
                    function_declare_string += originalc_linelist[function_iter].replace("\n","")
                    #here we replace long param to char* param to solve the type recovery issue in ghidra!!
                    if trigger_long_to_char_star == True:
                        #print("INSIDE trigger_long_to_char_star\n\n!!!!\n\n")
                        #print(originalc_linelist[function_iter])
                        originalc_linelist[function_iter] = originalc_linelist[function_iter].replace("long param","char* param")
                        function_declare_string= function_declare_string.replace("long param","char* param")
                        #print(originalc_linelist[function_iter])
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
            automatic_compilation(filepath_individual_function,filepath_individual_function_bc,function_name_list[i],filepath_individual_function_log,filepath_whole_decompiled_html)
        except:
            pass
    

def angr_running_pointer(arg1,arg2,angr_project,pcfg_input,filename,log_file):

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

    #print(hex(required_address))

    #use cfgfast to identify the boundry of basic block
    #pcfg = p.analyses.CFGFast(normalize = True)
    pcfg = pcfg_input
    pcfg = pcfg.functions.get(required_address).transition_graph

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
            
    state = p.factory.call_state(log_filepath, required_address,args[0],args[1],args[2],args[3],args[4],args[5],args[6],args[7],args[8],args[9],args[10],add_options={angr.options.CALLLESS,angr.options.STRINGS_ANALYSIS,angr.options.ZERO_FILL_UNCONSTRAINED_MEMORY,angr.options.ZERO_FILL_UNCONSTRAINED_REGISTERS},remove_options=angr.options.simplification)
     
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

def remove_duplicated_function_name(filename_path):
    fread = open(filename_path,'r')
    read_linelist = fread.readlines()
    fread.close()
    
    read_linelist = list(dict.fromkeys(read_linelist))
    
    fwrite = open(filename_path,'w')
    for i in range(len(read_linelist)):
        if ":" not in read_linelist[i]:
            fwrite.write(read_linelist[i])
    fwrite.close()

def create_and_copy_correct_function_name(filepath_originalclang,filename_path,filename_path_original,file_function_name,ghidra_scripts_folder_address_base):
    ghidra_repo_address = ghidra_repo_address_folder+ file_function_name+"_name.gpr"
    os.system(ghidra_address+" "+ghidra_repo_address+" -import " + filepath_originalclang + " -overwrite -scriptPath " + ghidra_scripts_folder_address_base +" -prescript "+ ghidra_decompiled_java_script3 + " -postscript " + ghidra_get_function_name_java_script+" "+filename_path +" ")
    fread = open(filename_path_original,'r')
    read_linelist_in = fread.readlines()
    fread.close()
    
    fread = open(filename_path,'r')
    read_linelist_out = fread.readlines()
    fread.close()
    
    
    fwrite = open(filename_path,'w')
    for i in range(len(read_linelist_in)):
        for j in range(len(read_linelist_out)):
            if read_linelist_in[i][:-1] in read_linelist_out[j][0:len(read_linelist_in[i][:-1])]:
                fwrite.write(read_linelist_out[j])
    fwrite.close()

def permutate_run_ghidra(filepath_originalclang,filepath_generated_whole_c,file_function_name,ghidra_scripts_folder_address_base):
    ghidra_repo_address = ghidra_repo_address_folder+ file_function_name+"_original.gpr"
    print(ghidra_address+" "+ghidra_repo_address+" -import " + filepath_originalclang + " -overwrite -scriptPath " + ghidra_scripts_folder_address_base +" -prescript "+ ghidra_decompiled_java_script3 + " -postscript " + ghidra_decompiled_java_script2+" "+filepath_generated_whole_c +" ")
    os.system(ghidra_address+" "+ghidra_repo_address+" -import " + filepath_originalclang + " -overwrite -scriptPath " + ghidra_scripts_folder_address_base +" -prescript "+ ghidra_decompiled_java_script3 + " -postscript " + ghidra_decompiled_java_script2+" "+filepath_generated_whole_c +" ")

def generate_function_html(filepath_originalclang,filepath_generated_html,filename,ghidra_scripts_folder_address_base):
    ghidra_repo_address = ghidra_repo_address_folder+ filename+"_html.gpr"
    os.system(ghidra_address+" "+ghidra_repo_address+" -import " + filepath_originalclang + " -overwrite -scriptPath " + ghidra_scripts_folder_address_base +" -postscript " + ghidra_decompiled_java_script5+" "+filepath_generated_html +" ")

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
def main_each_function_klee(i,function_name_list,filename,filepath_originalclang,directname_generatedbc,directname_model,directname_log_klee):

    function_name = function_name_list[i]
    filepath_generatedbc = os.path.join(directname_generatedbc, filename+"_"+function_name[:-1]+".bc")

    if os.path.isfile(filepath_generatedbc)  :
        #run prompt for symbolic execution
        #generate model.txt for prompt for that function
        print(filepath_generatedbc)
        model_function_name = "model"+filename+"_"+function_name[:-1] +".txt"
        filepath_prompt_model_on_function = os.path.join(directname_model, model_function_name)
        log_klee_function_name = "log_klee"+filename+"_"+function_name[:-1] +".txt"
        filepath_log_klee = os.path.join(directname_log_klee,log_klee_function_name)
        os.system("rm /tmp/klee_"+filename+"_"+function_name[:-1] +"_test.txt")
        
        f = open(filepath_prompt_model_on_function, "w")
        f.write("global settings:\ndata models:\nfunction models:\nlifecycle model:\n    entry-point "+ function_name.replace(".","_"))
        #f.write("global settings: array size 0;\ndata models:(0 = w) where w is argsize "+function_name+" arg 0;\nfunction models:\nlifecycle model:\n    entry-point "+ function_name)
        f.close()
        
        print("timeout 300s /home/muqi/PROMPT/build/bin/klee  -prose-api-model="+filepath_prompt_model_on_function+ " --search=bfs --solver-backend=z3 --posix-runtime " + filepath_generatedbc + " > "+ filepath_log_klee)
        
        #'''
        #os.system("timeout 300s /home/muqi/PROMPT/build/bin/klee  -prose-api-model="+filepath_prompt_model_on_function+ " --search=bfs --solver-backend=z3 --posix-runtime " + filepath_generatedbc + " > "+ filepath_log_klee)
        run_cmd("/home/muqi/PROMPT/build/bin/klee  -prose-api-model="+filepath_prompt_model_on_function+ " --search=bfs --solver-backend=z3 --posix-runtime " + filepath_generatedbc + " > "+ filepath_log_klee, 180)

class thread_with_trace(threading.Thread):
    def __init__(self, *args, **keywords):
        threading.Thread.__init__(self, *args, **keywords)
        self.killed = False
    def start(self):
        self.__run_backup = self.run
        self.run = self.__run
        threading.Thread.start(self)

    def __run(self):
        sys.settrace(self.globaltrace)
        self.__run_backup()
        self.run = self.__run_backup

    def globaltrace(self, frame, event, arg):
        if event == 'call':
            return self.localtrace
        else:
            return None

    def localtrace(self, frame, event, arg):
        if self.killed:
            if event == 'line':
                raise SystemExit()
        return self.localtrace

    def kill(self):
        self.killed = True

@func_set_timeout(120)
def main_each_function_angr(i,function_name_list,filename,pcfg_angr,angr_project,filepath_originalclang,directname_generatedbc,directname_model,directname_log_klee,angrlog_file,kleelog_file,bothwork_file,log_file,directname_generatedc,directname_z3,directname_diff):

    angr_work = True
    klee_work = True
    angr_log_work = True
    klee_log_work = True
    function_name = function_name_list[i]
    filepath_generatedbc = os.path.join(directname_generatedbc, filename+"_"+function_name[:-1]+".bc")
    
    if os.path.isfile("/tmp/angr_"+ filename+"_"+function_name_list[i]+"_ir_third_flip.txt"):
        try:
            analyze_results.analyze_results(i,filename,function_name,directname_generatedc,directname_z3,directname_diff)
        except:
            klee_log_work = False
            f = open(kleelog_file, "a")
            f.write(filename+": "+function_name + " is wrong during z3 analyzing!\n")
            f.close()

        return

    if os.path.isfile(filepath_generatedbc)  :
        log_klee_function_name = "log_klee"+filename+"_"+function_name[:-1] +".txt"
        filepath_log_klee = os.path.join(directname_log_klee,log_klee_function_name)
        try:
            f = open( filepath_log_klee, 'r')
            log_lines = f.readlines()[-1]
            f.close()
            if 'terminating state' not in log_lines:
                klee_work = False
                f = open(kleelog_file, "a")
                f.write(filename+": "+function_name + " is wrong! not terminated\n")
                f.close()
        except:
            klee_work = False
            f = open(kleelog_file, "a")
            f.write(filename+": "+function_name + " is wrong!  not terminated\n")
            f.close()
        

        #run angr for symbolic execution
                 
        try:
        
            if klee_work == True:
                angr_running_pointer(filepath_originalclang,function_name[:-1],angr_project,pcfg_angr,filename,log_file)
        except:
            f = open(angrlog_file, "a")
            f.write(filename+": "+function_name + " is wrong!\n")
            f.close()
            angr_work = False
        

                
        #'''
        #start analyzing
        if klee_work == True and angr_work == True:
            #generate angr result
            try:
                log_filepath_no_suffix='/tmp/angr_'+filename +'_'+ function_name[:-1] 
                angr_log = log_filepath_no_suffix+".txt"
                angr_ir_first = log_filepath_no_suffix+ "_ir_first.txt"
                angr_ir_second = log_filepath_no_suffix+"_ir_second.txt"
                angr_ir_third = log_filepath_no_suffix +"_ir_third.txt"
                angr_ir_third_flip = log_filepath_no_suffix+"_ir_third_flip.txt"
                #'''
                analyze_angr.reset_global(angr_log,angr_ir_first,angr_ir_second,angr_ir_third,angr_ir_third_flip)
                analyze_angr.build_basic_block(angr_log,angr_ir_first,angr_ir_second,angr_ir_third,angr_ir_third_flip)
                analyze_angr.generate_ir_first_version(angr_log,angr_ir_first,angr_ir_second,angr_ir_third,angr_ir_third_flip)
                analyze_angr.generate_father_block_second_version(angr_log,angr_ir_first,angr_ir_second,angr_ir_third,angr_ir_third_flip)
                analyze_angr.generate_children_block_second_version(angr_log,angr_ir_first,angr_ir_second,angr_ir_third,angr_ir_third_flip)
                analyze_angr.cfg_to_ir(angr_ir_third,angr_ir_third_flip)
                analyze_angr.ir_reorder(angr_ir_third_flip)
                #'''
            except:
                angr_log_work = False
                f = open(angrlog_file, "a")
                f.write(filename+": "+function_name + " is wrong during analyzing!\n")
                f.close()
                    
            #generate klee result
            #analyze_results.analyze_results(i,filename,function_name)
            #'''
            if angr_log_work == True:
                try: 
                    analyze_results.analyze_results(i,filename,function_name,directname_generatedc,directname_z3,directname_diff)
                except:
                    klee_log_work = False 
                    f = open(kleelog_file, "a")
                    f.write(filename+": "+function_name + " is wrong during z3 analyzing!\n")
                    f.close()
            #'''
                
            if klee_log_work == True and angr_log_work == True:
                f = open(bothwork_file, "a")
                f.write(filename+": "+function_name + " worked !\n")
                f.close()

def after_timeout():
    print ("Inside after timeout")
    raise SystemExit


def self_regenerate_symbolic(filename,function_name_temp,directname_whole_test_folder,filepath_original_function_name_individual,ghidra_scripts_folder_address_base,trigger_long_to_char_star,angr_project,pcfg_angr):
    angrlog_file = directname_whole_test_folder+"log_angr"
    kleelog_file = directname_whole_test_folder+"log_klee2"
    bothwork_file = directname_whole_test_folder+"both_work"
    log_file = directname_whole_test_folder+ "angrlog_pcode"
    
    directname_originalclang= directname_whole_test_folder+"originalclang/"
    directname_generated_whole_c = directname_whole_test_folder+"generated_whole_c"
    directname_folder_for_project=directname_whole_test_folder+"generated_function_c/project_folder"
    directname_folder_for_log = directname_whole_test_folder+"generated_function_c/log_for_compile"
    directname_function_name= directname_whole_test_folder+"function_name_generated"
    directname_generatedbc = directname_whole_test_folder+"generatedbc"
    directname_model = directname_whole_test_folder + "model_prompt"
    directname_log_klee = directname_whole_test_folder + "log_klee"
    directname_generatedc = directname_whole_test_folder + "generatedc"
    directname_z3 = directname_whole_test_folder + "z3"
    directname_diff = directname_whole_test_folder + "diff"
    directname_generated_html = directname_whole_test_folder+"generated_html"
    
    os.system("rm "+angrlog_file)
    os.system("rm "+kleelog_file)
    os.system("rm "+ bothwork_file)
    os.system("rm "+ directname_whole_test_folder+"log_klee.txt")
    os.system("rm -r "+directname_whole_test_folder+"generatedbc/*")
    
    file_function_name = filename +"_"+function_name_temp
    i = 0
    filenames = []
    if filename in os.listdir(directname_originalclang):
    
        #reset dictionary
        global dic_funcname_funcargs 
        dic_funcname_funcargs = {}
        
        
        filename_c = filename + ".c"
        filename_bc = filename +".bc"
        filename_html = filename + ".html"
        filename_clang = filename
        filename_ll = filename+".ll"
        
        filepath_originalclang = os.path.join(directname_originalclang,filename_clang)
        
        filepath_generated_whole_c = os.path.join(directname_generated_whole_c, filename_c)
        filepath_generated_html = os.path.join(directname_generated_html, filename_html)
        filepath_generated_function_name= os.path.join(directname_function_name,filename_clang)
        filepath_original_function_name = filepath_original_function_name_individual
        
        
        #'''
        if trigger_long_to_char_star == False:
            t1 = threading.Thread(target = permutate_run_ghidra, args = (filepath_originalclang,filepath_generated_whole_c,file_function_name,ghidra_scripts_folder_address_base))
            t2 = threading.Thread(target = create_and_copy_correct_function_name, args = (filepath_originalclang,filepath_generated_function_name,filepath_original_function_name,file_function_name,ghidra_scripts_folder_address_base))
            t3 = threading.Thread(target = generate_function_html, args = (filepath_originalclang,filepath_generated_html,file_function_name,ghidra_scripts_folder_address_base))
    
            t1.start()
            #t1.join()
            t2.start()
            t3.start()
            t1.join()
            t2.join()
            t3.join()
        

        function_filename_file = open(filepath_generated_function_name, 'r')
        function_name_list = function_filename_file.readlines()
        function_filename_file.close()
        
        print("before seperate_function_compilation")
        seperate_function_compilation(filepath_generated_whole_c,filename,filepath_generated_html,filepath_generated_function_name,directname_folder_for_project,directname_folder_for_log,directname_generated_whole_c,directname_generatedbc,trigger_long_to_char_star)
        print("after seperate_function_compilation")
        print(function_name_list)

        for i in range(len(function_name_list)):
            main_each_function_klee(i,function_name_list,filename,filepath_originalclang,directname_generatedbc,directname_model,directname_log_klee)

        
        for i in range(len(function_name_list)):
            try:
                main_each_function_angr(i,function_name_list,filename,pcfg_angr,angr_project,filepath_originalclang,directname_generatedbc,directname_model,directname_log_klee,angrlog_file,kleelog_file,bothwork_file,log_file,directname_generatedc,directname_z3,directname_diff)
            except FunctionTimedOut as e:
                pass




def check_void(directname_function_content,individual_functionname):

    try:
        #print(directname_function_content)
        fout = open(directname_function_content,'r')
        linelist = fout.readlines()
        fout.close()
        #'''
        for i in range(len(linelist)):
            if individual_functionname+"(" in linelist[i] and  "void " in linelist[i][:5]:
                return True
        return False
        #'''
    except:
        print("Inside check_void cannot open "+ whole_functionname)
        return True

def check_pointer_return(directname_function_content,individual_functionname):
   
    try:
        #print(directname_function_content)
        fout = open(directname_function_content,'r')
        linelist = fout.readlines()
        fout.close()
        #'''
        for i in range(len(linelist)):
            if individual_functionname+"(" in linelist[i]:
                pattern = '(.+?)'+individual_functionname
                return_type_info = re.search(pattern,linelist[i]).group(1)
                #print(return_type_info)
                #print(linelist[i])
                if "*" in return_type_info:
                    #print(return_type_info)
                    #print(linelist[i])
                    return True
        return False
        #'''
    except:
        print("Inside check_pointer_return cannot open "+ whole_functionname)
        return True

    
def check_diff(filename_partial,directname_diff,directname_whole_test_folder,filename_forfile):
    #os.system("rm "+ output_diff)
    remove_this_function_for_all = False
    for filename in os.listdir(directname_diff):
        print(filename)
        fdiffpath  = os.path.join(directname_diff,filename)
        fdiffin = open(fdiffpath,'r')
        linelistdiff = fdiffin.readlines()
        fdiffin.close()
        
        '''
        whole_functionname = re.search('(.+?)_z3',filename).group(1)
        filename_forfile = "Unknown" 
        os.system("find "+directname_whole_test_folder+" -name " + whole_functionname+".c > "+directname_whole_test_folder+"temp_found_file.txt")
        f_file = open(directname_whole_test_folder+"temp_found_file.txt",'r')
        linelist = f_file.readlines()
        f_file.close()
        directname_function_content = linelist[0][:-1]
        file_name = re.search('/generated_function_c/project_folder/(.+?)_folder',directname_function_content).group(1)
        filename_forfile = file_name
        '''
        whole_functionname = re.search('(.+?)_z3',filename).group(1)
        directname_function_content = "./test_muqi/"+whole_functionname+"/generated_function_c/project_folder/"+filename_forfile+"_folder/*.c"


        remove_this_function_individual = True
        if len(linelistdiff) > 1 :
            remove_this_function_individual = False
        elif len(linelistdiff) == 0 :
            remove_this_function_individual = False
        else :
            if 'unsat' == ("xxxxx"+filename)[-5:]:
                try:
                    cond = linelistdiff[0][0:5] == 'unsat'
                except:
                    remove_this_function_individual = False
            else :
                try:
                    cond = linelistdiff[0][0:3] == 'sat' 
                except:
                    remove_this_function_individual = False
            if cond != True:
                    remove_this_function_individual = False
            
        remove_this_function_for_all = remove_this_function_for_all or remove_this_function_individual
        if remove_this_function_individual == True:
            directname_remove_function_folder= os.path.join(directname_regenerated_correct_result,filename_forfile+"_folder")
            os.system("mkdir "+ directname_remove_function_folder)
            os.system("cp "+directname_function_content + " " + directname_remove_function_folder+"/")
            
    
    return remove_this_function_for_all

def rewrite_java(filepath_ghidra,ghidra_base_linelist,Java_option_dictionary):
    fout_ghidra = open(filepath_ghidra,'w')
    for j in range(len(ghidra_base_linelist)):
        fout_ghidra.write(ghidra_base_linelist[j].replace("Decompile_pre_base","Decompile_pre"))
        if "muqi change start" in ghidra_base_linelist[j]:
            for option_name in Java_option_dictionary:
                option_value = Java_option_dictionary[option_name]
                if option_value :
                    option_value_str = "true"
                else:
                    option_value_str = "false"
                fout_ghidra.write("setAnalysisOption(currentProgram, \""+option_name+"\", \""+option_value_str+"\");\n")
                
    fout_ghidra.close()



decompiler_policy_folder = "./test_muqi_base/decompile_special/"
dp_dict = {}

#read each file in decompiler_policy_folder, hash them to our hashtable
def init_hash_to_dp():
    global dp_dict
    dp_dict = {}
    for filename in os.listdir(decompiler_policy_folder):
        filepath_dp = os.path.join(decompiler_policy_folder,filename)
        fopen = open (filepath_dp,'r')
        dp_string = fopen.read()
        fopen.close()
        dp_dict[filename] = dp_string

def hash_dp_string_to_rule(outputstring):
    rule = re.split("following rules are banned:\n",outputstring)[1]
    return rule

def hash_dp_string_to_Java_option(outputstring):
    Java_rule_string = re.split("following rules are banned:\n",outputstring)[0]
    Java_rule_string_array = re.split(r'[\n]',Java_rule_string)
    Java_option_dictionary =  {}

    for Java_option in Java_rule_string_array :
        if ":" in Java_option:
            Java_option = Java_option.replace("\n","")
            Java_option_name = re.split(":",Java_option)[0]
            Java_option_value = re.split(":",Java_option)[1]
            if "true" in Java_option_value:
                Java_option_dictionary[Java_option_name] = True    
            else:
                Java_option_dictionary[Java_option_name] = False
    return Java_option_dictionary

#check hash table, if new, we need to add this decompiler combination to folder
def insert_hash_to_dp(Java_option_dictionary,rule):
    global dp_dict 
    outputstring = ""
    for option_name in Java_option_dictionary:
        option_value = Java_option_dictionary[option_name]
        if option_value :
            option_value_str = "true"
        else:
            option_value_str = "false"
        outputstring += option_name+":"+option_value_str+"\n"
    outputstring += "following rules are banned:\n"
    outputstring += rule +"\n"

    dp_exist = False
    for filename, dp_string in dp_dict.items():
        if outputstring.replace("\n","") == dp_string.replace("\n",""):
            dp_exist = True
    
    if dp_exist == False :
        #first record this to dp hashfile
        size = len (dp_dict)
        newfilename = size + 1
        newfilepath = os.path.join(decompiler_policy_folder, str(newfilename))
        fnew = open (newfilepath,'w')
        fnew.write(outputstring)
        fnew.close()

        #second add this to hash table
        dp_dict[newfilename] = outputstring

def write_to_show_off(result_show_off,diff_partial_name,Java_option_dictionary):
    f_show_off = open (result_show_off,'a')
    f_show_off.write(diff_partial_name+":\n")
    for option_name in Java_option_dictionary:
        option_value = Java_option_dictionary[option_name]
        if option_value :
            option_value_str = "true"
        else:
            option_value_str = "false"
        f_show_off.write(option_name+":"+option_value_str+"\n")
    f_show_off.close()


def write_to_show_off_message(result_show_off,diff_partial_name,message):
    f_show_off = open (result_show_off,'a')
    f_show_off.write(diff_partial_name+":\n")
    f_show_off.write(message+"\n")
    f_show_off.close()

def write_to_show_off_message_direct_append(result_show_off,message):
    f_show_off = open (result_show_off,'a')
    f_show_off.write(message+"\n")
    f_show_off.close()

def write_to_show_off_rules(result_show_off,rule):
    f_show_off = open (result_show_off,'a')
    f_show_off.write("following rules are banned:\n")
    f_show_off.write(rule+"\n")
    f_show_off.close()

def check_double(Java_option_dictionary,filepath_ghidra,ghidra_base_linelist,filename,function_name_temp,directname_whole_test_folder,filepath_original_function_name_individual,ghidra_scripts_folder_address_base,angr_project,pcfg_angr,directname_diff,result_show_off,diff_partial_name):
    self_regenerate_symbolic(filename,function_name_temp,directname_whole_test_folder,filepath_original_function_name_individual,ghidra_scripts_folder_address_base,False,angr_project,pcfg_angr)
    return_result = check_diff(filename+"_"+function_name_temp+"_z3",directname_diff,directname_whole_test_folder,filename)
    if return_result == True:
        write_to_show_off(result_show_off,diff_partial_name,Java_option_dictionary)
        return True
    else :
        #retry with type recovery problem
        self_regenerate_symbolic(filename,function_name_temp,directname_whole_test_folder,filepath_original_function_name_individual,ghidra_scripts_folder_address_base,True,angr_project,pcfg_angr)
        return_result = check_diff(filename+"_"+function_name_temp+"_z3",directname_diff,directname_whole_test_folder,filename)
        if return_result == True:
            write_to_show_off(result_show_off,diff_partial_name,Java_option_dictionary)
            return True
    return False
    


def c120_1(avail_rules,Java_option_dictionary,filepath_ghidra,ghidra_base_linelist,filename,function_name_temp,directname_whole_test_folder,filepath_original_function_name_individual,ghidra_scripts_folder_address_base,angr_project,pcfg_angr,directname_diff,result_show_off,diff_partial_name):
    for option_name, option_value in Java_option_dictionary.items():
        start_time = time.time()
        #we negative this value first
        Java_option_dictionary[option_name] = not option_value
        
        rewrite_java(filepath_ghidra,ghidra_base_linelist,Java_option_dictionary)
        result = check_double(Java_option_dictionary,filepath_ghidra,ghidra_base_linelist,filename,function_name_temp,directname_whole_test_folder,filepath_original_function_name_individual,ghidra_scripts_folder_address_base,angr_project,pcfg_angr,directname_diff,result_show_off,diff_partial_name)
        if result == True:
            insert_hash_to_dp(Java_option_dictionary,"")
            return True
         #we restore value back
        Java_option_dictionary[option_name] = option_value
        
        write_to_show_off_message_direct_append(result_show_off,"filename: " + filename  + " function_name: "+ function_name_temp +" rule: "+ option_name +" time: "+str(time.time()-start_time))


    for rule in avail_rules:
        start_time = time.time()
        fout = open("/tmp/ghidra_gate_"+filename+"_"+function_name_temp, "w")
        fout.write(rule)
        fout.close()
        result = check_double(Java_option_dictionary,filepath_ghidra,ghidra_base_linelist,filename,function_name_temp,directname_whole_test_folder,filepath_original_function_name_individual,ghidra_scripts_folder_address_base,angr_project,pcfg_angr,directname_diff,result_show_off,diff_partial_name)
        if result == True:
            write_to_show_off_rules(result_show_off,rule)
            insert_hash_to_dp(Java_option_dictionary,rule)
            return True

        write_to_show_off_message_direct_append(result_show_off,"filename: " + filename  + " function_name: "+ function_name_temp +" rule: "+ rule +" time: "+str(time.time()-start_time))

    return False
    

def c120_2(avail_rules,Java_option_dictionary,filepath_ghidra,ghidra_base_linelist,filename,function_name_temp,directname_whole_test_folder,filepath_original_function_name_individual,ghidra_scripts_folder_address_base,angr_project,pcfg_angr,directname_diff,result_show_off,diff_partial_name):
    for option_name1, option_value1 in Java_option_dictionary.items():
        #we negative this value first
        for option_name2, option_value2 in Java_option_dictionary.items():
            Java_option_dictionary[option_name1] = not option_value1
            Java_option_dictionary[option_name2] = not option_value2
            rewrite_java(filepath_ghidra,ghidra_base_linelist,Java_option_dictionary)
            result = check_double(Java_option_dictionary,filepath_ghidra,ghidra_base_linelist,filename,function_name_temp,directname_whole_test_folder,filepath_original_function_name_individual,ghidra_scripts_folder_address_base,angr_project,pcfg_angr,directname_diff,result_show_off,diff_partial_name)
            if result == True:
                insert_hash_to_dp(Java_option_dictionary,"")
                return True
             #we restore value back
            Java_option_dictionary[option_name1] = option_value1
            Java_option_dictionary[option_name2] = option_value2

    for rule1 in avail_rules:
        for rule2 in avail_rules:
            fout = open("/tmp/ghidra_gate_"+filename+"_"+function_name_temp, "w")
            fout.write(rule1)
            fout.write("\n")
            fout.write(rule2)
            fout.close()
            result = check_double(Java_option_dictionary,filepath_ghidra,ghidra_base_linelist,filename,function_name_temp,directname_whole_test_folder,filepath_original_function_name_individual,ghidra_scripts_folder_address_base,angr_project,pcfg_angr,directname_diff,result_show_off,diff_partial_name)
            if result == True:
                write_to_show_off_rules(result_show_off,rule1+"\n"+rule2)
                insert_hash_to_dp(result_show_off,rule1+"\n"+rule2)
                return True
    
    for option_name1, option_value1 in Java_option_dictionary.items():
        for rule1 in avail_rules:
            Java_option_dictionary[option_name1] = not option_value1
            fout = open("/tmp/ghidra_gate_"+filename+"_"+function_name_temp, "w")
            fout.write(rule1)
            fout.close()
            rewrite_java(filepath_ghidra,ghidra_base_linelist,Java_option_dictionary)
            result = check_double(Java_option_dictionary,filepath_ghidra,ghidra_base_linelist,filename,function_name_temp,directname_whole_test_folder,filepath_original_function_name_individual,ghidra_scripts_folder_address_base,angr_project,pcfg_angr,directname_diff,result_show_off,diff_partial_name)
            if result == True:
                write_to_show_off_rules(result_show_off,rule1)
                insert_hash_to_dp(result_show_off,rule1)
                return True
             #we restore value back
            Java_option_dictionary[option_name1] = option_value1

    return False

def permuate_each_function(read_linelist_in,result_show_off,filename,i):
    function_name_temp = read_linelist_in[i][:-1]
    file_function_name = filename+"_"+function_name_temp
    
    directname_whole_test_folder = "./test_muqi/"+file_function_name+"/"
    directname_diff = directname_whole_test_folder+"diff/"
    
    os.system("mkdir "+ directname_whole_test_folder)
    os.system("cp -r ./test_muqi_base/* " + directname_whole_test_folder)
    os.system("cp " +"../test_muqi/originalclang/"+filename+" "+directname_whole_test_folder+"originalclang/")
    
    filepath_original_function_name_individual = directname_whole_test_folder+"function_name/"+file_function_name+".txt"
    fwrite = open(filepath_original_function_name_individual,'w')
    #we do not need this for first function anymore
    #fwrite.write(read_linelist_in[0])
    fwrite.write(read_linelist_in[i])
    fwrite.close()
    
    #build ghidra script folder
    ghidra_scripts_folder_address_base = ghidra_decompiled_java_script_inall+file_function_name+"_ghidra_script/"
    os.system("mkdir "+ ghidra_scripts_folder_address_base)
    
    os.system("cp "+ghidra_decompiled_java_script_base+"* "+ ghidra_scripts_folder_address_base)
    filepath_ghidra_base = os.path.join(ghidra_scripts_folder_address_base,ghidra_decompiled_java_script4)
    filepath_ghidra = os.path.join(ghidra_scripts_folder_address_base,ghidra_decompiled_java_script3)
    fin_ghidra_base = open(filepath_ghidra_base,'r')
    ghidra_base_linelist = fin_ghidra_base.readlines()
    fin_ghidra_base.close()
    
    #default value
    Java_option_dictionary =  {
                                            "DWARF":True,
                                            "Apply Data Archives" :True,
                                            "Decompiler Parameter ID" : False,
                                            "x86 Constant Reference Analyzer":True,
                                            "Aggressive Instruction Finder":False,
                                            "DWARF Line Number": False,                                        
                                            "ASCII Strings":True,
                                            "Call Convention ID":True,
                                            "Call-Fixup Installer":True,
                                            "Condense Filler Bytes":False,
                                            "Create Address Tables":True,
                                            "Data Reference":True,
                                            
                                            "Decompiler Switch Analysis":True,
                                            "Demangler GNU":True,
                                            "ELF Scalar Operand References":True,
                                            "Embedded Media":True,
                                            "External Entry References":True,
                                            "Function ID":True,
                                            "Function Start Search":True,
                                            "GCC Exception Handlers":True,
                                            "Non-Returning Functions - Discovered":True,
                                            "Non-Returning Functions - Known":True,
                                             "Reference":True,
                                             "Shared Return Calls":True,
                                             "Stack":True,
                                             "Subroutine References":True,
                                             "Variadic Function Signature Override":False,
                                            
                                            
                                            
    }
    Java_option_dictionary_classic_5 =  {
                                            "DWARF":True,
                                            "Apply Data Archives" :True,
                                            "Decompiler Parameter ID" : False,
                                            "x86 Constant Reference Analyzer":True,
                                            "Aggressive Instruction Finder":False,
                                            "DWARF Line Number": False,
    }

    Java_option_dictionary_test_1 =  {
                                            "DWARF":True,
    }



    diff_partial_name = filename+"_"+function_name_temp+"_z3"
    
    directname_originalclang= directname_whole_test_folder+"originalclang/"
    filename_clang = filename
    filepath_originalclang = os.path.join(directname_originalclang,filename_clang)


    os.system("rm /tmp/angr_"+ filename+"_"+function_name_temp+"_ir_third_flip.txt")
    if os.path.isfile("/tmp/angr_"+ filename+"_"+function_name_temp+"_ir_third_flip.txt"):
        angr_project = 0
        pcfg_angr = 0
    else:
        try:
            angr_project = angr.Project(filepath_originalclang, engine=angr.engines.UberEnginePcode)
            pcfg_angr = angr_project.analyses.CFGFast(normalize = True)
        except:
            f = open(angrlog_file, "a")
            f.write(filename+": "+function_name_temp + " is wrong during cfg analyzing!\n")
            f.close()
        
    avail_rules = open(rules).read().split('\n')
    print(avail_rules)
    iter = 0

    os.system("rm /tmp/ghidra_gate_"+filename+"_"+function_name_temp)
    
    start_time = time.time()


    #'''code for c120
    rewrite_java(filepath_ghidra,ghidra_base_linelist,Java_option_dictionary)
    self_regenerate_symbolic(filename,function_name_temp,directname_whole_test_folder,filepath_original_function_name_individual,ghidra_scripts_folder_address_base,False,angr_project,pcfg_angr)
    return_result = check_diff(filename+"_"+function_name_temp+"_z3",directname_diff,directname_whole_test_folder,filename)
    if return_result == True:
        write_to_show_off_message(result_show_off,diff_partial_name,"Our framework's problem..works now")
        write_to_show_off_message_direct_append(result_show_off,str(time.time()-start_time))
        return 
    self_regenerate_symbolic(filename,function_name_temp,directname_whole_test_folder,filepath_original_function_name_individual,ghidra_scripts_folder_address_base,True,angr_project,pcfg_angr)
    return_result = check_diff(filename+"_"+function_name_temp+"_z3",directname_diff,directname_whole_test_folder,filename)
    if return_result == True:
        write_to_show_off_message(result_show_off,diff_partial_name,"This function has type recovery problem in its arguments, nothing related with options, it works now")
        write_to_show_off_message_direct_append(result_show_off,str(time.time()-start_time))
        return
    
    init_hash_to_dp()
    global dp_dict
    for dp_filename, dp_string in dp_dict.items():
        dp_rules = hash_dp_string_to_rule(dp_string)
        dp_Java_option_dictionary = hash_dp_string_to_Java_option(dp_string)
        rewrite_java(filepath_ghidra,ghidra_base_linelist,dp_Java_option_dictionary)
        fout = open("/tmp/ghidra_gate_"+filename+"_"+function_name_temp, "w")
        fout.write(dp_rules)
        fout.close()
        result = check_double(dp_Java_option_dictionary,filepath_ghidra,ghidra_base_linelist,filename,function_name_temp,directname_whole_test_folder,filepath_original_function_name_individual,ghidra_scripts_folder_address_base,angr_project,pcfg_angr,directname_diff,result_show_off,diff_partial_name)
        if result == True:
            write_to_show_off_rules(result_show_off,dp_rules)
            write_to_show_off_message_direct_append(result_show_off,str(time.time()-start_time))
            write_to_show_off_message_direct_append(result_show_off,"Finish with stored dp")
            return
    #write_to_show_off_message(result_show_off,diff_partial_name,"DWARF plus simple fix from 120 CANNOT fix this function")
    '''
    result = c120_1(avail_rules,Java_option_dictionary,filepath_ghidra,ghidra_base_linelist,filename,function_name_temp,directname_whole_test_folder,filepath_original_function_name_individual,ghidra_scripts_folder_address_base,angr_project,pcfg_angr,directname_diff,result_show_off,diff_partial_name)
    if result == True:
        write_to_show_off_message_direct_append(result_show_off,str(time.time()-start_time))
        write_to_show_off_message_direct_append(result_show_off,"Finished with C120_1")
        return

    '''
    #'''
    result = c120_2(avail_rules,Java_option_dictionary_classic_5,filepath_ghidra,ghidra_base_linelist,filename,function_name_temp,directname_whole_test_folder,filepath_original_function_name_individual,ghidra_scripts_folder_address_base,angr_project,pcfg_angr,directname_diff,result_show_off,diff_partial_name)
    if result == True:
        write_to_show_off_message_direct_append(result_show_off,str(time.time()-start_time))
        write_to_show_off_message_direct_append(result_show_off,"Finished with C120_2")
        return
    #'''

    write_to_show_off_message(result_show_off,diff_partial_name,"Chose 1,2 rules from 120 CANNOT fix this function")
    write_to_show_off_message_direct_append(result_show_off,str(time.time()-start_time))
    write_to_show_off_message_direct_append(result_show_off,"We cannot fix this function C120")
    return




def main_each_program(filename):
    filename_clang = filename
    filepath_original_function_name = os.path.join(directname_function_name_original,filename_clang)
    result_show_off = os.path.join(directname_regenerated_correct_result,"show_off.txt")
    fread = open(filepath_original_function_name,'r')
    read_linelist_in = fread.readlines()
    fread.close()
    
    
    #we need to seperate each function to run
    '''
    for i in range(len(read_linelist_in)):
        print("1111" + read_linelist_in[i])
        permuate_each_function(read_linelist_in,result_show_off,filename,i)
        #regenerate_each_function_clang(read_linelist_in,result_show_off,filename,i)
        print("2222" + read_linelist_in[i])
    '''
    #'''
    pool = Pool()
    args = ((read_linelist_in,result_show_off,filename,i) for i in range(len(read_linelist_in)))
    pool.starmap(permuate_each_function,args)
    pool.close()
    pool.join()
    #'''
 
def smart_change_prescript():
    result_show_off = os.path.join(directname_regenerated_correct_result,"show_off.txt")
    os.system("rm "+result_show_off)
    os.system("rm /home/muqi/ghidra_projects/*.lock")
    os.system("rm /tmp/ghidra_gate*")
    os.system("rm -r ./test_muqi/*")
    '''
    #pool = Pool()
    for filename in os.listdir(directname_function_name_original):
        main_each_program(filename)
    
    
    '''
    #'''
    pool = Pool()
    pool.map(main_each_program, os.listdir(directname_function_name_original)) 
    #'''
def main():
    #permuate_change_prescript()
    smart_change_prescript()
    
    '''
    init_hash_to_dp()
    #insert_hash_to_dp(0,0)
    global dp_dict
    for filename, dp_string in dp_dict.items():
        print(123)
        print(hash_dp_string_to_rule(dp_string))
        print(123)
        print(hash_dp_string_to_Java_option(dp_string))
        print(123)
    '''
if __name__ == "__main__":
    main()


