import hashlib
from random import randint


# 助手函数类
class Helper:
    # 生成银行卡号
    @staticmethod
    def generate_cid(length=8):
        cid = ''
        for i in range(length):
            cid += str(randint(0, 9))
        return cid

    # 加密密码
    @staticmethod
    def generate_password_hash(password):
        # 创建加密对象
        m = hashlib.md5()
        # 设置加密字符串
        m.update(password.encode('utf-8'))
        # 返回加密字符串
        return m.hexdigest()

    # 检验密码
    @staticmethod
    def check_password_hash(pwd, pwd_hash):
        m = hashlib.md5()
        m.update(pwd.encode('utf-8'))
        return m.hexdigest() == pwd_hash
