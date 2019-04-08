from user import User
from admin import Admin
from operate import Operate

if __name__ == '__main__':
    # 记录管理员登录失败次数，若达到3次则直接结束
    count = 0
    # 创建管理员对象
    admin = Admin()
    while True:
        # 显示欢迎页面
        admin.welcome()
        # 登录检查
        ret = admin.login()
        if ret:
            # 记录是否退出
            is_quit = False
            # 先从文件中加载用户信息
            userinfo = User.load_user()
            # 创建操作对象
            op = Operate(userinfo)
            while True:
                # 显示操作菜单
                admin.menu()
                # 获取用户的操作
                num = int(input('请选择操作:'))
                if num == 0:
                    print('退出')
                    is_quit = True
                    break
                elif num == 1:
                    op.new_user()
                elif num == 2:
                    op.del_user()
                elif num == 3:
                    op.query_money()
                elif num == 4:
                    op.save_money()
                elif num == 5:
                    op.get_money()
                elif num == 6:
                    op.transfer_money()
                elif num == 7:
                    op.change_pwd()
                elif num == 8:
                    op.lock_user()
                elif num == 9:
                    op.unlock_user()
                elif num == 10:
                    op.show_users()
                else:
                    print('操作代号有误，请重新输入')
            if is_quit:
                break
        else:
            print('账户或密码有误，登录失败')
            count += 1
            if count >= 3:
                print('错误已达上限，禁止登录')
                break
    print('OVER')
