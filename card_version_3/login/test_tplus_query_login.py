from time import sleep

from selenium.webdriver.common.by import By

from model import unit_init
from utils.url import CardUrl
from web.login_operator import LoginOperator


class TPlusQueryLoginTest(unit_init.Base):

    # 测试用户登陆
    def login(self, phone, url, org):
        LoginOperator(self.driver).tplus_query_login(phone, url, org)

    def get_phone_error_text(self):
        phone_error_hint_loc = (By.XPATH, '//*[@id="app"]/div/ul/li[2]/div/div[3]/p')
        operator = LoginOperator(self.driver)
        return operator.get_text(phone_error_hint_loc)

    # 推荐结果登陆
    def test_t_login_normal(self):
        self.login("17621523736", CardUrl.SOURCE_RECOMMENDATION_RESULT_QUERY_LOGIN_URL, 1001)

    # 手机号码少一位
    def test_t_phone_miss(self):
        self.login("120000001", CardUrl.SOURCE_RECOMMENDATION_RESULT_QUERY_LOGIN_URL, 1001)
        self.assertIn("手机号输入有误", self.get_phone_error_text())

    # 手机号码有英文
    def test_t_phone_english(self):
        self.login("120000001m", CardUrl.SOURCE_RECOMMENDATION_RESULT_QUERY_LOGIN_URL, 1001)
        self.assertIn("手机号输入有误", self.get_phone_error_text())

    # 手机号码null
    def test_phone_null(self):
        self.login("", CardUrl.SOURCE_RECOMMENDATION_RESULT_QUERY_LOGIN_URL, 1001)
        self.assertIn("手机号不能为空", self.get_phone_error_text())

    # 手机号码有空格
    def test_phone_space(self):
        self.login("123456 1234", CardUrl.SOURCE_RECOMMENDATION_RESULT_QUERY_LOGIN_URL, 1001)
        self.assertIn("手机号输入有误", self.get_phone_error_text())
