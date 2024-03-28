from DES_BOX import IP, IP_RE, PC_1, PC_2, E, P, S_BOX, SHIFT

#读取文件
def read_file(filename): 
    '''
    filename : 打开文件名
    return : 读取文件中字符串
    '''
    try:
        fp = open(filename,"r",encoding='utf-8')
        message = fp.read()
        fp.close()
        return message
    except:
        print("Open file error!")

#文件写入
def write_file(filename): 
    '''
    filename : 打开文件名
    return : 读取文件中字符串
    '''
    try:
        fp = open('text.txt','w',encoding='utf-8')
        message = fp.read()
        fp.write(message)
        fp.close()
        return message
    except:
        print("Write file error!")

# 字符串转01比特流
def str_bit( message ):
    '''
    message ：字符串
    return ：将读入的字符串序列转化成01比特流序列
    '''
    bits = ""
    for i in message:
        asc2i = bin(ord(i))[2:] #bin将十进制数转二进制返回带有0b的01字符串
        '''为了统一每一个字符的01bit串位数相同，将每一个均补齐8位'''
        for j in range(8-len(asc2i)):
            asc2i = '0' + asc2i
        bits += asc2i
    return bits 

# 01比特流转字符
def bit_str(bits):
    '''
    bits: 01比特串（长度是8的倍数）
    return: 对应的字符
    '''
    message = ""
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        decimal = int(byte, 2)
        character = chr(decimal)
        message += character
    return message

# 密钥字符串转比特流
def process_key(key):
    '''
    key : 输入的密钥字符串
    return : 64bit 01序列密钥(采用偶校验的方法) 
    '''
    key_bits = ""
    for i in key:
        count = 0
        asc2i = bin(ord(i))[2:] 
        '''将每一个ascii均补齐7位,第8位作为奇偶效验位''' 
        for j in asc2i:
            count += int(j)
        if count % 2 == 0:
            asc2i += '0'
        else:
            asc2i += '1' 
        for j in range(7-len(asc2i)):
            asc2i = '0' + asc2i
        key_bits += asc2i
    if len(key_bits) > 64:
        return key_bits[0:64]
    else:
        for i in range(64-len(key_bits)):
            key_bits += '0'
        return key_bits 

# 对比特流分组
def divide(bits, bit):
    '''
    bits: 01比特串
    bit: 分组的位数
    return: 按bit位分组后得到的列表
    '''
    groups = []
    num_groups = len(bits) // bit
    for i in range(num_groups):
        group = bits[i * bit : (i + 1) * bit]
        groups.append(group)
    remaining_bits = len(bits) % bit
    if remaining_bits > 0:
        last_group = bits[num_groups * bit : num_groups * bit + remaining_bits]
        last_group += '0' * (bit - remaining_bits)
        groups.append(last_group)
    return groups

# IP置换
def IP_change(bits):
    '''
    bits:一组64位的01比特字符串   
    return：初始置换IP后64bit01序列
    '''
    ip_str = ""
    for i in IP:
        ip_str = ip_str + bits[i-1]
    return ip_str

# PC_1置换
def PC_1_change(bits):
    '''
    bits: 一组64位的01比特字符串   
    return: PC_1置换后的56位01序列
    '''
    pc_1_str = ""
    for i in PC_1:
        pc_1_str = pc_1_str + bits[i-1]
    return pc_1_str

#比特串左移
def key_leftshift(key_str, num):
    '''
    key_str: 一组01比特字符串
    num: 左移的位数
    return: 循环左移num位后的01比特串
    '''
    left_part = key_str[num:]  # 左移后的部分
    right_part = key_str[:num]  # 左移的部分
    return left_part + right_part

# PC_2置换
def PC_2_change(bits):
    '''
    bits: 一组56位的01比特字符串   
    return: PC_2置换后的48位01序列
    '''
    pc_2_str = ""
    for i in PC_2:
        pc_2_str = pc_2_str + bits[i-1]
    return pc_2_str

# 16轮密钥生成
def generate_key(key):
    '''
    key : 64bit01密钥序列
    return : 16轮的16个48bit01密钥列表按1-16顺序
    '''
    key_list = ["" for i in range(16)]
    key = PC_1_change(key) #1、调用置换PC_1
    key_left = key[0:28] #2、左右28位分开
    key_right = key[28:]
    for i in range(len(SHIFT)): #共16轮即16次左循环移位
        key_left = key_leftshift(key_left, SHIFT[i]) #3、调用比特串左移函数
        key_right = key_leftshift(key_right, SHIFT[i]) 
        key_i = PC_2_change(key_left + key_right) #4、左右合并调用置换PC_2
        key_list[i] = key_i #5、将每一轮的56bit密钥存入列表key_list
    return key_list

# E置换
def E_change(bits):
    '''
    bits: 一组32位的01比特字符串   
    return: E置换后的48位01序列
    '''
    e_str = ""
    for i in E:
        e_str = e_str + bits[i-1]
    return e_str

# 异或运算
def xor(bits, ki):
    '''
    bits: 48位的01字符串或32位的01 F函数输出
    ki: 48位的01密钥序列或32位的01 Li
    return: bits与ki异或运算得到的48位的01或32位的01
    '''
    result = ""
    for i in range(len(bits)):
        if bits[i] == ki[i]:
            result += "0"
        else:
            result += "1"
    return result

#单次 S 盒查找
def s(bits,i):
    '''
    bits : 6 bit01字符串
    i : 使用第i个s盒
    return : 4 bit01字符串
    '''
    row = int(bits[0]+bits[5],2) 
    col = int(bits[1:5],2)
    num = bin(S[i-1][row*16+col])[2:]  #i-1号S盒的row*16+col号数
    for i in range(4-len(num)):    #补齐4位后输出
        num = '0'+num
    return num

#S盒变换
def S_change(bits):
    '''
    bits: 48位的01字符串
    return: 经过S盒变换后的32位的01字符串
    '''
    result = ""
    for i in range(8):
        row = int(bits[i*6] + bits[i*6+5], 2)
        col = int(bits[i*6+1:i*6+5], 2)
        s_box_val = S_BOX[i][row][col]
        result += format(s_box_val, '04b')
    return result

#P变换
def P_change(bits):
    '''
    bits: 一组32位的01比特字符串   
    return: P置换后的32位01序列
    '''
    p_str = ""
    for i in P:
        p_str = p_str + bits[i-1]
    return p_str

# F 函数
def F(bits,ki):
    '''
    bits : 32bit 01 Ri输入
    ki : 48bit 第i轮密钥
    return : F函数输出32bit 01序列串
    '''
    bits = xor(E_change(bits),ki)
    bits = P_change(S_change(bits))
    return bits

#IP 逆置换
def IP_inv_change(bits):
    '''
    bits: 一组64位的01比特字符串   
    return: IP逆置换后的64位01序列
    '''
    ip_inv_str = ""
    for i in IP_RE:
        ip_inv_str = ip_inv_str + bits[i-1]
    return ip_inv_str

#64bit加密 调用IP置换、16轮密钥生成、F函数、异或运算、IP逆置换等模块
def des_encrypt(bits, key):
    '''
    bits: 分组64bit的01明文字符串
    key: 64bit的01密钥
    return: 加密得到的64bit的01密文序列
    '''
    bits = IP_change(bits)  # IP置换
    L = bits[0:32]          # 切片分成两个32bit
    R = bits[32:]
    key_list = generate_key(key)  # 生成16个密钥
    for i in range(16):  # 16轮迭代变换
        L_next = R
        R = xor(L, F(R, key_list[i]))
        L = L_next
    result = IP_inv_change(R + L)  # IP逆置换
    return result

#64bit 解密
def des_decrypt(bits, key):
    '''
    bits: 分组64bit的01密文字符串
    key: 64bit的01密钥
    return: 解密得到的64bit的01明文序列
    '''
    bits = IP_change(bits)  # IP置换
    L = bits[0:32]          # 切片分成两个32bit
    R = bits[32:]
    key_list = generate_key(key)  # 生成16个密钥
    for i in range(15, -1, -1):  # 16轮迭代变换，使用相反顺序的密钥
        L_next = R
        R = xor(L, F(R, key_list[i]))
        L = L_next
    result = IP_inv_change(R + L)  # IP逆置换
    return result

# 整体加密
def all_des_encrypt(message,key):
    '''
    message : 读入明文字符串
    key : 读入密钥串
    returns : 密文01序列
    '''
    message = str_bit(message)  # 明文转01比特流
    key = process_key(key)      # 64bit初始密钥生成
    mess_div = divide(message, 64)  # 明文按64bit一组进行分组
    result =""
    for i in mess_div:
        result += des_encrypt(i, key)  #对每一组进行加密运算
    return result    


# 整体解密
def all_des_decrypt(message, key):
    '''
    message: 读入明文字符串
    key: 读入密钥串
    return: 解密后的01比特流
    '''
    key = process_key(key)  # 64bit初始密钥生成
    mess_div = divide(message, 64)  # 密文按64bit一组进行分组
    result = ""
    for i in mess_div:
        result += des_decrypt(i, key)  # 对每一组进行解密运算
    return result
