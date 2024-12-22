import secrets
import string
try:
    print("this is a pasword generator machine")
    lenght_pasword = int(input("Can you pls tell me the lenght of the pasword you want: "))
    alphabet = string.ascii_letters + string.digits + string.punctuation + string.hexdigits + string.octdigits
    password = ''
    if 1 <= lenght_pasword <= 3:
        print("Your pasword is going to be too easy to guess")
    else:
        for i in range(lenght_pasword):
            password = password + secrets.choice(alphabet) 
    print(password)
except:
    print("the input should only be integer")
