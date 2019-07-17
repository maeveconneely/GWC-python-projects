from random import *

words = ["sausage", "banana", "chicken", "cookie", "chips", "ice cream", "apple",
         "pineapple", "mango", "celery", "cucumber", "carrot", "pie", "cake",
         ""]
aRandomindex = randrange(0, len(words))
word = words[aRandomindex]
print()

# gets rid of repeating letters
no_repeats = ""
for i in word:
    if (i not in no_repeats and i != " "):
        no_repeats += i

# creates a list as long as the word with just _
current_guessed_word = []
for i in range(len(word)):
    if (word[i] != " "):
        current_guessed_word.append("_")
    else:
        current_guessed_word.append(" ")

tries = 7
guesses = []
correct_guesses = 0
while tries > 0:
    string_word = ""
    for i in current_guessed_word:
        string_word += i + " "

    print("Current letters guessed:", string_word, " ", end="")
    letter = input("Guess a letter: ")

    # check if user already guessed letter
    if (letter in guesses):
        print("You already guessed this letter! try again.")
        continue

    # adds the letter to the list of guesses
    guesses.extend(letter)

    # if the letter in in the word
    if (letter in no_repeats):
        correct_guesses += 1
        print("Correct! tries remaining:", tries, end="\n\n")

        # adds the index of the letter in the original word to the
        #  list
        indexes_of_letter = []
        # jana
        # 0123
        # len(jana) is 4
        #        range(4)
        #        range makes i 0, 1, 2, 3
        for i in range(len(word)):
            if (letter == word[i]):
                indexes_of_letter.append(i)

        # adds the word to the list in order of guessed letters
        # [1, 3]
        for i in indexes_of_letter:
            current_guessed_word[i] = letter

        # if they user guessed all of the letters
        if (correct_guesses == len(no_repeats)):
            print("You guessed the word! Word:", word)
            break
        continue


    tries -= 1
    print("Tries remanining:", tries, end="\n\n")

if (tries == 0):
    print("You ran out of guesses :(! The word was", word)
