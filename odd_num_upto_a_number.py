num_input = int(input("Give us a number "))
odd_num = []
for i in range(num_input):
    j=i+1
    if j % 2 == 1:
        odd_num.append(j)
print(f"These are the odd numbers{odd_num}")