from data import morse_chars


MORSE_DATA = morse_chars


def text_to_morse(text: str):
    morse_code = [
        MORSE_DATA[character] for character in text if character in MORSE_DATA
    ]
    return " ".join(morse_code)


def run():
    user_input = list(input("Text to be converted to morse code: ").upper())
    result = text_to_morse(text=user_input)
    print(result)


if __name__ == "__main__":
    run()
