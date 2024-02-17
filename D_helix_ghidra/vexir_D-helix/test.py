import os

os.system('/home/muqi/PROMPT/build/bin/klee -prose-api-model=../test_muqi/model_prompt/modelmov_mov_read_dvcc_dvvc.txt --search=bfs --solver-backend=z3 --posix-runtime ../test_muqi/generatedbc/mov_mov_read_dvcc_dvvc.bc 1> 123 2>12345')
