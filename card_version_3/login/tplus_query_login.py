from time import sleep

from model import unit_init
from utils.url import CardUrl
from web.login_operator import LoginOperator


class TPlusQueryLoginTest(unit_init.Base):

    # 测试用户登陆
    def login(self, phone, url, org):
        LoginOperator(self.driver).tplus_query_login(phone, url, org)

    # 推荐结果登陆
    def test_t_login_normal(self):
        self.login("17621523736", CardUrl.SOURCE_RECOMMENDATION_RESULT_QUERY_LOGIN_URL, 1001)

    # 手机号码少一位
    def test_t_phone_miss(self):
        self.login("120000001", CardUrl.SOURCE_RECOMMENDATION_RESULT_QUERY_LOGIN_URL, 1001)
        po = LoginOperator(self.driver)
        sleep(1)
        self.assertIn("手机号输入有误", po.phone_error_hint())

    # 手机号码有英文
    def test_t_phone_english(self):
        self.login("120000001m", CardUrl.SOURCE_RECOMMENDATION_RESULT_QUERY_LOGIN_URL, 1001)
        po = LoginOperator(self.driver)
        sleep(1)
        self.assertIn("手机号输入有误", po.phone_error_hint())

    # 手机号码null
    def test_phone_ull(self):
        self.login("", CardUrl.SOURCE_RECOMMENDATION_RESULT_QUERY_LOGIN_URL, 1001)
        po = LoginOperator(self.driver)
        self.assertIn("手机号不能为空", po.phone_error_hint())

    # 手机号码有空格
    def test_phone_miss(self):
        self.login("123456 1234", CardUrl.SOURCE_RECOMMENDATION_RESULT_QUERY_LOGIN_URL, 1001)
        po = LoginOperator(self.driver)
        sleep(1)
        self.assertIn("手机号输入有误", po.phone_format_text())
