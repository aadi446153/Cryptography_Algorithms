from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import string

def shift_by_n_cipher(text, shift, mode='encrypt'):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    if mode == 'decrypt':
        translation_table = str.maketrans(shifted_alphabet, alphabet)
    else:
        translation_table = str.maketrans(alphabet, shifted_alphabet)
    return text.translate(translation_table)

# Example usage
plaintext = "hello"
shift = 3
ciphertext = shift_by_n_cipher(plaintext, shift)
print("Encrypted:", ciphertext)
decrypted = shift_by_n_cipher(ciphertext, shift, mode='decrypt')
print("Decrypted:", decrypted)
