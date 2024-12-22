name = input("what is your name ? ")
vowels = ["a","e","i","o","u"]
count_v = 0
consonent = 0
for letters in name :
    if letters in vowels:
        count_v = count_v + 1
    else :
        consonent = consonent + 1
print("name has ",count_v,"vowels")
print("name ha s",consonent,"consonent")