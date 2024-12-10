def columnar_transposition_encrypt(plaintext, key):
    # Create a list of strings for each column
    matrix = [''] * key

    # Fill the columns with characters from the plaintext
    for col in range(key):
        pointer = col
        while pointer < len(plaintext):
            matrix[col] += plaintext[pointer]
            pointer += key

    # Return the encrypted text by concatenating the columns
    return ''.join(matrix)

def columnar_transposition_decrypt(ciphertext, key):
    num_cols = key
    num_rows = len(ciphertext) // num_cols
    num_extra_chars = len(ciphertext) % num_cols

    # Create a matrix to hold the plaintext values
    plaintext_matrix = [''] * num_cols

    # Fill the matrix columns by columns
    index = 0
    for col in range(num_cols):
        # Calculate the number of characters to fill in this column
        num_chars = num_rows + (1 if col < num_extra_chars else 0)
        for row in range(num_chars):
            plaintext_matrix[col] += ciphertext[index]
            index += 1

    # Reconstruct the plaintext from the matrix
    plaintext = ''
    for row in range(num_rows + 1):  # Include extra row if there are extra characters
        for col in range(num_cols):
            if row < len(plaintext_matrix[col]):
                plaintext += plaintext_matrix[col][row]

    return plaintext

# Example usage
plaintext = "GoodMorning"
key = 5
encrypted = columnar_transposition_encrypt(plaintext, key)
print(f"Encrypted: {encrypted}")
decrypted = columnar_transposition_decrypt(encrypted, key)
print(f"Decrypted: {decrypted}")
