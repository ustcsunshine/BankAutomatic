import sys
from time import sleep

from login.login import Login
from model import unit_init
from utils.url import CardUrl

sys.path.append("./model")
sys.path.append("./card_application")


class MgmGiftDeliveryLoginTest(unit_init.Base):

    # 测试用户登陆
    def login_verify(self, phone, url):
        Login(self.driver).gift_distribute(phone, url)

    def test_login_normal(self):
        '''正常登陆礼品配送登陆'''
        self.login_verify("13262576101", CardUrl.MGM_GIFT_DELIVERY_LOGIN_URL)
        message = self.driver.find_element_by_xpath('//*[@id="app"]/div/p[1]').text
        print(message)
        sleep(2)
        self.assertIn("礼品配送信息登记", message)
        sleep(1)


    def test_login_phone_miss(self):
        '''手机号少一位'''
        self.login_verify("1326257610", CardUrl.MGM_GIFT_DELIVERY_LOGIN_URL)
        sleep(1)
        po = Login(self.driver)
        sleep(1)
        self.assertIn("手机号输入有误", po.identity_error_hint())
        sleep(1)




    def test_login_phone_english(self):
        '''手机号不合法'''
        self.login_verify("1326257610m", CardUrl.MGM_GIFT_DELIVERY_LOGIN_URL)
        sleep(1)
        po = Login(self.driver)
        sleep(1)
        self.assertIn("手机号输入有误", po.identity_error_hint())
        sleep(1)


    def test_login_phone_null(self):
        '''手机号为空'''
        self.login_verify("", CardUrl.MGM_GIFT_DELIVERY_LOGIN_URL)
        sleep(1)
        po = Login(self.driver)
        sleep(1)
        self.assertIn("手机号不能为空", po.identity_error_hint())
        sleep(1)
        #//*[@id="app"]/div/div[3]/div/p[2]