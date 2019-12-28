import sys
from time import sleep

from login.login import Login
from model import unit_init

sys.path.append("./model")
sys.path.append("./card_application")


class MgmPersonalizationLoginTest(unit_init.Base):

    # 测试用户登陆
    def mgm_login_verify(self, phone, username, url, org):
        Login(self.driver).mgm_recommendation(phone, username, url, org)

    # 推荐结果登陆
    def test_login_phone_normal(self):
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/mgm/index'
        self.mgm_login_verify("13262576102", "窦路路", url, 1002)
        sleep(1)

    # 手机号码少一位
    def test_login_phone_miss(self):
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/mgm/index'
        self.mgm_login_verify("1326257610", "窦路路", url, 1002)
        sleep(1)
        po = Login(self.driver)
        sleep(1)
        self.assertIn("手机号输入有误", po.identity_error_hint())

    # 手机号为空
    def test_login_phone_null(self):
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/mgm/index'
        self.mgm_login_verify("", "窦路路", url, 1002)
        sleep(1)
        po = Login(self.driver)
        sleep(1)
        self.assertIn("手机号不能为空", po.identity_error_hint())

    # 合作方代码输入英文
    def test_login_org_english(self):
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/mgm/index'
        self.mgm_login_verify("12000000009", "窦路路", url, "fff")
        sleep(1)
        po = Login(self.driver)
        sleep(1)
        self.assertIn("合作方代码输入有误", po.org_error_hint())

    # 合作方代码null
    def test_login_org_english(self):
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/mgm/index'
        self.mgm_login_verify("12000000005", "窦路路", url, "")
        sleep(1)
        po = Login(self.driver)
        sleep(1)
        self.assertIn("合作方代码不能为空", po.org_error_hint())
