TAX_PARCENTAGE = 35
gross_salary = int(input("what is your salery ? "))
tax = (gross_salary * TAX_PARCENTAGE) / 100
if gross_salary > 10000 :
    amount = (gross_salary - tax)
    amount_tax = (amount * 10) / 100
    net_salary = (amount - amount_tax)
    print(net_salary)
else :
    net_salary = gross_salary - tax
    print(net_salary)
