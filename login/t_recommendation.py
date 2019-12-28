from test.models import myunit
from login.login import Login

from time import sleep


class TRecommendationTest(myunit.MyTest):

    # 测试用户登陆
    def t_login_verify(self, phone, url, org):
        # url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/mgm/index'
        #
        Login(self.driver).t_recommendation(phone, url, org)

    # 推荐结果登陆
    def test_t_login_normal(self):
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/tplus0/index'
        self.t_login_verify("17621523736", url, 1001)

    # 手机号码少一位
    def test_t_phone_miss(self):
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/tplus0/index'
        self.t_login_verify("120000001", url, 1001)
        po = Login(self.driver)
        sleep(1)
        self.assertIn("手机号输入有误", po.phone_error_hint())

    # 手机号码有英文
    def test_t_phone_english(self):
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/tplus0/index'
        self.t_login_verify("120000001m", url, 1001)
        po = Login(self.driver)
        sleep(1)
        self.assertIn("手机号输入有误", po.phone_error_hint())

    # 手机号码null
    def test_phone_ull(self):
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/tplus0/index'
        self.t_login_verify("", url, 1001)
        po = Login(self.driver)
        self.assertIn("手机号不能为空", po.phone_error_hint())

    # 手机号码有空格
    def test_phone_miss(self):
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/tplus0/index'
        self.t_login_verify("123456 1234", url, 1001)
        po = Login(self.driver)
        sleep(1)
        self.assertIn("手机号输入有误", po.identity_error_hint())




