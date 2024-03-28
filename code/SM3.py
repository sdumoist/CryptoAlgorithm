from cryptography.hazmat.primitives import hashes


def compute_sm3_hash(message):
    # 创建SM3哈希对象
    sm3_hash = hashes.Hash(hashes.SM3(), backend=default_backend())
    # 更新哈希对象的输入消息
    sm3_hash.update(message)
    # 获取哈希值
    hash_value = sm3_hash.finalize()
    return hash_value


# 示例用法
message = input('SM3哈希加密的消息')

# 计算SM3哈希值
sm3_hash = compute_sm3_hash(message)
print("SM3哈希值:", sm3_hash.hex())