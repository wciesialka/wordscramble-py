# Import our command-line interface module.
import wordscramble.menus as menus
# Import our key-generation module
import wordscramble.keygen as keygen
# Import our word-scrambling module
import wordscramble.scramble as scramble
# Import deepcopy to make "deep copies" of dictionaries
from copy import deepcopy

class UserQuitException(SystemExit):
    def __init__(self):
        super().__init__()
        self.code = 0

class WordScrambleCLI:

    def __init__(self):
        self.__key = None
    
    @property
    def key(self):
        return deepcopy(self.__key)
    
    def has_key(self):
        return not (self.__key is None)

    def get_key(self):
        choice = menus.key_menu()
        if choice == menus.KeyMenuChoice.GENERATE_NEW_KEY:
            self.__key = keygen.generate_random_key()
        elif choice == menus.KeyMenuChoice.IMPORT_KEY:
            key_string = input("Your key: ")
            self.__key = keygen.decode_key(key_string)
        elif choice == menus.KeyMenuChoice.QUIT:
            raise UserQuitException
    
    def scramble_menu(self):
        if not self.has_key():
            print("No key currently loaded.")
            self.get_key()
        choice = menus.scramble_menu()
        if choice == menus.ScrambleMenuChoice.SCRAMBLE_MESSAGE:
            word = menus.get_user_message()
            scrambled = scramble.scramble(word, self.key)
            return f"Your scrambled message: \"{scrambled}\""
        elif choice == menus.ScrambleMenuChoice.UNSCRAMBLE_MESSAGE:
            word = menus.get_user_message()
            unscrambled = scramble.unscramble(word, self.key)
            return f"Your unscrambled message: \"{unscrambled}\""
        elif choice == menus.ScrambleMenuChoice.EXPORT_KEY:
            key_string = keygen.encode_key(self.key)
            return f"Your key: \"{key_string}\""
        elif choice == menus.ScrambleMenuChoice.NEW_KEY:
            self.__key = self.get_key()
            return f"New key set."
        elif choice == menus.ScrambleMenuChoice.QUIT:
            raise UserQuitException
    
    def intro(self):
        intro_message = "== Welcome to Word Scrambler! =="
        print(f"{intro_message:^80}")
