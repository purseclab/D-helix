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
p = angr.Project(filepath_originalclang,engine=angr.engines.UberEnginePcode)
#p = angr.Project(filepath_originalclang)
#angr_project = angr.Project(filepath_originalclang, engine=angr.engines.UberEnginePcode)
pcfg_angr = p.analyses.CFGFast(normalize = True)

#pcfg = p.analyses[CFGFast].prep()(normalize=True, data_references=True)
required_address = 0
try:
    required_address = p.loader.find_symbol(required_function).rebased_addr
except:
    os.system("llvm-objdump -t " +filepath_originalclang +">"+filepath_objdump)
    with open(filepath_objdump,'r') as objdump_file:
        objdump_lines = objdump_file.readlines()
        for i in range(len(objdump_lines)):
            if required_function in objdump_lines[i] :
                fullname_required_function = objdump_lines[i].split(" ")[-1]
                try:
                    required_address = p.loader.find_symbol(fullname_required_function[:-1]).rebased_addr
                except:
                    try:
                        required_address = int(objdump_lines[i].split(" ")[0],16)
                    except:
                        pass
                break

#'''
arg1 = claripy.BVS('angr_arg1',8*8)
arg2 = claripy.BVS('angr_arg2',8*8)
#arg1 = angr.PointerWrapper(arg1)

print(hex(required_address))


#state = p.factory.call_state(required_address,arg1,add_options={angr.options.ZERO_FILL_UNCONSTRAINED_MEMORY,angr.options.ZERO_FILL_UNCONSTRAINED_REGISTERS},remove_options=angr.options.simplification)
state = p.factory.call_state("/tmp/test_angr.txt",required_address,arg1,arg2,add_options={angr.options.CALLLESS,angr.options.ZERO_FILL_UNCONSTRAINED_MEMORY,angr.options.ZERO_FILL_UNCONSTRAINED_REGISTERS},remove_options=angr.options.simplification)
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

#'''
#sm.use_technique(angr.exploration_techniques.LoopSeer(cfg=pcfg, functions=[required_function],bound=2,use_header = True))
#sm.use_technique(angr.exploration_techniques.LoopSeer(cfg=pcfg, functions=[required_function],bound=1))
sm.run()
print("finished sm run")
#'''

