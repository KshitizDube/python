
import sys
# loop = int(input("who many stars do you want "))
loop = int(sys.argv[1])
for star in range(1,loop) :
    print("X " * star)
for stars in reversed(range(1,loop-1)) :
    print("X " * stars)