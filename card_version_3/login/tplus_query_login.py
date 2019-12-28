from time import sleep

from login.login import Login
from model import unit_init
from utils.url import CardUrl


class TPlusQueryLoginTest(unit_init.Base):

    # 测试用户登陆
    def login_verify(self, phone, url, org):
        Login(self.driver).t_recommendation(phone, url, org)

    # 推荐结果登陆
    def test_t_login_normal(self):
        self.login_verify("17621523736", CardUrl.SOURCE_RECOMMENDATION_RESULT_QUERY_LOGIN_URL, 1001)

    # 手机号码少一位
    def test_t_phone_miss(self):
        self.login_verify("120000001", CardUrl.SOURCE_RECOMMENDATION_RESULT_QUERY_LOGIN_URL, 1001)
        po = Login(self.driver)
        sleep(1)
        self.assertIn("手机号输入有误", po.phone_error_hint())

    # 手机号码有英文
    def test_t_phone_english(self):
        self.login_verify("120000001m", CardUrl.SOURCE_RECOMMENDATION_RESULT_QUERY_LOGIN_URL, 1001)
        po = Login(self.driver)
        sleep(1)
        self.assertIn("手机号输入有误", po.phone_error_hint())

    # 手机号码null
    def test_phone_ull(self):
        self.login_verify("", CardUrl.SOURCE_RECOMMENDATION_RESULT_QUERY_LOGIN_URL, 1001)
        po = Login(self.driver)
        self.assertIn("手机号不能为空", po.phone_error_hint())

    # 手机号码有空格
    def test_phone_miss(self):
        self.login_verify("123456 1234", CardUrl.SOURCE_RECOMMENDATION_RESULT_QUERY_LOGIN_URL, 1001)
        po = Login(self.driver)
        sleep(1)
        self.assertIn("手机号输入有误", po.identity_error_hint())
