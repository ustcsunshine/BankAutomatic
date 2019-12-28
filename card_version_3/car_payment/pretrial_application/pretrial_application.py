from time import sleep

from selenium.webdriver.common.by import By

from web.element_operator import ElementOperator


class CarPaymentApplyInfo(ElementOperator):

    def car_payment_apply_info(self, phone, url):
        res = self.open(url)
        if res is None:
            print('Please input right url')
            return
        self.apply_info(phone)

    def apply_info(self, phone):
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
