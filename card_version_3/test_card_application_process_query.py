from time import sleep
from selenium.webdriver.common.by import By
from utils.phone_util import Phone
from web.login_operator import LoginOperator
from model import unit_init
from utils import image_util
from utils.url import CardUrl


class CardNumberQueryTest(unit_init.Base):

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

    # 正常登陆
    def test_login_customer(self):
        self.login("512236197807102659", "15765484676", CardUrl.CARD_NUMBER_QUERY_LOGIN_URL)
        image_util.insert_img(self.driver, "customer_name.png")
        table = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/ul')
        trlist = self.driver.find_elements_by_tag_name('li')
        print(len(trlist))
        sleep(2)
        for row in trlist:
            if row.text == '申请日期：':
                self.assertIn(row.text, '申请日期：')
                print(row.text)
