from user import User
from card import Card
from helper import Helper


# 操作类
class Operate:
    def __init__(self, userinfo={}):
        # 用户存放所有的用户信息
        self.userinfo = userinfo

    # 开户
    def new_user(self):
        name = input('请输入姓名:')
        uid = input('请输入身份证:')
        pwd = input('请输入密码:')
        # 密码加密
        pwd = Helper.generate_password_hash(pwd)
        # 生成随机卡号
        cid = Helper.generate_cid()
        # 创建银行卡
        card = Card(cid, pwd)
        # 创建用户
        user = User(uid, name, card)
        # 保存用户信息
        self.userinfo[cid] = user
        # 保存用户信息到文件
        User.save_user(self.userinfo)
        print('开户成功')

    # 销户
    def del_user(self):
        print('销户成功')

    # 查询
    def query_money(self):
        cid = input('请输入您的卡号:')
        user = self.userinfo.get(cid)
        if user:
            print('您的余额为:', user.card.money)
        else:
            print('无效的卡号')

    # 转账
    def transfer_money(self):
        cid = input('请输入您的卡号:')
        user = self.userinfo.get(cid)
        if user:
            dst_cid = input('请输入对方卡号:')
            dst_user = self.userinfo.get(dst_cid)
            if dst_user:
                money = float(input('请输入转账金额:'))
                # 判断余额是否充足
                if user.card.money < money:
                    print('余额不足，转账失败')
                    return
                pwd = input('请输入密码:')
                if Helper.check_password_hash(pwd, user.card.pwd):
                    user.card.money -= money
                    dst_user.card.money += money
                    User.save_user(self.userinfo)
                    print('转账成功')
                else:
                    print('密码有误，转账失败')
            else:
                print('无效的卡号')
        else:
            print('无效的卡号')

    # 存款
    def save_money(self):
        cid = input('请输入您的卡号:')
        user = self.userinfo.get(cid)
        if user:
            # 查看用户是否锁定
            if user.card.is_lock:
                print('该卡已锁定，请先去解锁')
                return
            # 记录密码错误次数
            count = 0
            while count < 3:
                pwd = input('请输入密码:')
                if Helper.check_password_hash(pwd, user.card.pwd):
                    money = input('请输入您的存款金额:')
                    user.card.money += float(money)
                    User.save_user(self.userinfo)
                    print('存款成功')
                    break
                else:
                    count += 1
                    print('密码有误，请重新输入')
            else:
                user.card.is_lock = True
                User.save_user(self.userinfo)
                print('密码错误已达上限，该卡已锁定')
        else:
            print('无效的卡号')

    # 取款
    def get_money(self):
        print('取款成功')

    # 改密
    def change_pwd(self):
        print('密码修改成功')

    # 锁定
    def lock_user(self):
        print('用户锁定')

    # 解锁
    def unlock_user(self):
        cid = input('请输入卡号:')
        user = self.userinfo.get(cid)
        if user:
            user.card.is_lock = False
            User.save_user(self.userinfo)
            print('解锁成功')
        else:
            print('无效的卡号')

    # 显示所有用户信息
    def show_users(self):
        for user in self.userinfo.values():
            print(user)
