import os
import sys

directfuncname = "./function_count/"

count = 0
terminate_count = 0
wrapper = 0
not_terminate_count = 0
function_not_found = 0
multiple_symbol = 0
segment = 0
abort = 0
switch = 0
modefied_c_not_found = 0
log_klee_not_found = 0

for filename in os.listdir(directfuncname):
    fopen = open (directfuncname+filename,'r')
    counts = fopen.readlines()
    fopen.close()
    
    try:
        count += int(counts[0][:-1])
        terminate_count += int(counts[1][:-1])
        wrapper += int(counts[2][:-1])
        not_terminate_count += int(counts[3][:-1])
        function_not_found += int(counts[4][:-1])
        multiple_symbol += int(counts[5][:-1])
        segment += int(counts[6][:-1])
        abort += int(counts[7][:-1])
        switch += int(counts[8][:-1])
        modefied_c_not_found += int(counts[9][:-1])
        log_klee_not_found += int(counts[10][:-1])
        
        all_number = int(counts[1][:-1]) + int(counts[2][:-1])  + int(counts[3][:-1]) +  int(counts[5][:-1]) + int(counts[6][:-1]) + int(counts[7][:-1]) + int(counts[8][:-1])
        if all_number > 200  :
            print(filename)
            print(all_number)
            #print(int(counts[1][:-1]))
            #print(counts[9][:-1])
        '''
        print(int(counts[0][:-1]))
        print(int(counts[1][:-1]))
        print(int(counts[2][:-1]))
        print(int(counts[3][:-1]))
        '''
    except:
        pass
        #print(filename)
        #print(counts)

print("finally")
print(count)
print(terminate_count)
print(wrapper)
print(not_terminate_count)
print(function_not_found)
print(multiple_symbol)
print(segment)
print(abort)
print(switch)
print(modefied_c_not_found)
print(log_klee_not_found)
