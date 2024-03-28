from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


def aes_encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    return cipher.iv + ciphertext


def aes_decrypt(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    ciphertext = ciphertext[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext



key = get_random_bytes(16)  # 128-bit key
plaintext = input('This is a secret message.')

# 加密
encrypted = aes_encrypt(plaintext, key)
print("Encrypted:", encrypted)

# 解密
decrypted = aes_decrypt(encrypted, key)
print("Decrypted:", decrypted)