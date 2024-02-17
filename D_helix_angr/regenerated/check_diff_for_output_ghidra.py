import os
import sys
import math
import re

directname_diff = "./test_muqi/diff"
directname_z3 = "./test_muqi/z3"
directname_z3_after_abort_sibling = "./test_muqi/z3_after_abort_sibling"
directname_z3_fourth_cfgfast = "./test_muqi/z3_fourth_cfgfast"
output_diff = "./diff_result"
directname_originalclang = "./test_muqi/originalclang"
directname_function_big_folder= "./test_muqi/generated_function_c/project_folder"
directname_function_list = "./function_name"
directname_regenerated_function_list = "./regenerated/function_name_original"
directname_regenerated_correct_result = "./regenerated/correct_result"
directname_regenerated_tmp_folder = "./regenerated/tmp_folder"
directname_regenerated_unsolved_result = "./regenerated/unsolved_result"

def check_void(directname_function_content,individual_functionname):

    try:
        #print(directname_function_content)
        fout = open(directname_function_content,'r')
        linelist = fout.readlines()
        fout.close()
        #'''
        for i in range(len(linelist)):
            if individual_functionname in linelist[i] and  "void " in linelist[i][:5]:
                return True
        return False
        #'''
    except:
        print("Inside check_void cannot open "+ individual_functionname)
        return True

def check_double(directname_function_content,individual_functionname):

    try:
        #print(directname_function_content)
        fout = open(directname_function_content,'r')
        linelist = fout.readlines()
        fout.close()
        #'''
        for i in range(len(linelist)):
            if individual_functionname in linelist[i] and  "double " in linelist[i][:7]:
                return True
        return False
        #'''
    except:
        print("Inside check_void cannot open "+ individual_functionname)
        return True
    
def check_pointer_return(directname_function_content,individual_functionname):
   
    try:
        #print(directname_function_content)
        fout = open(directname_function_content,'r')
        linelist = fout.readlines()
        fout.close()
        #'''
        for i in range(len(linelist)):

            if individual_functionname in linelist[i]:
                if "*" in linelist[i-1]:
                    return True
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
        print("Inside check_pointer_return cannot open "+ individual_functionname)
        return True
        
def check_same_block_id (linelistz3) :
    for i in range(len(linelistz3)):
        if "ite constraint" in linelistz3[i]:
            try:
                #print(linelistz3[i])
                blockid1 = re.search("ite constraint_block_(.+?) block_(.+?) block_(.+?) \)",linelistz3[i]).group(2)
                blockid2 = re.search("ite constraint_block_(.+?) block_(.+?) block_(.+?) \)",linelistz3[i]).group(3)
                #print(blockid1)
                #print(blockid2)
                if blockid1 == blockid2 :
                    return True
            except:
                pass
    return False
    
def write_log_to_file(fout,linelistdiff,linelistz3,filename):
    wrapper_functions_list = ["dirfd","getpagesize"]
    whole_functionname = re.search('(.+?)_z3',filename).group(1)
    #print(whole_functionname)
    '''
    filename_forfile = "Unknown"
    for name in os.listdir(directname_originalclang):
        if (whole_functionname[:len(name)] == name):
            filename_forfile = name
            break
    #print(filename)
    directname_function_folder= os.path.join(directname_function_big_folder,filename_forfile+"_folder")
    directname_function_content = os.path.join(directname_function_folder,whole_functionname+".c")
    individual_functionname = whole_functionname[len(name)+1:]
    '''
    filename_forfile = "Unknown"
    print(whole_functionname)
    os.system("find ./test_muqi/generated_function_c/project_folder/ -name " + whole_functionname+".c > temp_found_file.txt")
    f_file = open("temp_found_file.txt",'r')
    linelist = f_file.readlines()
    f_file.close()
    print(linelist)

    print(whole_functionname+"_modified.c")
    os.system("find /home/muqi/pthread_Angr_Prompt/test_muqi/generated_function_c/project_folder/ -name " + whole_functionname+"_modified.c > temp_found_file_ghidra.txt")
    f_file_ghidra = open("temp_found_file_ghidra.txt",'r')
    linelist_ghidra = f_file_ghidra.readlines()
    f_file_ghidra.close()
    print(linelist_ghidra)

    if len(linelist) > 0:
        directname_function_content = linelist[0][:-1]
    else:
        return

    if len(linelist_ghidra) > 0:
        directname_function_content_ghidra = linelist_ghidra[0][:-1]
    else:
        return


    if whole_functionname not in directname_function_content:
    	print("ERROR!!! "+ whole_functionname +" is not in: "+ directname_function_content)
    filename_forfile = re.search('./test_muqi/generated_function_c/project_folder/(.+?)_folder',directname_function_content).group(1)
    individual_functionname = whole_functionname[len(filename_forfile)+1:]
    
    if individual_functionname in wrapper_functions_list :
        return

    #'''
    print_or_not = check_void(directname_function_content,individual_functionname) or check_pointer_return(directname_function_content,individual_functionname) or check_double (directname_function_content,individual_functionname) or check_same_block_id (linelistz3) 
    #print_or_not = check_void(directname_function_content,individual_functionname) or check_pointer_return(directname_function_content,individual_functionname) or check_double (directname_function_content,individual_functionname) 
    
    #print_or_not = check_void(directname_function_content,individual_functionname)
    #print_or_not = False

    #if (check_double(directname_function_content,individual_functionname) == False):
    #    fout.write(filename +"is relaed with double\n")

    if (print_or_not == False):
        fout.write(filename+" is wrong: \n")
        fout.write("in diff: \n")
        for i in range(len(linelistdiff)):
            fout.write(linelistdiff[i])
        fout.write("\n")
        function_name = os.path.join(directname_regenerated_function_list,filename_forfile)
        fout_functionname = open(function_name,'a')
        fout_functionname.write(individual_functionname+"\n")
        fout_functionname.close()
        os.system("cp "+directname_function_content+" ./problematic_modefied_c")
    
    #'''
    os.system("cp "+directname_function_content+" ./angr_modefied_c")
    os.system("cp "+directname_function_content_ghidra+" ./ghidra_modefied_c")
    '''
    fout.write("in z3: \n")
    for i in range(len(linelistz3)):
        fout.write(linelistz3[i])
    '''
def main():
    #'''
    os.system("rm "+ output_diff)
    fout = open(output_diff,'a')
    
    os.system("cp "+directname_function_list+"/* " + directname_regenerated_function_list)
    for function_file in os.listdir(directname_regenerated_function_list):
        function_file_path  = os.path.join(directname_regenerated_function_list,function_file)
        function_file_pathin = open(function_file_path,'r')
        linelistfilename = function_file_pathin.readlines()
        function_file_pathin.close()
        print(function_file_path)
        
        function_file_pathout = open(function_file_path,'w')
        if len(linelistfilename) > 0 :
            #now we do not need the first function to seperate base file any more
            #function_file_pathout.write(linelistfilename[0])
            pass
        else :
            print("---------delete this:"+function_file_path)
            os.system("rm "+ function_file_path)
        function_file_pathout.close()
    
    for filename in os.listdir(directname_diff):
        fdiffpath  = os.path.join(directname_diff,filename)
        fdiffin = open(fdiffpath,'r')
        linelistdiff = fdiffin.readlines()
        fdiffin.close()
        
        fz3path = os.path.join(directname_z3,filename)
        fz3in = open(fz3path,'r')
        linelistz3 = fz3in.readlines()
        
        if len(linelistdiff) > 1 :
            write_log_to_file(fout,linelistdiff,linelistz3,filename)
        elif len(linelistdiff) == 0 :
            pass
            #fout.write(filename+" is wrong: \n")
            #fout.write("no content in diff!! mainly because z3 runs overtime \n\n")
        else :
            if 'unsat' == ("xxxxx"+filename)[-5:]:
                try:
                    cond = linelistdiff[0][0:5] == 'unsat'
                except:
                    write_log_to_file(fout,linelistdiff,linelistz3,filename)
            else :
                try:
                    cond = linelistdiff[0][0:3] == 'sat' 
                except:
                    write_log_to_file(fout,linelistdiff,linelistz3,filename)
            if cond == True:
                write_log_to_file(fout,linelistdiff,linelistz3,filename)
            #if cond != True:
            #    write_log_to_file(fout,linelistdiff,linelistz3,filename)
    
    fout.close()
    #'''

    for function_file in os.listdir(directname_regenerated_function_list):
        function_file_path  = os.path.join(directname_regenerated_function_list,function_file)
        function_file_pathin = open(function_file_path,'r')
        linelistfilename = function_file_pathin.readlines()
        function_file_pathin.close()
        
        if len(linelistfilename) > 0 :
            pass
        else :
            print("---------delete this:"+function_file_path)
            os.system("rm "+ function_file_path)
        
    
if __name__ == "__main__":
    main()


