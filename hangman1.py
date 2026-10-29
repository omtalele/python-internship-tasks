import random

# List of words
words = ["python", "computer", "student", "program", "science"]

# ASCII Hangman stages
hangman_art = [
    """
     -----
     |   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
    =========
    """
]


def play_hangman():
    word = random.choice(words)
    guessed_letters = set()
    wrong_guesses = 0
    max_attempts = 6

    print("Welcome to Hangman Word Guessing Game!")

    while wrong_guesses < max_attempts:
        print(hangman_art[wrong_guesses])

        # Display hidden word
        display_word = " ".join(
            letter if letter in guessed_letters else "_"
            for letter in word
        )
        print("Word:", display_word)
        print("Guessed letters:", sorted(guessed_letters))
        print("Attempts left:", max_attempts - wrong_guesses)

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word:", word)
            return

        guess = input("Guess a letter: ").lower().strip()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one letter.")
            continue

        # Prevent duplicate guesses
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct guess!")
        else:
            wrong_guesses += 1
            print("Wrong guess!")

    print(hangman_art[wrong_guesses])
    print("Game Over! The word was:", word)


if __name__ == "__main__":
    play_hangman()
