# D-Helix: A Generic Decompiler Testing Framework Using Symbolic Differentiation
D-HELIX is a generic decompiler testing framework that can automatically vet the decompilation correctness on the function level.
### SYMDIFF:
To run SYMDIFF, D-helix asks for two patched components: angr and prompt.
#### Install/patch angr:
Here is the commit version of each component in angr, if you want P-code as IR:
<details>
angr-dev: 0578f015c68319b634cb7246d71184431563bd10<br>
admin: 0578f015c68319b634cb7246d71184431563bd10<br>
ailment: bef6268dd3d4ea9c251fd24f8a301375771d9dd7<br>
angr: 02a3fefbfa4fef67f039ef3027896a251779fff2<br>
angr-management: 5b4200e4ca33fb16680aef0de861624b226123a6<br>
archinfo: b150db4c0a939140966df8b0056b6deb5b07efbf<br>
archr: 6f6a39b98466f9303eef72d02e0fe6e64195b3e3<br>
binaries: 2bf0bd4f62951be0394432e794ba64d90a362371<br>
claripy: 36c640346a822a1950ca43d6d75678e33c731832<br>
cle: 3909a5ffdb1d4126e0ef359e8013e79350b12a92<br>
pysoot: d08dc569ec35796ccea5509b3e04b74967bcfd48<br>
monkeyhex: 2718ae888d05c0827af3aca9bb46d25f773edfc2<br>
mulpyplexer: 2f3c8761650b09a1ff8a14ef64c346ec0b610b42<br>
pyvex: a4aef1c12277860253541501f4604101dc507916<br>
vex: 0feb7ff984340d738b37543a817f2e3b436e26ee<br>
</details>
Here are the commit version of each components in angr, if you want Vex IR as IR:
<details>
angr-dev: b2198226e6194310c57a4b50ae9a6c82b1b6cd7f<br>
admin: b2198226e6194310c57a4b50ae9a6c82b1b6cd7f<br>
ailment: cb3205ffcb182632840d9b745a8f42b5d259a4b6<br>
angr: 6ef773615ff70c5c334ee16945e22e9005a8c82d<br>
angr-management: 474e7325ac4b2b649a3149d156c34c68d8839f17<br>
archinfo: 4eea2b81e78a2d902d6c7c0ff7168b304b9d3b8c<br>
archr: 28a92b3e72c2791eb9a77549ff91f3c4a5840c0e<br>
binaries: ee16a9bcfde2edf039100e38726f27ba649d89de<br>
claripy: 91518043156fc317195a577a6c8b41763c138577<br>
cle: 7024cd3fc479af221cc3070b0ddca1ac20ca1a22<br>
pypy: b2198226e6194310c57a4b50ae9a6c82b1b6cd7f<br>
pyvex: de7f92e126fbbaa61287e2a647be6f2871d56032<br>
</details>
After checkout the corresponding commit in angr, you may patch angr and claripy using different patch files. We currently only support loop-bound and external function call features specified in design 4.2.1 for Vex IR.
After patching, copy muqi.py to the following directory:
` ./angr-dev/angr/angr`

#### Install/patch prompt:
To install prompt, you need to install clang-3.8 first.
After that, clone prompt from: `https://github.com/sysrel/PROMPT `.
We build our prompt using the following commands:
<details>
export LLVM_CONFIG=/home/muqi/llvm-3.8/llvm-src/build/bin/llvm-config <br>
cmake     	-DENABLE_TCMALLOC=ON     	-DENABLE_POSIX_RUNTIME=ON     	-DENABLE_KLEE_UCLIBC=ON     	-DKLEE_UCLIBC_PATH=/home/muqi/klee-uclibc     	-DENABLE_SOLVER_Z3=ON     	-DENABLE_SOLVER_STP=OFF     	-DENABLE_SOLVER_METASMT=OFF     	-DENABLE_UNIT_TESTS=OFF -DENABLE_POSIX_RUNTIME=ON -DENABLE_KLEE_UCLIBC=ON -DLLVM_CONFIG_BINARY=/home/muqi/llvm-3.8/llvm-src/build/bin/llvm-config -DLLVMCC=/home/muqi/llvm-3.8/llvm-src/tool/clang/cfe-3.8.0.src/build/bin/clang -DLLVMCXX=/home/muqi/llvm-3.8/llvm-src/tool/clang/cfe-3.8.0.src/build/bin/clang++ ../ 
</details>
Finally, use different prompt_diff*.patch to patch the prompt for different purpose.

We use Z3 with version 4.9.1 - 64 bit.

#### Run SYMDIFF:
After putting the binary D_helixxxx/test_muqi/originalclang, we run SYMDIFF by calling 'python generate_symbolic.py' in each D_helixxxx folder (For D_helix_ghidra, go into subdirectories named pcode_D-helix/vexir_D-helix). Before running, make sure: 
1. angr environment is correctly set.
2. the clang compiler/ghidra/ghidra scripts folder address in generate_symbolic.py is correct.<br>
Note, to enable the loop-bound feature in angr, uncomment the setting for 'loop_bound_cond' in 'angr/engines/vex/heavy/heavy.py'.
After symbolic models are generated, run 'python check_diff.py' to generate the report for inaccuracies.
The result of SYMDIFF will be shown in a file named diff_result.

### Tuner:
#### Patch Ghidra:
You may patch Ghidra using ghidra_diff.patch with the following Ghidra commit:
15d22e81643f4647fc2b985f61e44d9cdcee15da. <br>
Or you may download the latest Ghidra. And to disable heuristics in Ghidra, you may follow our method for 'Rule *rl;' in Ghidra/Features/Decompiler/src/decompile/cpp/action.cc.
#### Run Tuner:
Before running tuner, make sure the inaccuracies detected from SYMDIFF is reported by running 'python check_diff.py'. After that, run 'python regenerated_inall.py' in subdirectory regenerated.
The result of Tuner will be shown in a directory called correct_result.
