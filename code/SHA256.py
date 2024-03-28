import hashlib


def compute_sha256_hash(message):
    # 创建SHA-256哈希对象
    sha256_hash = hashlib.sha256()
    # 更新哈希对象的输入消息
    sha256_hash.update(message)
    # 获取哈希值
    hash_value = sha256_hash.hexdigest()
    return hash_value


message = input('计算SHA-256哈希的消息')

# 计算SHA-256哈希值
sha256_hash = compute_sha256_hash(message)
print("SHA-256哈希值:", sha256_hash)