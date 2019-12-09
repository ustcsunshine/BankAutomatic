from time import sleep

from selenium.webdriver.common.by import By

from bank.login.login import Login


class CarPaymentApplyInfo(Login):

    def car_payment_apply_info(self, phone, url):
        res = self.open(url)
        if res is None:
            print('Please input right url')
            return
        self.apply_info(phone)

    def apply_info(self, phone):
        self.login_phone(phone, (By.XPATH, '//input[@placeholder="请输手机号码"]'))
        self.login_sms((By.XPATH, '//*[@id="blue"]'))
        sleep(2)
        code = self.driver.find_element_by_xpath('//*[@id="smscode"]')
        print('code: ' + code.text)
        sleep(1)
        self.fill_login_sms((By.XPATH, '//*[@id="code"]'), code.text)
        sleep(1)
        self.login_button((By.XPATH, '//*[@id="bt"]'))
        sleep(2)
