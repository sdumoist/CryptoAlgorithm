from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend


def generate_sm2_keypair():
    # 生成SM2密钥对
    private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
    public_key = private_key.public_key()
    return private_key, public_key


def perform_sm2_encryption(public_key, plaintext):
    # 使用SM2公钥进行加密
    ciphertext = public_key.encrypt(plaintext, ec.ECIES())
    return ciphertext


def perform_sm2_decryption(private_key, ciphertext):
    # 使用SM2私钥进行解密
    plaintext = private_key.decrypt(ciphertext, ec.ECIES())
    return plaintext


# 示例用法
# 生成SM2密钥对
private_key, public_key = generate_sm2_keypair()

# 待加密的明文
plaintext = '使用SM2加密的消息'

# 使用公钥进行加密
ciphertext = perform_sm2_encryption(public_key, plaintext)
print("加密后的密文:", ciphertext)

# 使用私钥进行解密
decrypted_plaintext = perform_sm2_decryption(private_key, ciphertext)
print("解密后的明文:", decrypted_plaintext)