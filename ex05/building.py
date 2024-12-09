import string
import sys

def main():
    if len(sys.argv) == 2:
        message = sys.argv[1]
        count = sum([1 for x in message if x in string.punctuation])
        print("The text contains", len(message), "characters:")
        print(sum(1 for u in message if u.isupper()), "upper letters")
        print(sum(1 for c in message if c.islower()), "lower letters")
        print(count, "punctuation marks")
        print(sum(1 for s in message if s.isspace()), "spaces")
        print(sum(1 for n in message if n.isdigit()), "digits")

    else:
        print("What is the text to count?")
        message = sys.stdin.read()
        count = sum([1 for x in message if x in string.punctuation])
        print("The text contains", len(message), "characters:")
        print(sum(1 for u in message if u.isupper()), "upper letters")
        print(sum(1 for c in message if c.islower()), "lower letters")
        print(count, "punctuation marks")
        print(sum(1 for s in message if s.isspace()), "spaces")
        print(sum(1 for n in message if n.isdigit()), "digits")

if __name__ == "__main__":
    main()
