temp = input("what is the temperature ")
unit = temp[-1].lower()
value = int(temp[:-1])
if unit == "f" :
    print("your answer in celcius ",(value - 32) * 5/9)
else:
    formula = (value * 9/5) + 32
    print(formula)
