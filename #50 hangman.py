import random
words = ["happy", "hungry", "tired", "water", "book", "big", "hot", "cold", "open", "close"]
display = [
    """
     _____
    |     |
    |      
    |
    |
    |
""",
    """
     _____
    |     |
    |     O
    |
    |
    |
""",
    """
     _____
    |     |
    |     O
    |     |
    |
    |
""",
    """
     _____
    |     |
    |     O
    |    /|\
    |
    |
""",
    """
     _____
    |     |
    |     O
    |    /|\
    |    /
    |
""",
    """
     _____
    |     |
    |     O
    |    /|\
    |    / \
    |
"""
]

word_to_guess = random.choice(words)
word_length = len(word_to_guess)
remaining_attempts = 6
guessed_letters = []

print("Let's play Hangman!\n")

while remaining_attempts > 0:
    print(display[6 - remaining_attempts])
    print(" ".join([letter if letter in guessed_letters else "_" for letter in word_to_guess]))
    print(f"\nAttempts left: {remaining_attempts}\n")

    if all(letter in guessed_letters for letter in word_to_guess):
        print(f"Congratulations! You guessed the word '{word_to_guess}' correctly!")
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.\n")
        continue

    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try again.\n")
        continue

    guessed_letters.append(guess)

    if guess not in word_to_guess:
        remaining_attempts -= 1
        print(f"Warning: {remaining_attempts} attempts left.\n")
    
if remaining_attempts == 0:
    print(f"Sorry, you are out of attempts. The word was '{word_to_guess}'. Better luck next time!")
