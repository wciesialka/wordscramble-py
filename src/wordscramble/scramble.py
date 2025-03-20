import wordscramble.key as key

def scramble(word: str, key: key.Key):
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

def unscramble(word: str, key: key.Key):
    # Inverse the key, then use that to "scramble" the word.
    return scramble(word, key.inverse())