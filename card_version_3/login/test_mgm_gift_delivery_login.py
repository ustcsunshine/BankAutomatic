import sys
from time import sleep

from selenium.webdriver.common.by import By

from model import unit_init
from utils.phone_util import Phone
from utils.url import CardUrl
from web.login_operator import LoginOperator

sys.path.append("./model")
sys.path.append("./card_application")


class MgmGiftDeliveryLoginTest(unit_init.Base):

    # 验证用户登陆
    def login(self, phone, url):
        LoginOperator(self.driver).mgm_gift_delivery_login(phone, url)

    def mgm_phone_error_text(self):
        phone_error_hint_loc = (By.XPATH, '//*[@id="app"]/div/ul/li[1]/div/div[3]/p')
        operator = LoginOperator(self.driver)
        return operator.get_text(phone_error_hint_loc)

    #正常登陆礼品配送登陆
    def test_login_normal(self):
        self.login(Phone.create_phone(), CardUrl.MGM_GIFT_DELIVERY_LOGIN_URL)
        message = self.driver.find_element_by_xpath('//*[@id="app"]/div/p[1]').text
        print(message)
        sleep(1)
        self.assertIn("礼品配送信息登记", message)

    #手机号少一位
    def test_login_phone_miss(self):
        self.login("1326257610", CardUrl.MGM_GIFT_DELIVERY_LOGIN_URL)
        sleep(1)
        self.assertIn("手机号输入有误", self.mgm_phone_error_text())

    #手机号不合法,有英文
    def test_login_phone_english(self):
        self.login("1326257610m", CardUrl.MGM_GIFT_DELIVERY_LOGIN_URL)
        sleep(1)
        self.assertIn("手机号输入有误", self.mgm_phone_error_text())

    #手机号为空
    def test_login_phone_null(self):
        self.login("", CardUrl.MGM_GIFT_DELIVERY_LOGIN_URL)
        self.assertIn("手机号不能为空", self.mgm_phone_error_text())
        sleep(1)
