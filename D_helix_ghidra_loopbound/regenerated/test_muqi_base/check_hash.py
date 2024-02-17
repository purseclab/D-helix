f = open("./rules_sub_v1","r")
line = f.readlines()
f.close()
list_1 = []
for i in range(len(line)):
    list_1.append(line[i])

print(len(set(list_1)))

