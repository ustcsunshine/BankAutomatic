from time import sleep

from selenium.webdriver.common.by import By

from web.login_operator import LoginOperator


class CarPaymentApplyInfo(LoginOperator):

    def open_login(self, phone, url):
        self.open(url)
        self.login(phone)

    def login(self, phone):
        sleep(1)
        self.send_keys(phone, (By.XPATH, '//input[@placeholder="请输手机号码"]'))
        self.click((By.XPATH, '//*[@id="blue"]'))
        sleep(2)
        code = self.driver.find_element_by_xpath('//*[@id="smscode"]')
        print('code: ' + code.text)
        sleep(1)
        self.send_keys((By.XPATH, '//*[@id="code"]'), code.text)
        sleep(1)
        self.click((By.XPATH, '//*[@id="bt"]'))
        sleep(2)
