import random

words = ["java", "c", "python", "html", "css"]

while True:
    word = random.choice(words)
    guessed = ""
    tries = 6

    print("\nNew Game Started!")

    while tries > 0:
        fail = 0
        for letter in word:
            if letter in guessed:
                print(letter, end=" ")
            else:
                print("_", end=" ")
                fail += 1
        print()

        if fail == 0:
            print("You win! The word was:", word)
            break

        guess = input("Guess a letter: ")
        if guess == "stop":
            print("Thanks for playing!")
            exit()
        if guess in guessed:
            print("Already guessed.")
            continue

        guessed += guess

        if guess not in word:
            tries -= 1
            print("Wrong! Tries left:", tries)
            if tries == 0:
                print("Game over! The word was:", word)
