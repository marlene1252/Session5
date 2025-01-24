# you have 3 lives. I roll the dice. If I roll 6, you win
# if not a 6, you lose 1 life

from random import randint

lives = 3
while lives > 0:
    roll = randint(1,6) #make sure not to put a: and b"
    if roll == 6:
        print("You rolled a 6, you win!")
        break # this exists the while even if lives still > 0
        # there is no other way to get here, unless i DID NOT roll a 6
    print(f"You rolled a {roll}! You lose a life")
    lives -=1
    print(f"Live left: {lives}")
else: # else from while
    print("You lost!")

