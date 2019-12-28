from selenium.webdriver.common.by import By
from web.element_operator import ElementOperator
from time import sleep


class CardApplicationBasicInfo(ElementOperator):

    def basic_info(self, username, identity, phone, url):
        res = self.open(url)
        if res is None:
            print('Please input right url')
            return
        self.base_info(username, identity, phone)

    def base_info(self, username, identity, phone):
        sleep(2)
        self.click((By.XPATH, '//*[@id="shenqing"]'))

        self.send_keys(username, (By.XPATH, '//input[@placeholder="请输入身份证上的姓名"]'))
        sleep(1)
        self.send_keys(identity, (By.XPATH, '//input[@placeholder="请输入您的18位身份证号码"]'))
        sleep(1)
        self.send_keys(phone, (By.XPATH, '//*[@id="tel"]'))
        sleep(1)
        self.click((By.XPATH, '//button[@id="yz"]'))
        sleep(2)
        code = self.driver.find_element_by_xpath('//*[@id="smsCodeShow"]')
        print('code: ' + code.text)

        sleep(1)
        self.send_keys((By.XPATH, '//*[@id="identifyCode"]'), code.text)
        sleep(3)
        self.click((By.XPATH, '//*[@id="next"]'))
        sleep(2)
