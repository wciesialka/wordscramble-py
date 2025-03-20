# Import Dict from Typing module for type-hinting
from typing import Dict
# Import random module to generate our random key
import random
# Import string module for string operations
import string

# Seed the random number generator
random.seed()

def scramble(word: str, key: Dict[str, str]):
    result = ""
    # Build the result character by character
    for character in word:
        # If the character is in our key, then add the corresponding
        # character to our list. Otherwise, just add the character.
        if character in key:
            result += key[character]
        else:
            result += character
    return result

def unscramble(word: str, key: Dict[str, str]):
    # Create a dictionary that puts the key in reverse,
    # then use that to "scramble" the word.
    reverse_key = {v: k for k, v in key.items()}
    return scramble(word, reverse_key)

def generate_random_key():
    # Create a list of letters, and a shuffled version of that list
    letters = string.ascii_letters + string.digits + string.punctuation + " "
    shuffled = random.sample(letters, len(letters))
    # Create our key
    key = {k: v for k, v in zip(letters, shuffled)}
    return key

def main():
    key = generate_random_key()
    while True:
        print("Welcome to Word Scrambler!")
        print("Actions:")
        print("\t[1] Scramble")
        print("\t[2] Unscramble")
        print("\t[3] Exit")
        print()
        user_inp = input("Your selection: ").strip()
        if user_inp == "1":
            word = input("Your message: ")
            scrambled = scramble(word, key)
            print(f"Your scrambled message is: \"{scrambled}\"")
        elif user_inp == "2":
            word = input("Your message: ")
            unscrambled = unscramble(word, key)
            print(f"Your unscrambled message is: \"{unscrambled}\"")
        elif user_inp == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Try again!")

if __name__ == "__main__":
    main()
