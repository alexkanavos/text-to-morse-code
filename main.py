from data import morse_chars


MORSE_DATA = morse_chars


def text_to_morse(text: str):
    morse_code = [
        MORSE_DATA[character] for character in text if character in MORSE_DATA
    ]
    return " ".join(morse_code)


def run():
    keep_converting = True
    while keep_converting:
        user_input = list(
            input("Type the text to be converted to Morse Code: ").upper()
        )
        result = text_to_morse(text=user_input)
        print(f"Morse Code: {result}")
        if input("Do you want to convert text again [y/n]: ").lower() != "y":
            keep_converting = False


if __name__ == "__main__":
    run()
