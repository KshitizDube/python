city = input("please give me a name of a city : ")
city1 = len(city)
if city1 >= 10:
    print(f"your city name ({city}) is a hard city name to remember as it has {city1} letters")
else:
    print(f"looks like your city name ({city}) is quite a easy city name ot remember as it has only {city1} letters")