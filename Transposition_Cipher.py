def columnar_transposition_encrypt(plaintext, key):
    matrix = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(plaintext):
            matrix[col] += plaintext[pointer]
            pointer += key
    return ''.join(matrix)

def columnar_transposition_decrypt(ciphertext, key):
    num_cols = key
    num_rows = len(ciphertext) // num_cols
    num_extra_chars = len(ciphertext) % num_cols
    plaintext_matrix = [''] * num_cols
    col = row = 0
    for char in ciphertext:
        plaintext_matrix[col] += char
        col += 1
        if (col == num_cols) or (col == num_cols - 1 and row >= num_rows):
            col = 0
            row += 1
    return ''.join(plaintext_matrix)

# Example usage
plaintext = "HELLOENCRYPTION"
key = 5
encrypted = columnar_transposition_encrypt(plaintext, key)
print(f"Encrypted: {encrypted}")
decrypted = columnar_transposition_decrypt(encrypted, key)
print(f"Decrypted: {decrypted}")
