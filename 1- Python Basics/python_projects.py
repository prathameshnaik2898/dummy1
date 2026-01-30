import random

call = input("Roll a dice yes or no: ")

if call == "yes":
    random_integer = random.randint(1, 6)
    print(random_integer)
else:
    print("Thanks for playing")
