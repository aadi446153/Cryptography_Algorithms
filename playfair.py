import numpy as np

def playfair_encrypt_decrypt(text, key, mode='encrypt'):
    def prepare_text(text, mode):
        text = text.replace("j", "i").replace(" ", "")
        if mode == 'encrypt' and len(text) % 2 != 0:
            text += 'x'
        return text

    def create_matrix(key):
        alphabet = "abcdefghiklmnopqrstuvwxyz"
        key = "".join(dict.fromkeys(key + alphabet))  # Remove duplicates
        return np.array(list(key)).reshape(5, 5)

    def find_positions(matrix, char1, char2):
        pos1 = np.where(matrix == char1)
        pos2 = np.where(matrix == char2)
        return (pos1[0][0], pos1[1][0]), (pos2[0][0], pos2[1][0])

    text = prepare_text(text, mode)
    matrix = create_matrix(key)
    result_text = ""

    for i in range(0, len(text), 2):
        char1, char2 = text[i], text[i + 1]
        (r1, c1), (r2, c2) = find_positions(matrix, char1, char2)

        if r1 == r2:
            if mode == 'encrypt':
                result_text += matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]
            else:
                result_text += matrix[r1][(c1 - 1) % 5] + matrix[r2][(c2 - 1) % 5]
        elif c1 == c2:
            if mode == 'encrypt':
                result_text += matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]
            else:
                result_text += matrix[(r1 - 1) % 5][c1] + matrix[(r2 - 1) % 5][c2]
        else:
            result_text += matrix[r1][c2] + matrix[r2][c1]

    return result_text

# Example usage
plaintext = "hello"
key = "playfairkey"

ciphertext = playfair_encrypt_decrypt(plaintext, key, mode='encrypt')
print("Encrypted:", ciphertext)

decrypted = playfair_encrypt_decrypt(ciphertext, key, mode='decrypt')
print("Decrypted:", decrypted)
