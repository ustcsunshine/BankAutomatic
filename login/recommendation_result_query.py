from test.models import myunit
from login.login import Login

from time import sleep
import sys

sys.path.append("./models")
sys.path.append("./page_obj")


class RecommendationResultQueryTest(myunit.MyTest):

    # 测试用户登陆
    def user_login_verify(self, phone, url):
        Login(self.driver).login_recommendation(phone, url)

    # 推荐结果正常登陆
    def test_login_normal(self):
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/recommendResult/index'
        self.user_login_verify("12000000101", url)

    # 手机号码少一位
    def test_phone_miss(self):
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/recommendResult/index'
        self.user_login_verify("1200000010", url)
        po = Login(self.driver)
        sleep(1)
        self.assertIn("手机号格式不正确", po.identity_error_hint())

    # 手机号码有英文
    def test_phone_english(self):
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/recommendResult/index'
        self.user_login_verify("120000001m", url)
        po = Login(self.driver)
        sleep(1)
        self.assertIn("手机号格式不正确", po.identity_error_hint())

    # 手机号码null
    def test_phone_ull(self):
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/recommendResult/index'
        self.user_login_verify("", url)
        po = Login(self.driver)
        sleep(1)
        self.assertIn("手机号码不能为空", po.identity_error_hint())

    # 手机号码有空格
    def test_phone_miss(self):
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/recommendResult/index'
        self.user_login_verify("12345 67676", url)
        po = Login(self.driver)
        sleep(1)
        self.assertIn("手机号格式不正确", po.identity_error_hint())
