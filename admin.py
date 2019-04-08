# 管理员类
class Admin:
    def __init__(self, account='admin', password='123456'):
        self.account = account
        self.password = password

    # 显示欢迎信息
    def welcome(self):
        print('*' * 30)
        print(' ' * 5 + '欢迎使用XX银行管理系统')
        print('*' * 30)

    # 登录页面
    def login(self):
        account = input('请输入账号:')
        password = input('请输入密码:')
        if account == self.account and password == self.password:
            return True
        return False

    # 操作菜单
    def menu(self):
        print('*' * 30)
        print('开户[1] 销户[2] 查询[3] 存款[4]')
        print('取款[5] 转账[6] 改密[7] 锁定[8]')
        print('解锁[9] 退出[0] 显示所有用户[10]')
        print('*' * 30)
