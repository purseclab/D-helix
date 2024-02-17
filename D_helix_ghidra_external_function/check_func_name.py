import os
import sys

directfuncname = "./function_name/libcrypto_so_3"
destination = "/home/muqi/pthread_Angr_Prompt/test_muqi/z3/"

fopen = open(directfuncname,'r')
function_names= fopen.readlines()
fopen.close()

for i in range(len(function_names)):
    funct_name = function_names[i][:-1]
    if "X509_PURPOSE_get_count" in funct_name :
        print(destination+"libcrypto_so_3_"+funct_name+"_z3")
    if os.path.isfile(destination+"libcrypto_so_3_"+funct_name+"_z3") == True or os.path.isfile(destination+"libcrypto_so_3_"+funct_name+"_z3_unsat") == True :
        #print(funct_name)
        print(destination+"libcrypto_so_3_"+funct_name)

