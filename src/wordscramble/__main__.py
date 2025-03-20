# Import our command-line interface module.
import wordscramble.cli as cli

def main():
    scrambler = cli.WordScrambleCLI()
    scrambler.intro()
    while True:
        message = scrambler.scramble_menu() 
        if message:
            print(message)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    except cli.UserQuitException:
        print("Goodbye!")
    except Exception as ex:
        raise