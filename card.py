# 银行卡类
class Card:
    def __init__(self, cid, pwd):
        self.cid = cid          # 卡号
        self.pwd = pwd          # 密码
        self.money = 0          # 金额
        self.is_lock = False    # 是否锁定
