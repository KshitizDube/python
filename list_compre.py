# list1 = ["hello","bat","ball","mine","number"]
# list2 = []
# for i in list1:
#     if "b" not in i:
#         list2.append(i)
# print(list2)
inputt = int(input("how many words do you wnat to give "))
# list2 =[]
# for i in range(inputt):
#     intt = input("pls input your word ")
#     list2.append(intt)
# print(list2)
list2 =[input("pls input your word ") for i in range(inputt) ]
print(list2)