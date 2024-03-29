import angr
import traceback
import claripy
import sys
from angr.analyses import (
    VariableRecoveryFast,
    CallingConventionAnalysis,
    CompleteCallingConventionsAnalysis,
    CFGFast,
    Decompiler,
)
from claripy.backends.backend_smtlib_solvers import *

filepath_originalclang = sys.argv[1]
required_function = sys.argv[3]
p = angr.Project(filepath_originalclang,auto_load_libs=False, load_debug_info=True)
#p = angr.Project(filepath_originalclang)
pcfg = p.analyses[CFGFast].prep()(normalize=True, data_references=True)

required_address = p.loader.find_symbol(required_function).rebased_addr


#'''
arg1 = claripy.BVS('angr_arg1',8*8)
arg2 = claripy.BVS('angr_arg2',8*8)
arg3 =  claripy.BVS('angr_arg3',8*8)
arg4 = claripy.BVS('angr_arg4',8*8)
arg5 = claripy.BVS('angr_arg5',8*8)
arg6 = claripy.BVS('angr_arg6',8*8)
arg7 = claripy.BVS('angr_arg7',8*8)
arg8 = claripy.BVS('angr_arg8',8*8)
arg9 = claripy.BVS('angr_arg9',8*8)
arg10 = claripy.BVS('angr_arg10',8*8)
arg11 = claripy.BVS('angr_arg11',8*8)

#arg1 = angr.PointerWrapper(arg1)

#print(hex(required_address))
#state = p.factory.call_state(required_address,arg1,add_options={angr.options.ZERO_FILL_UNCONSTRAINED_MEMORY,angr.options.ZERO_FILL_UNCONSTRAINED_REGISTERS},remove_options=angr.options.simplification)
state = p.factory.call_state("/tmp/test_angr.txt",required_address,arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8,arg9,arg10,add_options={angr.options.CALLLESS,angr.options.STRINGS_ANALYSIS,angr.options.ZERO_FILL_UNCONSTRAINED_MEMORY,angr.options.ZERO_FILL_UNCONSTRAINED_REGISTERS},remove_options=angr.options.simplification)
#state = p.factory.call_state(required_address,arg1,arg2,add_options={angr.options.ZERO_FILL_UNCONSTRAINED_MEMORY,angr.options.ZERO_FILL_UNCONSTRAINED_REGISTERS},remove_options=angr.options.simplification)

sm = p.factory.simulation_manager(state)
print("|||||||||||||||||||||||||||||")
for function in p.kb.functions:
   func_name = pcfg.functions.get(function).name
   if func_name == required_function :
      print( func_name)
      #print(pcfg.functions.get(function).jumpout_sites[0])
      #print(hex(list(pcfg._get_jumpout_targets(pcfg.functions.get(function)))[0]))
      print(list(pcfg._get_jumpout_targets(pcfg.functions.get(function))))
      sm.input_jumpout_edge(list(pcfg._get_jumpout_targets(pcfg.functions.get(function))))

'''
abort_address = []
for function in p.kb.functions:
   func_name = pcfg.functions.get(function).name
   if func_name == "abort" :
      print(pcfg.functions.get(function))
      abort_address.append(pcfg.functions.get(function).addr)

sm.input_abort_edge(abort_address)

print(abort_address)
print(type(sm))
'''
filename = "tac"
required_function = "rpl_re_match_2"

#'''
#sm.use_technique(angr.exploration_techniques.LoopSeer(cfg=pcfg, functions=[required_function],bound=2,use_header = True))
#sm.use_technique(angr.exploration_techniques.LoopSeer(cfg=pcfg, functions=[required_function],bound=1))
sm.run(read_args_txt ="/tmp/call_count_"+filename+"_angr_numargs.txt",
                call_count_path = "/tmp/call_count_"+filename+"_"+required_function+"_angr_args.txt")
print("finished sm run")
#'''

