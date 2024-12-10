from Crypto.Cipher import ARC4
from Crypto.Random import get_random_bytes

# Generate a random key
key = get_random_bytes(16)  # 128-bit key for RC4

# Create an RC4 cipher object
cipher = ARC4.new(key)

# Encrypt a message
plaintext = "Hello, Stream Ciphers!"
ciphertext = cipher.encrypt(plaintext.encode('utf-8'))
print("Ciphertext (in bytes):", ciphertext)

# Decrypt the message
cipher = ARC4.new(key)  # Reinitialize the cipher object with the same key
decrypted_text = cipher.decrypt(ciphertext)
print("Decrypted text:", decrypted_text.decode('utf-8'))
