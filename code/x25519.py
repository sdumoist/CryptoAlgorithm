from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey, X25519PublicKey
from cryptography.hazmat.primitives import serialization


def generate_x25519_keypair():
    # 生成X25519密钥对
    private_key = X25519PrivateKey.generate()
    public_key = private_key.public_key()
    return private_key, public_key


def perform_x25519_key_exchange(private_key, peer_public_key):
    # 执行X25519密钥交换
    shared_key = private_key.exchange(peer_public_key)
    return shared_key

# 为Alice生成密钥对
alice_private_key, alice_public_key = generate_x25519_keypair()

# 为Bob生成密钥对
bob_private_key, bob_public_key = generate_x25519_keypair()

# 在Alice和Bob之间执行密钥交换
alice_shared_key = perform_x25519_key_exchange(alice_private_key, bob_public_key)
bob_shared_key = perform_x25519_key_exchange(bob_private_key, alice_public_key)

# 检查共享密钥是否匹配
print("共享密钥匹配:", alice_shared_key == bob_shared_key)