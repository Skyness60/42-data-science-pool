"""Program that counts different types of characters in a given text."""

import sys


def print_stats(text):
    """Print statistics of the given text."""
    print("The text contains " + str(len(text)) + " characters:")
    print(str(sum(1 for c in text if c.isupper())) + " upper letters")
    print(str(sum(1 for c in text if c.islower())) + " lower letters")
    print(str(sum(1 for c in text if c in ".,;:!?\"'")) + " punctuation marks")
    print(str(sum(1 for c in text if c.isspace())) + " spaces")
    print(str(sum(1 for c in text if c.isdigit())) + " digits")


def main():
    """Main function to process command line arguments or standard input."""
    args = sys.argv[1:]
    if len(args) == 0:
        while True:
            try:
                line = input()
                print_stats(line)
                break
            except EOFError:
                break
    elif len(args) >= 1:
        for arg in args:
            print_stats(arg)


if __name__ == "__main__":
    main()
