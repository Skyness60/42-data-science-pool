import sys
import unicodedata


NESTED_MORSE = {
    "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",
    "E": ".",     "F": "..-.",  "G": "--.",   "H": "....",
    "I": "..",    "J": ".---",  "K": "-.-",   "L": ".-..",
    "M": "--",    "N": "-.",    "O": "---",   "P": ".--.",
    "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
    "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",
    "Y": "-.--",  "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.",
    " ": "/"
}


def normalize_char(c: str) -> str:
    """Normalize special letters (é, à, ü, etc.) into base Latin letters."""
    normalized = unicodedata.normalize("NFD", c)
    return "".join(ch for ch in normalized if unicodedata.category(ch) != "Mn")


def encode_morse(text: str) -> str:
    """Return Morse code translation with intelligent fallback."""
    morse = []

    for c in text.upper():
        c = normalize_char(c)
        if len(c) > 1:
            c = c[0]
        if c in NESTED_MORSE:
            morse.append(NESTED_MORSE[c])
        elif c.isalpha():
            morse.append("...-.-")
        elif c.isdigit():
            morse.append("-----")
        else:
            continue
    return " ".join(morse)


def main():
    """Main entry point."""
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")

        text = sys.argv[1]
        result = encode_morse(text)
        print(result)

    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
