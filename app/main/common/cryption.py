# _*_ coding: utf-8 _*_
import bcrypt
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from app.main.common.file_op import readfile
"""
数据加密，数据解密，密码加密
"""

# 读取配置文件
user_key = readfile('./app/conf/main.ini','ini')['secretkey']['user_key']


# 1.1、加密数据
def aes_encrypt(data,secret_key = user_key):
    """加密数据
    :param secret_key: 加密秘钥
    :param data: 需要加密数据
    """
    data = bytes(data, encoding="utf-8")
    
    # 填充数据采用pkcs7
    data = pad(data, block_size=16, style="pkcs7")
    # 创建加密器
    cipher = AES.new(key=secret_key.encode("utf-8"), mode=AES.MODE_ECB)
    # 对数据进行加密
    encrypted_data = cipher.encrypt(data)
    # 对数据进行base64编码
    encrypted_data = base64.b64encode(encrypted_data)
    return encrypted_data.decode()
 
# 1.2、解密数据
def aes_decrypt(data,secret_key = user_key):
    """解密数据
    """
    data = base64.b64decode(data)
    cipher = AES.new(key=secret_key.encode("utf-8"), mode=AES.MODE_ECB)
    decrypt_data = cipher.decrypt(data)
    decrypt_data = unpad(decrypt_data, 16, style="pkcs7")
    return decrypt_data.decode("utf-8")



# 2.1、加密密码 密码采取hash加密，不可逆
def bcrypt_encrypt(password):
    """加密密码
    :param password: 密码
    """
    password = bytes(password, encoding="utf-8")
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed_password.decode()


# 2.2、验证密码
def bcrypt_verify(password, hashed_password):
    """验证密码
    :param password: 密码
    :param hashed_password: 加密后的密码
    """
    password = bytes(password, encoding="utf-8")
    hashed_password = bytes(hashed_password, encoding="utf-8")
    return bcrypt.checkpw(password, hashed_password)       