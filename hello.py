from random import randint
x = randint(1,100)
guesscount = 10
while guesscount > 0:
    inp = int(input("Guess a Number 1-100: "))
    if guesscount > 0:
        if inp != x:
            guesscount = guesscount - 1
            print(f"Wrong guess! You have {guesscount} guesses remaining!")
            if inp > x:
                print(f"The number is lower than {inp}!")
            elif inp < x:
                print(f"The number is higher than {inp}!")
        else:
            print(f"Congratulations! You got the number in {10 - guesscount} guesses!")
            guesscount = 0
    else:
        print("You have no guesses remaining! Please restart")