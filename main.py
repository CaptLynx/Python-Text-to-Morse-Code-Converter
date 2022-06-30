while True:

    encode_or_decode = input("Press '1' to encode text, Press '0' to decode morse code to text: ")

    morse_dict = {
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        " ": "/",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----."
    }

    key_list = list(morse_dict.keys())
    val_list = list(morse_dict.values())

    def encode():
        txt = input("What would you like to convert to morse code? Letters and numbers only: ").lower()
        morse_code = ""
        for letter in txt:
            if letter in morse_dict.keys():
                morse_code += morse_dict[letter]
                morse_code += " "
        print(morse_code)

    def decode():
        txt = input("Type or paste in the morse code you would like to decode: ").lower().split()
        alphabet_text = ""
        for char in txt:
            if char in morse_dict.values():
                pos = val_list.index(char)
                alphabet_text += key_list[pos]
        print(alphabet_text)

    if encode_or_decode == "1":
        encode()
    elif encode_or_decode == "0":
        decode()

    continue_input = input("Press any key to contine.")

#--🚀 Text to Morse Code Converter by CaptLynx 2022 🚀--#