from random import randrange

number = randrange(0, 100, 1)


def guessing_game(guessed= list()) -> None:
   
    try:
        if (guess := int(input("Guess a number, it's between 0 and 100. " ))) != number:
            if guess not in guessed:
                guessed.append(guess)

            print(f"guesses you made: {guessed}")
            guessing_game(guessed)

        else:
            print("Congratulations you guessed the number! :D")

    except ValueError: 
        print("That was not a number! ")
        guessing_game(guessed)

guessing_game()
