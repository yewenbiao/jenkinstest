import allure
import pytest


def test_a():
    print("[aasfsdafas")
    assert 1

@allure.step(title = '前置条件')
@pytest.fixture()
def qianzhitiaojian():
    allure.attach("前置条件","加载驱动")
    print("testestsete前置条件")

@allure.step(title = '测试登录的流程')
@pytest.mark.parametrize("content",["登录1"])
def test_b(content,qianzhitiaojian):
    allure.attach(content,"输入用户名")
    print("sdfsdfsdfsd") #找登录名
    allure.attach(content, "输入密码")
    print("sdfsdfsdfsd")  # 找密码
    allure.attach(content, "点击登录")
    print("sdfsdfsdfsd")  # 登录
    allure.attach("登录", "在来一步")
    print("testsetset")
    assert 1


@pytest.fixture()
def houzhitiaojian():
    print("后置条件")

@allure.step(title = 'test登录')
def test_c():
    allure.attach("注销", "第一步")
    print("第一步")
    allure.attach("注销", "第二步")
    print("第二步")
    allure.attach("注销", "第三步")
    print("第三步")
    assert 1
