import sys

args = sys.argv[1:]

if len(args) == 0:
    pass
elif len(args) > 1:
    print("AssertionError: more than one argument is provided")
else:
    arg = args[0]
    if arg.lstrip("+-").isdigit():
        num = int(arg)
        if num % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    else:
        print("AssertionError: argument is not an integer")
