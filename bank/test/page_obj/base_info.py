from selenium.webdriver.common.by import By
from bank.utils.base import Page
from bank.login.login import Login
from time import sleep


class BaseInfo(Login):

    def fast_base_info(self, username, identity, phone, url):
        res = self.open(url)
        if res is None:
            print('Please input right url')
            return
        self.base_info(username, identity, phone)

    def base_info(self, username, identity, phone):
        sleep(2)
        self.login_button((By.XPATH, '//*[@id="shenqing"]'))

        self.login_username(username, (By.XPATH, '//input[@placeholder="请输入身份证上的姓名"]'))
        sleep(1)
        self.login_identity(identity, (By.XPATH, '//input[@placeholder="请输入您的18位身份证号码"]'))
        sleep(1)
        self.login_phone(phone, (By.XPATH, '//*[@id="tel"]'))
        sleep(1)
        self.login_sms((By.XPATH, '//button[@id="yz"]'))
        sleep(2)
        code = self.driver.find_element_by_xpath('//*[@id="smsCodeShow"]')
        print('code: ' + code.text)

        sleep(1)
        self.fill_login_sms((By.XPATH, '//*[@id="identifyCode"]'), code.text)
        sleep(3)
        self.login_button((By.XPATH, '//*[@id="next"]'))
        sleep(2)
