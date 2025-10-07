"""Program that filters words longer than a given length using ft_filter."""

import sys
from ft_filter import ft_filter


def main():
    """Main entry point for the filterstring program."""
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        s = sys.argv[1]
        n_str = sys.argv[2]

        if not n_str.lstrip("+-").isdigit():
            raise AssertionError("the arguments are bad")

        n = int(n_str)
        words = s.split()

        result = list(ft_filter(lambda w: len(w) > n, words))
        print(result)

    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
