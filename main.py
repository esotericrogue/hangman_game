import random

path = "/home/odin/Desktop/words.txt"

with open(path, "rb") as file:
    words = file.read().decode("utf-8").splitlines()

guessed_letters = []
words_easy = [word for word in words if len(word) > 5 and len(word) <= 10]

words_hard = [word for word in words if len(word) > 10]

random_easy_word = random.choice(words_easy)
easy_word_length = len(random_easy_word)

random_hard_word = random.choice(words_hard)
hard_word_length = len(random_hard_word)

stages = [
    " O\n/|\\\n/\\",
    " O\n/|\\\n/",
    " O\n/|\\",
    " O\n/|",
    " O\n |",
    " O",
]

lives = 5
difficulty = input("Easy or Hard: ")

if difficulty.lower() == "easy":
    hangman_word = [random_easy_word[0]] + ["_"] * (len(random_easy_word) - 2) + [random_easy_word[-1]]
    while lives != 0:
        print("".join(hangman_word))

        letter = input("letter: ")

        if letter in random_easy_word:
            for idx, char in enumerate(random_easy_word):
                if char == letter:
                    hangman_word[idx] = letter
        else:
            guessed_letters.append(letter)
            if letter in guessed_letters:
                print("You already guessed this letter!")

            lives -= 1
            print(stages[lives])
            print(f"Incorrect! You have {lives} lives left.")

            if lives == 0:
                print("You Lost! The word was: " + random_easy_word)
                break
        if "".join(hangman_word) == random_easy_word:
            print("Congratulations! You Won! \nThe word was: " + random_easy_word)
            break

elif difficulty.lower() == "hard":
    hangman_word = [random_hard_word[0]] + ["_"] * (len(random_hard_word) - 2) + [random_hard_word[-1]]
    while lives != 0:
        print("".join(hangman_word))

        letter = input("letter: ")

        if letter in random_hard_word:
            for idx, char in enumerate(random_hard_word):
                if char == letter:
                    hangman_word[idx] = letter
        else:
            lives -= 1
            print(stages[lives])
            print(f"Incorrect! You have {lives} lives left.")

            if lives == 0:
                print("You Lost! The word was: " + random_hard_word)
                break
        if "".join(hangman_word) == random_hard_word:
            print("Congratulations! You Won! \n The word was: " + random_hard_word)
            break
elif difficulty.lower() != "hard" or difficulty.lower() != "easy":
    print("Please type easy or hard!")