#Building a guessing game with additional functions
#Ask player if he would like to play the game
#Provide a clue when the guess is wrong
#Ensure that player only have 3 guesses
print("Would you want to play the guessing game?")
choice = "\n"

while choice != "N":

    choice = input("Enter Y/N to play game: ").upper()
    if choice == "Y":

        secret_word = "LION"
        guess = "\n"
        guess_count = 0
        guess_limit = 3
        out_of_guesses = False

        while guess != secret_word and not(out_of_guesses):
            if guess_count < guess_limit:
                guess = input("Guess the secret word: ").upper()
                guess_count += 1
                if guess != secret_word:
                    print("Clue: It is an animal.")
            else:
                out_of_guesses = True
        if out_of_guesses:
            print("Out of Guesses, YOU LOSE!\n")
        else:    
            print("You win!\n")
    else:
        if choice != "N" or choice != "Y":
            print("Enter again.")       
print("Bye~ You have exited the game.")