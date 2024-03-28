from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding


def sm4_encrypt(key, plaintext):
    # 创建SM4加密算法对象
    sm4_cipher = Cipher(algorithms.SM4(key), mode=modes.ECB(), backend=default_backend())
    encryptor = sm4_cipher.encryptor()
    # 对明文进行填充
    padder = padding.PKCS7(128).padder()
    padded_plaintext = padder.update(plaintext) + padder.finalize()
    # 加密明文
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
    return ciphertext


def sm4_decrypt(key, ciphertext):
    # 创建SM4解密算法对象
    sm4_cipher = Cipher(algorithms.SM4(key), mode=modes.ECB(), backend=default_backend())
    decryptor = sm4_cipher.decryptor()
    # 解密密文
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    # 对解密后的明文进行去填充
    unpadder = padding.PKCS7(128).unpadder()
    unpadded_plaintext = unpadder.update(plaintext) + unpadder.finalize()
    return unpadded_plaintext


# 示例用法
key = b'0123456789ABCDEF'
plaintext = input('使用SM4加密的明文')

# 加密明文
ciphertext = sm4_encrypt(key, plaintext)
print("加密后的密文:", ciphertext.hex())

# 解密密文
decrypted_plaintext = sm4_decrypt(key, ciphertext)
print("解密后的明文:", decrypted_plaintext.decode())