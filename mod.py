import random
num = int(input("how many numbers do you want to print "))
even = []
odd = []
while num > 0 :
    ran = random.randint(1,100)
    if ran % 2 == 0 :
        even.append(ran)
    else :
        odd.append(ran)
    num = num - 1
print(odd)
print(even)