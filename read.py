f = open("family.txt")
a = f.read()
print(a)
if "SONAM VAJPAYEE" in a.upper() :
    print("Here is my moma")
else :
    print("where is my moma")