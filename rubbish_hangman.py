from random import randrange

word_list = ["applesauce", "quixotic", "bumblebee", "station", "charmer", "loveliness", "python", "programmer", "train", "railway", "sleeper", "dream", "habit", "rivet", "recur", "situation", "conjuring", "pennant", "rout", "libel", "cellar", "seats", "hatred", "love", "jazz", "buzz", "fizz", "stigma", "appear", "basic", "thorn", "grocer", "conifer", "object", "armada"]

hidden_word = word_list[randrange(len(word_list))]

guessed_letters = []

guesses_remaining = 10

def generate_display():
    display_string = ""
    for letter in hidden_word:
        if letter in guessed_letters:
            display_string = display_string + letter
        else:
            display_string = display_string + "*"
    return display_string

def ingame_display():
    print("Hidden word: ", generate_display())
    if len(guessed_letters) > 0:
        print("You've guessed:", guessed_letters)
    print("Guesses remaining:", guesses_remaining)
    print()

def take_input():
    ##get the input
    global guesses_remaining
    user_input = input("Enter a character: ")
    user_input = user_input.lower()

    ##check it's valid and convert to lower before adding to list
    while user_input.lower() in guessed_letters or not user_input.isalpha() or not len(user_input) == 1:
    #do some if statements here to give a bespoke message for each condition
        user_input = input("Either you've already chosen that, or it's not a single alphabetic character!\nPick again:")
        user_input = user_input.lower()
    guessed_letters.append(user_input)

    ##check if it's in the word
    if not user_input in hidden_word:
        guesses_remaining -= 1
        print()
        print("Sorry, that's not there.")
        print()
    if user_input in hidden_word:
        print()
        print("That's right!")
        print()


#program starts here
print("Welcome to Coops's rubbish hangman game! Pick a letter to get started.")
print()
ingame_display()

while guesses_remaining > 0:
    if generate_display() != hidden_word:
        take_input()
        ingame_display()
    else:
        print("You got it! The hidden word was", hidden_word, ". Thanks for playing!")
        break
else:
    print("Sorry, out of guesses! The hidden word was", hidden_word)

print("")
print("GAME OVER")
