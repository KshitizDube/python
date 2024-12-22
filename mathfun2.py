table = int(input("what is your number "))
for num in range(1,31) :
    if num % table == 0:
        continue
    print(num)


