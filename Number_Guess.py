import random

top_of_range = input("Type a number: ")
if (top_of_range.isdigit()):
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Type a number greater than 0 ")
        quit()
else:
    print("Try next time")
    quit()

random_number = random.randint(0,top_of_range)
guesses = 0

while True:
    guesses += 1
    guess = input("Make a guess:")
    if guess.isdigit():
       guess=int(guess) 
    else:
        print("Pleases type a number next time")
    
    if random_number == guess:
        print("You got it Right!")
        break
    elif random_number <= guess:
        print("Try lower number")
    else:
        print("Try higher number")
        continue


print("You got it right in",guesses,"guesses")


