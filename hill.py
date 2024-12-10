import numpy as np

def hill_cipher_encrypt_decrypt(text, key, mode='encrypt'):
    text = text.lower().replace(" ", "")
    key_matrix = np.array(key)
    n = key_matrix.shape[0]

    while len(text) % n != 0:
        text += "x"  # Padding

    text_vector = [ord(char) - ord('a') for char in text]
    text_matrix = np.array(text_vector).reshape(-1, n)

    if mode == 'decrypt':
        det = int(np.round(np.linalg.det(key_matrix)))  # Determinant of key
        det_inv = pow(det, -1, 26)  # Modular inverse
        adj = np.round(det * np.linalg.inv(key_matrix)).astype(int) % 26  # Adjugate matrix
        key_matrix = (det_inv * adj) % 26

    result_matrix = (text_matrix @ key_matrix) % 26
    result_text = ''.join(chr(char + ord('a')) for char in result_matrix.flatten())

    if mode == 'decrypt':
        result_text = result_text.rstrip("x")  # Remove padding

    return result_text

# Example usage
plaintext = "hello"
key = [[6, 24, 1], [13, 16, 10], [20, 17, 15]]  # Example 3x3 key matrix

ciphertext = hill_cipher_encrypt_decrypt(plaintext, key, mode='encrypt')
print("Encrypted:", ciphertext)

decrypted = hill_cipher_encrypt_decrypt(ciphertext, key, mode='decrypt')
print("Decrypted:", decrypted)
