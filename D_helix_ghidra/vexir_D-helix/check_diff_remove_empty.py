import os
import sys
import math
import re

directname_regenerated_function_list = "./regenerate../function_name_original"
def main():    
    for function_file in os.listdir(directname_regenerated_function_list):
        function_file_path  = os.path.join(directname_regenerated_function_list,function_file)
        function_file_pathin = open(function_file_path,'r')
        linelistfilename = function_file_pathin.readlines()
        function_file_pathin.close()
        print(function_file_path)
        if len(linelistfilename) == 1 :
            os.system("rm "+ function_file_path)
    
    
if __name__ == "__main__":
    main()

