from time import sleep

from selenium.webdriver.common.by import By

from utils.phone_util import Phone
from web.login_operator import LoginOperator
from model import unit_init
from utils.url import CardUrl


class InteractQrCodeTPlusQueryLoginTest(unit_init.Base):

    # 测试用户登陆
    def login(self, phone, code, url):
        # url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/mgm/index'
        LoginOperator(self.driver).interact_qr_code_tplus_query_login(phone, code, url)

    def phone_interact_error_text(self):
        interact_error_hint_loc = (By.XPATH, '//*[@id="app"]/div/ul/li[2]/div/div[3]/p')  # 交互式二维码的无权限弹框
        operator = LoginOperator(self.driver)
        return operator.get_text(interact_error_hint_loc)

    # 交互式二维码正常登陆
    def test_interact_plus(self):
        self.login('12345698755', 4484040029, CardUrl.INTERACT_QR_CODE_TPLUS_QUERY_LOGIN_URL)

    # 交互式二维码推广人代码为空时
    def test_interact_code_null(self):
        self.login('12345698755', "", CardUrl.INTERACT_QR_CODE_TPLUS_QUERY_LOGIN_URL)
        interact_error_hint_loc = (By.XPATH, '//*[@id="app"]/div/ul/li[1]/div/div[3]/p')
        operator = LoginOperator(self.driver)
        self.assertIn("推广人代码不能为空", operator.get_text(interact_error_hint_loc))

    # 交互式二维码查询人手机号码少一位
    def test_interact_code_miss(self):
        self.login('1234569875', "4484040029", CardUrl.INTERACT_QR_CODE_TPLUS_QUERY_LOGIN_URL)
        self.assertIn("查询人手机号输入有误", self.phone_interact_error_text())

    # 交互式二维码查询人手机号码有英文
    def test_interact_code_english(self):
        self.login('1234569875m', "4484040029", CardUrl.INTERACT_QR_CODE_TPLUS_QUERY_LOGIN_URL)
        self.assertIn("查询人手机号输入有误", self.phone_interact_error_text())
        sleep(1)

    # 交互式二维码查询人手机号码为空
    def test_interact_code_english_null(self):
        self.login('', "4484040029", CardUrl.INTERACT_QR_CODE_TPLUS_QUERY_LOGIN_URL)
        self.assertIn("查询人手机号不能为空", self.phone_interact_error_text())
        sleep(1)

    # 交互式二维码正常登陆,但没权限
    def test_interact_permission(self):
        self.login(Phone.create_phone(), 4484040029, CardUrl.INTERACT_QR_CODE_TPLUS_QUERY_LOGIN_URL)
        interact_error_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/p[2]')
        operator = LoginOperator(self.driver)
        self.assertIn("无权查询",  operator.get_text(interact_error_hint_loc))
