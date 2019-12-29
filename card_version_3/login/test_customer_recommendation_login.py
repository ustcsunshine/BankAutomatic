from time import sleep

from selenium.webdriver.common.by import By

from web.login_operator import LoginOperator
from model import unit_init
from utils import image_util
from utils.url import CardUrl


class CustomerRecommendationLoginTest(unit_init.Base):

    # 测试用户登陆
    def login(self, username, phone, url, org=''):
        LoginOperator(self.driver).customer_recommendation_login(username, phone, url, org)

    def get_sms_error_text(self):
        sms_error_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[5]/div/p[2]')  # 推荐客户错误提示弹框定位
        operator = LoginOperator(self.driver)
        return operator.get_text(sms_error_hint_loc)

    # 正常登陆,有机构号1001
    def test_login_org_normal(self):
        self.login("李芽", "17000199918", CardUrl.CUSTOMER_RECO_LOGIN_URL, '1001')
        sleep(3)
        message = self.driver.find_element_by_xpath('//p[@id="copyright"]').text
        self.assertIn(u'©本服务由兴业银行信用卡中心提供', message)
        image_util.insert_img(self.driver, "user_pawd_true1.png")
        sleep(1)

    # 正常登陆,无机构号
    def test_login_org_null(self):
        self.login("李芽", "17000199917", CardUrl.CUSTOMER_RECO_LOGIN_URL)
        sleep(3)
        message = self.driver.find_element_by_xpath('//p[@id="copyright"]').text
        self.assertIn(u'©本服务由兴业银行信用卡中心提供 v3.6.9', message)
        image_util.insert_img(self.driver, "user_pawd_true2.png")
        sleep(1)

    # 用户名为空
    def test_login_null_name(self):
        self.login("", "17621523735", CardUrl.CUSTOMER_RECO_LOGIN_URL, '1001')
        sleep(3)
        self.assertIn("姓名为空或格式不正确", self.get_sms_error_text())
        image_util.insert_img(self.driver, "user_name_miss2.png")
        print('用户名为空，提示姓名为空或格式不正确')
        sleep(1)

    # 用户名为英文
    def test_login_english_name(self):
        self.login("jingj", "17621523731", CardUrl.CUSTOMER_RECO_LOGIN_URL, '1001')
        sleep(2)
        self.assertIn("姓名为空或格式不正确", self.get_sms_error_text())
        image_util.insert_img(self.driver, "user_name_miss3.png")
        print('用户名为拼音，提示姓名为空或格式不正确')
        sleep(1)

    # 用户名正确，手机号码少一位
    def test_login_numb_miss(self):
        self.login("李孝雪", "1762152373", CardUrl.CUSTOMER_RECO_LOGIN_URL, '1001')
        sleep(2)
        self.assertIn("手机号为空或格式不正确", self.get_sms_error_text())
        image_util.insert_img(self.driver, "user_numb_miss4.png")
        print('用户名正确，手机号码少一位')

    # 手机不正确，不是数字
    def test_login_numb_english(self):
        self.login("李孝雪", "1762152373m", CardUrl.CUSTOMER_RECO_LOGIN_URL, '1001')
        sleep(2)
        self.assertIn("验证码为空或格式不正确", self.get_sms_error_text())
        image_util.insert_img(self.driver, "user_numb_english5.png")
        print('手机不正确，不是数字')
