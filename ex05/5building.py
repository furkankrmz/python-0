import sys
import string

def count_text_features(text):
    """
    Analyzes a string to count the following:
    - Uppercase letters
    - Lowercase letters
    - Punctuation characters
    - Spaces
    - Digits

    Args:
        text (str): The input text to analyze.

    Returns:
        dict: A dictionary containing counts of each feature.
    """
    result = {
        "upper": sum(1 for char in text if char.isupper()),
        "lower": sum(1 for char in text if char.islower()),
        "punctuation": sum(1 for char in text if char in string.punctuation),
        "spaces": sum(1 for char in text if char.isspace()),
        "digits": sum(1 for char in text if char.isdigit()),
    }
    return result

def main():
    """
    Main function to handle command-line arguments and process the input text.
    """
    try:
        # Ensure proper usage
        if len(sys.argv) > 2:
            raise AssertionError("Too many arguments provided. Please provide only one string argument.")

        # Get the input text
        if len(sys.argv) == 2:
            text = sys.argv[1]
        else:
            print("What is the text to count? (Press Ctrl+D to finish input):")
            text = sys.stdin.read()  # Read multiline input until EOF (Ctrl+D)

        # Analyze the text
        counts = count_text_features(text)
        total_characters = len(text)

        # Display the results
        print(f"The text contains {total_characters} characters:")
        print(f"{counts['upper']} upper letters")
        print(f"{counts['lower']} lower letters")
        print(f"{counts['punctuation']} punctuation marks")
        print(f"{counts['spaces']} spaces")
        print(f"{counts['digits']} digits")

    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
