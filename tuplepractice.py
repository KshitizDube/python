# tuple12 =(11,[1112,345,67],"dtvgb",124,34)
# print(type(tuple12))
# tuple12 = tuple12[::-2]
# print(tuple12)
# print(tuple12[1][2])

tuple1 = input("what are your three numbers comma seprated ")
list =tuple1.split(",")
count_of_num = len(list)
sum_of_items = 0
for items in list:
    sum_of_items = sum_of_items +int(items)
average = sum_of_items / count_of_num
print(list)
print(average)

# tuple2 = input("what is your second number ")
# tuple3 = input("what is your thired number ")
# tuple4 = [tuple1,tuple2,tuple3]
