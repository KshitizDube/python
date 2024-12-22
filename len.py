capital_of_Romania = input("What is the capital of Romania ? ")
capital_of_Bharat = input("What is the capital of Bharat ? ")
print("the capital of Romania is " + capital_of_Romania)
print("the capital of Bharat is " + capital_of_Bharat)
len_of_capital_of_rom = len(capital_of_Romania)
len_of_capital_of_bha =len(capital_of_Bharat)
print(len_of_capital_of_rom)
print(len_of_capital_of_bha)
if len_of_capital_of_rom > len_of_capital_of_bha:
    print(capital_of_Romania + " has more letters !!! ")
elif len_of_capital_of_rom == len_of_capital_of_bha:
    print(capital_of_Romania + " " + capital_of_Bharat + " both have the same amount of letters 😊😒😂 ")
else:
    print(capital_of_Bharat + " has more letters !!! ")