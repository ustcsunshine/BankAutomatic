from time import sleep

from selenium.webdriver.common.by import By

from web.login_operator import LoginOperator
from model import unit_init
from utils import image_util
from utils.url import CardUrl


class CardNumberQueryLoginTest(unit_init.Base):

    # 测试用户登陆
    def login(self, identity, phone, url):
        LoginOperator(self.driver).card_number_query_login(identity, phone, url)

    def get_identify_error_text(self):
        fast_identity_error_hint_loc = (By.XPATH, '//*[@id="app"]/div/ul/li[1]/div/div[3]/p ')  # 卡号进度申请查询错误提示弹框定位
        operator = LoginOperator(self.driver)
        return operator.get_text(fast_identity_error_hint_loc)

    def number_phone_error_text(self):
        phone_error_hint_loc = (By.XPATH, '//*[@id="app"]/div/ul/li[2]/div/div[3]/p')
        operator = LoginOperator(self.driver)
        return operator.get_text(phone_error_hint_loc)

    #正常登陆
    def test_login_customer(self):
        self.login("512236197807102659", "15765484676", CardUrl.CARD_NUMBER_QUERY_LOGIN_URL)
        image_util.insert_img(self.driver, "customer_name.png")
        sleep(1)

    #申请进度查询身份证少于18位
    def test_login_identity_miss(self):
        self.login("51223619780710265", "15765484670", CardUrl.CARD_NUMBER_QUERY_LOGIN_URL)
        sleep(1)
        self.assertIn("身份证号码有误，请确认", self.get_identify_error_text())
        image_util.insert_img(self.driver, "identity_miss.png")

    #申请进度查询身份证为空
    def test_login_identity_null(self):
        self.login("", "15765480006", CardUrl.CARD_NUMBER_QUERY_LOGIN_URL)
        sleep(1)
        self.assertIn("身份证号不能为空", self.get_identify_error_text())
        image_util.insert_img(self.driver, "identity_null.png")

    #申请进度查询手机号码少一位
    def test_login_phone_miss(self):
        self.login("110224199201305248", "1576548467", CardUrl.CARD_NUMBER_QUERY_LOGIN_URL)
        sleep(1)
        self.assertIn("手机号格式不正确", self.get_identify_error_text())
        image_util.insert_img(self.driver, "phone_miss.png")

    #申请进度查询手机号码为空
    def test_login_phone_null(self):
        self.login("110224199201305248", "", CardUrl.CARD_NUMBER_QUERY_LOGIN_URL)
        sleep(1)
        self.assertIn("手机号码不能为空", self.number_phone_error_text())
        image_util.insert_img(self.driver, "phone_null.png")
        sleep(1)

    #申请进度查询手机号码有英文
    def test_login_phone_english(self):
        self.login("110224199201305248", "1234567890m", CardUrl.CARD_NUMBER_QUERY_LOGIN_URL)
        self.assertIn("手机号格式不正确", self.number_phone_error_text())
        image_util.insert_img(self.driver, "customer_name.png")

    #申请进度查询手机号码有空格
    def test_login_phone_space(self):
        self.login("110224199201305248", "123456789 1", CardUrl.CARD_NUMBER_QUERY_LOGIN_URL)
        self.assertIn("手机号格式不正确", self.number_phone_error_text())
        image_util.insert_img(self.driver, "customer_name.png")

    #申请进度查询身份证和手机号同时为空
    def test_login_null(self):
        self.login("", "", CardUrl.CARD_NUMBER_QUERY_LOGIN_URL)
        self.assertIn("身份证号不能为空", self.get_identify_error_text())
        self.assertIn("手机号码不能为空", self.number_phone_error_text())
        image_util.insert_img(self.driver, "customer_name.png")
