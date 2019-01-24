import allure


def test_a():
    print("[aasfsdafas")
    assert 1

@allure.step(title = '测试登录的流程')
def test_b():
    allure.attach("登录","输入用户名")
    print("sdfsdfsdfsd") #找登录名
    allure.attach("登录", "输入密码")
    print("sdfsdfsdfsd")  # 找密码
    allure.attach("登录", "点击登录")
    print("sdfsdfsdfsd")  # 登录
    allure.attach("登录", "在来一步")
    print("testsetset")
    assert 0

@allure.step(title = 'test登录')
def test_c():
    allure.attach("注销", "第一步")
    print("第一步")
    allure.attach("注销", "第二步")
    print("第二步")
    allure.attach("注销", "第三步")
    print("第三步")
    assert 1
