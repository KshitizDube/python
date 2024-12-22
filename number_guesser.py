import random
print("Hi welcome to the game, This is a number guessing game.\nYou got 7 chances to guess the number. Let's start the game")
input1 = int(input("Please enter the range : "))
num_to_guess = random.randrange(input1)
chances = 7
guess_counter = 0
while guess_counter < chances:
    guess_counter+=1
    my_guess = int(input("Please Enter your Guess : "))
    if my_guess == num_to_guess:
        print(f"congrats you guesed the number 👍😊😊😀😁😆😉😊😋😎☺️🙂 it was {num_to_guess} in {guess_counter} attempt")

        break

    elif guess_counter >= chances and my_guess != num_to_guess:
        print(f"Oops sorry, The number is {num_to_guess} better luck next time")

    elif my_guess > num_to_guess:
        print("Your guess is higher ")

    elif my_guess < num_to_guess:
        print("Your guess is lesser")
