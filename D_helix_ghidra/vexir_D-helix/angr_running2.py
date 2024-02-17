import angr
import traceback
import claripy
import sys
import os
from angr.analyses import (
    VariableRecoveryFast,
    CallingConventionAnalysis,
    CompleteCallingConventionsAnalysis,
    CFGFast,
    Decompiler,
)


directname_originalclang = "/home/muqi/pthread_Angr_Prompt/test_muqi/originalclang"
directname_objdump = "../test_muqi/objdump"


filename = sys.argv[1]
filepath_originalclang = os.path.join(directname_originalclang, filename)
filepath_objdump = os.path.join(directname_objdump, filename)
required_function = sys.argv[3]
p = angr.Project(filepath_originalclang,main_opts={'backend': 'blob', 'arch': 'arm'},auto_load_libs=False, load_debug_info=True)
#p = angr.Project(filepath_originalclang,main_opts={'backend': 'blob', 'arch': 'AARCH64'},auto_load_libs=False, load_debug_info=True)
#p = angr.Project(filepath_originalclang,auto_load_libs=False, load_debug_info=True)

#p = angr.Project(filepath_originalclang)
pcfg = p.analyses[CFGFast].prep()(normalize=True, data_references=True)

