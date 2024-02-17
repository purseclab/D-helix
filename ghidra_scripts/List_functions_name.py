from ghidra.app.decompiler import DecompileOptions
from ghidra.app.decompiler import DecompInterface
from ghidra.util.task import ConsoleTaskMonitor
import sys

args = getScriptArgs()
output = args[0]
with open(args[0], 'w') as f:
	print("argv[1] is " + args[0])
	func = getFirstFunction()
	while func is not None:
		print("Function: {} @ 0x{}".format(func.getName(), func.getEntryPoint()))    
		f.write("{}".format(func.getName()))
		f.write("\n")
		func = getFunctionAfter(func)

f.close()
