from time import sleep

from login.login import Login
from model import unit_init
from utils import image_util
from utils.url import CardUrl


class CardNumberQueryLoginTest(unit_init.Base):

    # 测试用户登陆
    def login_verify(self, identity, phone, url):
        Login(self.driver).customer_progress(identity, phone, url)

    def test_login_customer(self):
        '''推荐结果登陆'''
        self.login_verify("512236197807102659", "15765484676", CardUrl.CARD_NUMBER_QUERY_LOGIN_URL)
        # self.assertIn()
        image_util.insert_img(self.driver, "customer_name.png")
        sleep(3)

    def test_login_identity_miss(self):
        '''推荐结果登陆失败，身份证少于18位'''
        self.login_verify("51223619780710265", "15765484670", CardUrl.CARD_NUMBER_QUERY_LOGIN_URL)
        sleep(2)
        po = Login(self.driver)
        sleep(3)
        self.assertIn("身份证号码有误，请确认", po.identity_error_hint())
        image_util.insert_img(self.driver, "identity_miss.png")
        sleep(3)

    def test_login_identity_null(self):
        '''推荐结果登陆失败，身份证为空'''
        self.login_verify("", "15765480006", CardUrl.CARD_NUMBER_QUERY_LOGIN_URL)
        sleep(2)
        po = Login(self.driver)
        sleep(3)
        self.assertIn("身份证号不能为空", po.identity_error_hint())
        image_util.insert_img(self.driver, "identity_null.png")
        sleep(1)

    def test_login_phone_miss(self):
        '''推荐结果登陆失败，手机好少于18位'''
        self.login_verify("110224199201305248", "1576548467", CardUrl.CARD_NUMBER_QUERY_LOGIN_URL)
        sleep(2)
        po = Login(self.driver)
        sleep(1)
        self.assertIn("手机号格式不正确", po.phone_error_hint())
        image_util.insert_img(self.driver, "phone_miss.png")
        sleep(2)

    def test_login_phone_null(self):
        '''推荐结果登陆失败，手机为空'''
        self.login_verify("110224199201305248", "", CardUrl.CARD_NUMBER_QUERY_LOGIN_URL)
        sleep(2)
        po = Login(self.driver)
        sleep(1)
        self.assertIn("手机号码不能为空", po.phone_error_hint())
        image_util.insert_img(self.driver, "phone_null.png")
        sleep(1)

    def test_login_phone_english(self):
        '''推荐结果登陆失败，手机不合法'''
        self.login_verify("110224199201305248", "1234567890m", CardUrl.CARD_NUMBER_QUERY_LOGIN_URL)
        sleep(2)
        po = Login(self.driver)
        sleep(1)
        self.assertIn("手机号格式不正确", po.phone_error_hint())
        image_util.insert_img(self.driver, "customer_name.png")
        sleep(1)

    def test_login_null(self):
        '''推荐结果登陆失败，身份证和手机号同时为空'''
        self.login_verify("", "", CardUrl.CARD_NUMBER_QUERY_LOGIN_URL)
        sleep(2)
        po = Login(self.driver)
        sleep(1)
        self.assertIn("手机号码不能为空", po.phone_error_hint())
        sleep(2)
        self.assertIn("身份证号不能为空", po.identity_error_hint())

        image_util.insert_img(self.driver, "customer_name.png")
        sleep(3)
