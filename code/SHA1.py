import hashlib


def compute_sha1_hash(message):
    # 创建SHA-1哈希对象
    sha1_hash = hashlib.sha1()
    # 更新哈希对象的输入消息
    sha1_hash.update(message)
    # 获取哈希值
    hash_value = sha1_hash.hexdigest()
    return hash_value


# 示例用法
message = input('计算SHA-1哈希的消息。')

# 计算SHA-1哈希值
sha1_hash = compute_sha1_hash(message)
print("SHA-1哈希值:", sha1_hash)