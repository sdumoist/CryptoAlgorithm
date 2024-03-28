str = input("请输入一段英文：")
key = int(input("请输入密钥："))
enc = int(input("0 - 解密\n1 - 加密\n请选择 0 或者 1: "))
str_enc = ""
str_dec = ""

if enc == 1:  #加密
    for i in str:  #用i进行遍历
        if i.isupper():  #isupper函数判断i是否为大写字母
            i_unicode = ord(i)  #找到“i”对应的Unicode码
            i_index = ord(i) - ord("A")  #计算字母“i”到A（起始）的间距
            new_index = (i_index + key) % 26
            new_unicode = new_index + ord("A")
            new_character = chr(new_unicode)  #将Unicode码转换为字符
            str_enc += new_character
        elif i.islower():  #如果“i”为小写字母
            i_unicode = ord(i)
            i_index = ord(i) - ord("a")
            new_index = (i_index + key) % 26
            new_unicode = new_index + ord("a")
            new_character = chr(new_unicode)
            str_enc = str_enc + new_character
        else:  #数字或符号
            str_enc += i  #直接返回“i”
    print("密文为：",str_enc)

else:  #解密
    for k in str:
        if k.isupper():
            k_unicode = ord(k)
            k_index = ord(k) - ord("A")
            new_index = (k_index - key) % 26
            new_unicode = new_index + ord("A")
            new_character = chr(new_unicode)
            str_dec = str_dec + new_character
        elif k.islower():
            k_unicode = ord(k)
            k_index = ord(k) - ord("a")
            new_index = (k_index - key) % 26
            new_unicode = new_index + ord("a")
            new_character = chr(new_unicode)
            str_dec += new_character 
        else:
            str_dec += k
    print("明文为：",str_dec)
