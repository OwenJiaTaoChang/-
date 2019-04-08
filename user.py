import os
import pickle


# 用户类
class User:
    def __init__(self, uid, name, card):
        self.uid = uid  # 身份证
        self.name = name  # 姓名
        self.card = card  # 银行卡

    def __str__(self):
        return '姓名:{},身份证:{},卡号:{}'.format(self.name, self.uid, self.card.cid)

    # 将用户信息序列化存储
    @staticmethod
    def save_user(userinfo):
        pathname = os.path.join(os.getcwd(), 'userinfo.db')
        with open(pathname, 'wb') as fp:
            pickle.dump(userinfo, fp)

    # 从文件中加载用户信息
    @staticmethod
    def load_user():
        pathname = os.path.join(os.getcwd(), 'userinfo.db')
        # 判断是否存在
        if os.path.exists(pathname):
            with open(pathname, 'rb') as fp:
                userinfo = pickle.load(fp)
            return userinfo
        return {}
