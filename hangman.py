import random
import string

def game():
    choices = ["python", "java", "kotlin", "javascript"]
    tries = 8
    answer = random.choice(choices)
    hint = "-" * len(answer)
    guessed = set()

    print("H A N G M A N")

    while tries > 0:
        correct_guess = False
        valid_guess = False
        user_response = ""

        # Get guess until it is valid
        while not valid_guess:
            print()
            print(hint)

            user_response = input("Input a letter: ")
            if user_response in guessed:
                print("You already typed this letter")
                continue

            if len(user_response) != 1:
                print("You should input a single letter")
                continue

            if user_response not in string.ascii_lowercase:
                print("It is not an ASCII lowercase letter")
                continue

            valid_guess = True

        guessed.add(user_response)

        for j in range(len(answer)):
            if user_response == answer[j]:
                hint = hint[:j] + user_response + hint[j + 1:]
                correct_guess = True

        if not correct_guess:
            print("No such letter in the word")
            tries -= 1

        if answer == hint:
            break

    if hint == answer:
        print(f"You guessed the word {answer}!")
        print("You survived!")
    else:
        print("You lost!")

while True:
    user_play = input("Type 'play' to play the game, 'exit' to quit: ")
    if user_play == 'play':
        game()
    elif user_play == 'exit':
        break
