import hashlib


def sha3_256(message):
    # 创建SHA-3-256哈希对象
    sha3_hash = hashlib.sha3_256()
    # 将消息添加到哈希对象中
    sha3_hash.update(message)
    # 返回16进制表示的哈希值
    return sha3_hash.hexdigest()


message = input('计算SHA-3哈希的消息')

# 计算SHA-3哈希值
sha3_digest = sha3_256(message)
print("SHA-3哈希值:", sha3_digest)