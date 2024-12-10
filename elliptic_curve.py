from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

def ecc_encrypt_decrypt(message, private_key, peer_public_key):
    # Generate shared secret
    shared_key = private_key.exchange(ec.ECDH(), peer_public_key)
    derived_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b'handshake data',
    ).derive(shared_key)

    # Encryption
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(derived_key), modes.CFB(iv))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(message) + encryptor.finalize()

    # Decryption
    decryptor = Cipher(algorithms.AES(derived_key), modes.CFB(iv)).decryptor()
    decrypted_message = decryptor.update(ciphertext) + decryptor.finalize()

    return ciphertext, decrypted_message

# Example usage
private_key = ec.generate_private_key(ec.SECP256R1())
peer_private_key = ec.generate_private_key(ec.SECP256R1())
peer_public_key = peer_private_key.public_key()

message = b"hello"
ciphertext, decrypted_message = ecc_encrypt_decrypt(message, private_key, peer_public_key)
print("Encrypted:", ciphertext)
print("Decrypted:", decrypted_message.decode())
