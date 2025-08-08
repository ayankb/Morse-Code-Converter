MORSE_CODES = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


def encrypt(text):
    encrypt_text = ''
    for letter in text:
        if letter != ' ':
            encrypt_text += MORSE_CODES[letter]+' '

        else:
            encrypt_text += ' '

    return encrypt_text


def decrypt(text):
    text += ' '
    decrypet_text = ''
    code = ''

    for letter in text:

        if letter != ' ':
            space_count = 0
            code += letter

        else:
            space_count += 1

            if space_count == 2:
                decrypet_text += ' '

            else:
                for key, val in MORSE_CODES.items():
                    if val == code:
                        actual_letter = key
                        break

                decrypet_text += actual_letter
                code = ''

    return decrypet_text


def main():
    mode = input('What do you want to do? (Type "E" for Encode or "D" for Decode): ').upper()
    if mode == 'E':
        message = input("Enter the message to Encode:\n").upper()
        print(f'Encrypted message:\n{encrypt(message)}')

    elif mode == 'D':
        message = input('Enter the morse code to Decode:\n')
        print(f"Decoded Message:\n{decrypt(message)}")

    else:
        print('Invalid Input!')


if __name__ == '__main__':
    main()
