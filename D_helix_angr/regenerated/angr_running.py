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
os.system("rm /tmp/call_count_angr_numargs.txt")
filepath_originalclang = sys.argv[1]
required_function = sys.argv[3]
p = angr.Project(filepath_originalclang,auto_load_libs=False, load_debug_info=True)
#p = angr.Project(filepath_originalclang)
pcfg = p.analyses[CFGFast].prep()(normalize=True, data_references=True)
p.analyses[angr.analyses.CompleteCallingConventionsAnalysis].prep()(recover_variables=True,analyze_callsites=True)
required_address = p.loader.find_symbol(required_function).rebased_addr


'''
arg1 = claripy.BVS('angr_arg1',8*8)
arg2 = claripy.BVS('angr_arg2',8*8)
#arg1 = angr.PointerWrapper(arg1)

#print(hex(required_address))
#state = p.factory.call_state(required_address,arg1,add_options={angr.options.ZERO_FILL_UNCONSTRAINED_MEMORY,angr.options.ZERO_FILL_UNCONSTRAINED_REGISTERS},remove_options=angr.options.simplification)
state = p.factory.call_state("/tmp/test_angr.txt",required_address,arg1,arg2,add_options={angr.options.CALLLESS,angr.options.ZERO_FILL_UNCONSTRAINED_MEMORY,angr.options.ZERO_FILL_UNCONSTRAINED_REGISTERS},remove_options=angr.options.simplification)
#state = p.factory.call_state(required_address,arg1,arg2,add_options={angr.options.ZERO_FILL_UNCONSTRAINED_MEMORY,angr.options.ZERO_FILL_UNCONSTRAINED_REGISTERS},remove_options=angr.options.simplification)

sm = p.factory.simulation_manager(state)
print("|||||||||||||||||||||||||||||")
for function in p.kb.functions:
   func_name = pcfg.functions.get(function).name
   print("111111")
   print(func_name)
   if func_name == required_function :
      print( func_name)
      #print(pcfg.functions.get(function).jumpout_sites[0])
      #print(hex(list(pcfg._get_jumpout_targets(pcfg.functions.get(function)))[0]))
      print(list(pcfg._get_jumpout_targets(pcfg.functions.get(function))))
      sm.input_jumpout_edge(list(pcfg._get_jumpout_targets(pcfg.functions.get(function))))

abort_address = []
for function in p.kb.functions:
   func_name = pcfg.functions.get(function).name
   if func_name == "abort" :
      print(pcfg.functions.get(function))
      abort_address.append(pcfg.functions.get(function).addr)

sm.input_abort_edge(abort_address)

print(abort_address)
print(type(sm))

#sm.use_technique(angr.exploration_techniques.LoopSeer(cfg=pcfg, functions=[required_function],bound=2,use_header = True))
#sm.use_technique(angr.exploration_techniques.LoopSeer(cfg=pcfg, functions=[required_function],bound=1))
os.system("rm /tmp/test_angr.txt")
os.system("rm /tmp/call_count_angr_args.txt")

sm.run()
print("finished sm run")
'''

