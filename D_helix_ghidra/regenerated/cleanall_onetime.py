import os
import sys
import math

directname_originalc = "./test_muqi/originalc"
directname_originalclang = "./test_muqi/originalclang"
directname_finishedclang = "./test_muqi/finishedclang"
directname_originalcfg = "./test_muqi/originalcfg"
directname_originalbc = "./test_muqi/originalbc"
directname_originalobject = "./test_muqi/originalobject"


directname_lifterbc = "./test_muqi/lifterbc"
directname_lifter_original_bc = "./test_muqi/lifteroriginalbc"
directname_lifterll = "./test_muqi/lifterll"
directname_lifterklee = "./test_muqi/lifterklee"

directname_globalvaraibles = "./test_muqi/global_variables"

directname_generatedc = "./test_muqi/generated_whole_c"
directname_generatedfunction_c_pro = "./test_muqi/generated_function_c/project_folder"
directname_generatedfunction_c_log = "./test_muqi/generated_function_c/log_for_compile"
directname_generatedbc = "./test_muqi/generatedbc"
directname_generatedll = "./test_muqi/generatedll"
directname_generatedklee = "./test_muqi/generatedklee"

directname_diff = "./test_muqi/diff"
directname_z3 = "./test_muqi/z3"
directname_functionname = "./function_name"
directname_functionaddress = "./function_address"

os.system("rm -r " + directname_originalclang + "/*")
os.system("rm -r " + directname_finishedclang + "/*")
os.system("rm -r " + directname_originalcfg + "/*")
os.system("rm -r " + directname_originalbc + "/*")
os.system("rm -r " + directname_originalobject + "/*")

os.system("rm -r " + directname_globalvaraibles + "/*")
os.system("rm -r " + directname_lifterbc + "/*")
os.system("rm -r " + directname_lifterll + "/*")
os.system("rm -r " + directname_lifterklee + "/*")
os.system("rm -r " + directname_lifter_original_bc + "/*")


os.system("rm -r " + directname_generatedfunction_c_pro + "/*")
os.system("rm -r " + directname_generatedfunction_c_log + "/*")
#os.system("rm -r " + directname_generatedc + "/*")
os.system("rm -r " + directname_generatedbc + "/*")
os.system("rm -r " + directname_generatedklee + "/*")
os.system("rm -r " + directname_generatedll + "/*")
os.system("rm -r " + directname_diff + "/*")
os.system("rm -r " + directname_z3 + "/*")
#os.system("rm -r " + directname_functionname + "/*")
os.system("rm -r " + directname_functionaddress + "/*")
