# Import our command-line interface module.
import wordscramble.menus as menus
# Import our word-scrambling module
import wordscramble.scramble as scramble
# Import our key class from our key module
from wordscramble.key import Key

# Create a custom Exception so we can quit from menus anywhere.
class MenuExit(SystemExit):
    def __init__(self):
        super().__init__()
        self.code = 0

# Create a class to handle Word Scramble CLI functionality.
class WordScrambleCLI:

    def __init__(self):
        self.__key: Key = None
    
    @property
    def key(self) -> Key:
        return self.__key
    
    # Check to see if we have a key already. If we do, return True. Otherwise,
    # return False.
    def has_key(self) -> bool:
        return not (self.__key is None)

    # Ask the user if they'd like to generate a new key or import a key,
    # then set whichever they choose to our key.
    def get_key(self):
        choice = menus.key_menu()
        if choice == menus.KeyMenuChoice.GENERATE_NEW_KEY:
            self.__key = Key.random()
        elif choice == menus.KeyMenuChoice.IMPORT_KEY:
            key_string = input("Your key: ")
            self.__key = Key.loads(key_string)
        elif choice == menus.KeyMenuChoice.QUIT:
            raise MenuExit
    
    # Show the user the main menu.
    def scramble_menu(self) -> str:
        # Set a key if we don't have one already.
        if not self.has_key():
            print("No key currently loaded.")
            self.get_key()
        # Show the user the menu.
        choice = menus.scramble_menu()
        # Parse user choice.
        if choice == menus.ScrambleMenuChoice.SCRAMBLE_MESSAGE:
            word = menus.get_user_message()
            scrambled = scramble.scramble(word, self.key)
            return f"Your scrambled message: \"{scrambled}\""
        elif choice == menus.ScrambleMenuChoice.UNSCRAMBLE_MESSAGE:
            word = menus.get_user_message()
            unscrambled = scramble.unscramble(word, self.key)
            return f"Your unscrambled message: \"{unscrambled}\""
        elif choice == menus.ScrambleMenuChoice.EXPORT_KEY:
            key_string = self.key.dumps()
            return f"Your key: \"{key_string}\""
        elif choice == menus.ScrambleMenuChoice.NEW_KEY:
            self.__key = self.get_key()
            return f"New key set."
        elif choice == menus.ScrambleMenuChoice.QUIT:
            raise MenuExit
    
    def perform_intro(self):
        intro_message = "== Welcome to Word Scrambler! =="
        print(f"{intro_message:^80}")
