import pyDes
import base64
 
from Crypto.Cipher import DES3
import codecs
import base64
 
class EncryptDate:
    def __init__(self, key):
        self.key = key  # 初始化密钥
        self.iv = b'01234567' # 偏移量
        self.length = DES3.block_size  # 初始化数据块大小
        self.des3 = DES3.new(self.key, DES3.MODE_CBC, self.iv)  # 初始化AES,CBC模式的实例
        # 截断函数，去除填充的字符
        self.unpad = lambda date: date[0:-ord(date[-1])]
 
    def pad(self, text):
        """
        #填充函数，使被加密数据的字节码长度是block_size的整数倍
        """
        count = len(text.encode('utf-8'))
        add = self.length - (count % self.length)
        entext = text + (chr(add) * add)
        return entext
 
    def encrypt(self, encrData):  # 加密函数
 
        res = self.des3.encrypt(self.pad(encrData).encode("utf8"))
        msg = str(base64.b64encode(res), encoding="utf8")
        # msg =  res.hex()
        return msg
 
    def decrypt(self, decrData):  # 解密函数
        res = base64.decodebytes(decrData.encode("utf8"))
        # res = bytes.fromhex(decrData)
        msg = self.des3.decrypt(res).decode("utf8")
        return self.unpad(msg)
 
 
eg = EncryptDate("liushangsdumoist")  # 这里密钥的长度必须是16的倍数
res = eg.encrypt("13173005656")
print(res)
eg1 = EncryptDate("liushangsdumoist")
print(eg1.decrypt(res))