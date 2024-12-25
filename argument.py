import sys
print(sys.argv)
length = len(sys.argv)
syss = sys.argv
add = 0
for i in range(1,length):
    add = add + int(syss[i])
print(add)