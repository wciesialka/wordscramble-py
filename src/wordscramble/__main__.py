# Import our command-line interface module.
import wordscramble.cli as cli

def main():
    # Create our CLI handler.
    scrambler = cli.WordScrambleCLI()
    scrambler.perform_intro()
    # Let the handler loose! Make it start giving the user menus!
    while True:
        message = scrambler.scramble_menu() 
        # If there's a message to report, send it!
        if message:
            print(message)

if __name__ == "__main__":
    try:
        main()
    # Allows us to press CTRL-C to quit without an annoying message.
    except KeyboardInterrupt:
        pass
    # Check to see if the User asked to quit.
    except cli.MenuExit:
        print("Goodbye!")
    # Report any other errors.
    except Exception as ex:
        raise