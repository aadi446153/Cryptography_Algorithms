import random

# Initialize the three shift registers with their tap positions
R1 = [0] * 19  # First register, size 19
R2 = [0] * 22  # Second register, size 22
R3 = [0] * 23  # Third register, size 23

# Feedback positions (tap positions) for the majority function
R1_taps = [13, 16, 17, 18]
R2_taps = [20, 21]
R3_taps = [7, 20, 21, 22]

# Majority function: it decides which register should be clocked
def majority(a, b, c):
    return (a & b) | (b & c) | (a & c)

# Clock function: it shifts the register and applies feedback from the tap positions
def clock_register(reg, taps):
    feedback = 0
    for t in taps:
        feedback ^= reg[t]
    return [feedback] + reg[:-1]

# Function to clock the A5/1 registers based on the majority function
def clock():
    # Compute the majority bit from the three registers
    maj = majority(R1[8], R2[10], R3[10])

    # Clock the registers whose clocking bit matches the majority bit
    if R1[8] == maj:
        clock_register(R1, R1_taps)
    if R2[10] == maj:
        clock_register(R2, R2_taps)
    if R3[10] == maj:
        clock_register(R3, R3_taps)

# Initialize the key stream
def key_stream(length):
    ks = []
    for _ in range(length):
        clock()  # Clock the registers
        # XOR the outputs of the three registers to form a key stream bit
        ks.append(R1[-1] ^ R2[-1] ^ R3[-1])
    return ks

# Convert a string to bits
def string_to_bits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result

# Convert bits back to a string
def bits_to_string(b):
    chars = []
    for byte in range(len(b) // 8):
        byte_bits = b[byte * 8:(byte + 1) * 8]
        chars.append(chr(int(''.join([str(bit) for bit in byte_bits]), 2)))
    return ''.join(chars)

# Encryption/Decryption function using A5/1 stream cipher
def a5_encrypt(plaintext):
    plaintext_bits = string_to_bits(plaintext)
    stream = key_stream(len(plaintext_bits))
    cipher_bits = [p ^ k for p, k in zip(plaintext_bits, stream)]
    return cipher_bits

def a5_decrypt(ciphertext_bits):
    stream = key_stream(len(ciphertext_bits))
    plain_bits = [c ^ k for c, k in zip(ciphertext_bits, stream)]
    return bits_to_string(plain_bits)

# Initialize registers with random values (or could be initialized with a key)
def initialize_registers():
    global R1, R2, R3
    R1 = [random.randint(0, 1) for _ in range(19)]
    R2 = [random.randint(0, 1) for _ in range(22)]
    R3 = [random.randint(0, 1) for _ in range(23)]

# Example usage
initialize_registers()

plaintext = "Aadesh Bafna"
ciphertext_bits = a5_encrypt(plaintext)
ciphertext = bits_to_string(ciphertext_bits)
print(f"Ciphertext: {ciphertext}")

# Decryption
decrypted_text = a5_decrypt(ciphertext_bits)
print(f"Decrypted: {decrypted_text}")
