import sys
from time import sleep

from selenium.webdriver.common.by import By

from utils.url import CardUrl
from web.login_operator import LoginOperator
from model import unit_init

sys.path.append("./model")
sys.path.append("./card_application")


class MgmPersonalizationLoginTest(unit_init.Base):

    # 测试用户登陆
    def login(self, phone, username, url, org):
        LoginOperator(self.driver).mgm_recommendation_login(phone, username, url, org)

    def get_phone_error_text(self):
        phone_error_hint_loc = (By.XPATH, '//*[@id="app"]/div/ul/li[1]/div/div[3]/p')
        operator = LoginOperator(self.driver)
        return operator.get_text(phone_error_hint_loc)

    def get_org_error_text(self):
        mgm_login_loc = (By.XPATH, '//*[@id="app"]/div/ul/li[3]/div/div[3]/p')  # 合作方代码错误提示
        operator = LoginOperator(self.driver)
        return operator.get_text(mgm_login_loc)

    # 推荐结果登陆
    def test_login_phone_normal(self):
        self.login("13262576102", "窦路路", CardUrl.MGM_PERSONALIZATION_URL, 1002)
        sleep(1)

    # 手机号码少一位
    def test_login_phone_miss(self):
        self.login("1326257610", "窦路路", CardUrl.MGM_PERSONALIZATION_URL, 1002)
        sleep(1)
        self.assertIn("手机号输入有误", self.get_phone_error_text())

    # 手机号为空
    def test_login_phone_null(self):
        self.login("", "窦路路", CardUrl.MGM_PERSONALIZATION_URL, 1002)
        sleep(1)
        self.assertIn("手机号不能为空", self.get_phone_error_text())

    # 合作方代码输入英文
    def test_login_org_english(self):
        self.login("12000000009", "窦路路", CardUrl.MGM_PERSONALIZATION_URL, "fff")
        sleep(1)
        self.assertIn("合作方代码输入有误", self.get_org_error_text())

    # 合作方代码null
    def test_login_org_english_null(self):
        self.login("12000000005", "窦路路", CardUrl.MGM_PERSONALIZATION_URL, "")
        sleep(1)
        self.assertIn("合作方代码不能为空", self.get_org_error_text())
