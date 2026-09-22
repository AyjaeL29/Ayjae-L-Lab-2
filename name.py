import random

game_number = random.randint(1,10)
#print(game_number)
guess_count = 0
while(True):
    guess = int(input("Enter a number between 1 and 10"))
    guess_count += 1

    if guess > game_number:
        print("Too high")

    elif guess < game_number:
        print("Too low")
    else:
        guess_word = "guess" if guess_count == 1 else "guesses"
        print(f"You win! It took you {guess_count} {guess_word}.")
        if guess_count <= 3:
            print("Great job! You guessed it quickly!")
        else:
            print("That took a while. You need to practice your guessing!")
        break