import os
import sys
import math
import re

directname_diff = "./test_muqi/diff"
directname_z3 = "./test_muqi/z3"
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

direname_original_all = "./test_muqi/originalclang_all_folders/"
dirname_count_hash = {}

def write_log_to_file(fout,linelistdiff,linelistz3,filename):
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
    directname_function_content = linelist[0][:-1]
    if whole_functionname not in directname_function_content:
    	print("ERROR!!! "+ whole_functionname +" is not in: "+ directname_function_content)
    filename_forfile = re.search('./test_muqi/generated_function_c/project_folder/(.+?)_folder',directname_function_content).group(1)
    individual_functionname = whole_functionname[len(filename_forfile)+1:]
    

    for dirname in os.listdir(direname_original_all):
        if "py" in dirname :
            continue
        for filename_temp in os.listdir(direname_original_all+dirname):
            if filename_temp == filename_forfile :
                dirname_count_hash[dirname] += 1
                break


    print_or_not = check_void(directname_function_content,individual_functionname) or check_pointer_return(directname_function_content,individual_functionname) or check_double (directname_function_content,individual_functionname) or check_same_block_id (linelistz3) 
    #print_or_not = check_void(directname_function_content,individual_functionname) or check_pointer_return(directname_function_content,individual_functionname) or check_double (directname_function_content,individual_functionname) 
    
    #print_or_not = check_void(directname_function_content,individual_functionname)
    #print_or_not = False
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
    '''
    fout.write("in z3: \n")
    for i in range(len(linelistz3)):
        fout.write(linelistz3[i])
    '''
def main():
    #'''
    os.system("rm "+ output_diff)
    fout = open(output_diff,'a')
    
    for dirname in os.listdir(direname_original_all):
        if "py" in dirname :
            continue
        dirname_count_hash[dirname] = 0

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
        print("in directname_diff")
        print(filename)
        fdiffpath  = os.path.join(directname_diff,filename)
        fdiffin = open(fdiffpath,'r')
        linelistdiff = fdiffin.readlines()
        fdiffin.close()
        
        fz3path = os.path.join(directname_z3,filename)
        fz3in = open(fz3path,'r')
        linelistz3 = fz3in.readlines()
        
        if len(linelistdiff) > 1 :
            print(">1"+filename)
            write_log_to_file(fout,linelistdiff,linelistz3,filename)
        elif len(linelistdiff) == 0 :
            fout.write(filename+" is wrong: \n")
            fout.write("no content in diff!! mainly because z3 runs overtime \n\n")
        else :
            print("else:"+filename)
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
            if cond != True:
                    write_log_to_file(fout,linelistdiff,linelistz3,filename)
    
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
        
    print(dirname_count_hash)
if __name__ == "__main__":
    main()


