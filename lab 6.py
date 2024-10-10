import string
from idlelib.editor import keynames
from msvcrt import kbhit
from operator import index
from pydoc import plaintext

letter= string.ascii_lowercase + ' '


def vigenere_square(alphabet):
    for i in range(26):
        for l in range(26):
            letter =(l+ i) % 26
            print(f'{alphabet[letter]}' , end=' ')

        print()


def letter_to_index(let, alphabet):
    let = let.lower()
    # print(f'{let}, {alphabet}')
    for i, l in enumerate(alphabet.lower()):
        if l == let:
            return i
    return -1

def index_to_letter(alphabet, index):
    i = 0
    for l in alphabet:
        if i == index:
            return l
        i += 1
    return ''


def vigenere_index(key_letter, plaintext_letter,alphabet):
    key_index = letter_to_index(key_letter, alphabet)
    plain_index = letter_to_index(plaintext_letter, alphabet)
    # print(f'{key_index} {plain_index}')
    encrypted_index = (key_index + plain_index)% len(alphabet)

    return index_to_letter(alphabet, encrypted_index)

key = "doover"
plaintext= "kill dem all an dung"
def encrypt_vigenere(key, plaintext, alphabet):
    ciphertext = ''
    k_len =len(key)
    for i, l in enumerate(plaintext):
        # print(f'{i}: {key[i%k_len]},{l}')
        ciphertext += vigenere_index(key[i%k_len], l, alphabet)
    return ciphertext

print(letter)
vigenere_square(letter)
print(letter_to_index('k',letter))
print(index_to_letter(letter,8))
print(vigenere_index('o',"o",letter))
print(encrypt_vigenere(key,plaintext, letter))
