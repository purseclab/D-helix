import os
import sys
import math
import re

directname_diff = "./test_muqi/diff"
directname_z3 = "./test_muqi/z3"
output_diff = "./diff_result"
directname_originalclang = "./test_muqi/originalclang"
directname_function_big_folder= "./test_muqi/generated_function_c/project_folder"

def check_void(functionname):
    #print(filename)
    whole_functionname = re.search('(.+?)_z3',functionname).group(1)
    #print(whole_functionname)
    filename = "Unknown"
    for name in os.listdir(directname_originalclang):
        if (whole_functionname[:len(name)] == name):
            filename = name
            break
    #print(filename)
    directname_function_folder= os.path.join(directname_function_big_folder,filename+"_folder")
    directname_function_content = os.path.join(directname_function_folder,whole_functionname+".c")
    individual_functionname = whole_functionname[len(name)+1:]
    #print(individual_functionname)
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
    
    

def write_log_to_file(fout,linelistdiff,linelistz3,filename):
    print_or_not = check_void(filename)
    if (print_or_not == False):
        fout.write(filename+" is wrong: \n")
        fout.write("in diff: \n")
        for i in range(len(linelistdiff)):
            fout.write(linelistdiff[i])
        fout.write("\n")
    '''
    fout.write("in z3: \n")
    for i in range(len(linelistz3)):
        fout.write(linelistz3[i])
    '''
def main():
    os.system("rm "+ output_diff)
    fout = open(output_diff,'a')
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
            fout.write(filename+" is wrong: \n")
            fout.write("no content in diff!! how can that be possible \n\n")
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
            if cond != True:
                    write_log_to_file(fout,linelistdiff,linelistz3,filename)
    
    fout.close()
    
    
if __name__ == "__main__":
    main()


