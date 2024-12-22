# numbers =[1,4,2,5,3,4,6,2,7,5,4,9,4,4,7,3]
# for number in numbers :
#     if number == 4 :
#         print(number)
#     else:
#         print("there are only 11 not four numbers")

number = [ 1,9,3,9,0,2,8,9,0,4,8,9,3,8,5,9,7,8,4,7,9,2,8,7,6 ]
for num in number :
    if (num) % 2 == 0:
        print(str(num) + " is even")
    else:
        print(str(num )+ ' is odd')
