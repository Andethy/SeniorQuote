# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import sys

shift_csr = 8


def encrypt():
    text_str = input("Input Text: ")
    text_hex = ''
    for index, char in enumerate(text_str):
        text_asc = ord(char.lower())
        char_csr = text_asc + shift_csr if text_asc > 64 else text_asc
        # print(char, text_asc)
        char_csr -= 26 if char_csr > 122 else 0
        char_hex = hex(char_csr)
        if char_csr == 32:
            text_hex += ' '
            continue
        text_hex += char_hex[2:len(char_hex)].upper()
    text_hex = text_hex[:len(text_hex)] + '.'
    print("---\nOUTPUT:\n", text_hex, sep='')


def decrypt():
    text_hex = input("Input Hex: ")
    text_str = ''
    text_lst = text_hex.split()
    for index, word in enumerate(text_lst):
        for location, char in enumerate(word):
            if location % 2 == 1 or char == '.': continue
            # print(location, len(word))
            char_hex = word[location:location + 2]
            char_bit = bytes.fromhex(char_hex)
            char_asc = ord(char_bit.decode('ASCII'))
            char_csr = char_asc - shift_csr if char_asc > 64 else char_asc
            char_csr += 26 if char_csr < 97 else 0
            if char_asc == 34: char_csr = 34
            char_str = chr(char_csr)
            # print(char_str, char_asc)
            text_str += char_str
        text_str += ' '
    text_str = text_str[:-1] + '.'
    print("---\nOUTPUT:\n", text_str, sep='')


if __name__ == '__main__':
    if sys.argv[1] == 'e':
        encrypt()
    elif sys.argv[1] == 'd':
        decrypt()
