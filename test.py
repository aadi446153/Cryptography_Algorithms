import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def aes_decrypt(ciphertext_b64, key):
    key_bytes = key.encode('utf-8')
    ciphertext = base64.b64decode(ciphertext_b64)
    
    # Using a zeroed IV (common when IV is not specified)
    iv = b'\x00' * AES.block_size
    
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext.decode()

# Example usage
ciphertext_b64 = "B/Qjn2MpwGfh0cZMCYaynK7GJqWA+ZOPN+IzoszvKX4Px5sQuP6/lpANyyLd8Eb8"
key = "AdeshAnirudhSami"
decrypted = aes_decrypt(ciphertext_b64, key)
print(f"Decrypted: {decrypted}")
