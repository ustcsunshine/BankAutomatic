from selenium.webdriver.common.by import By
from web.login_operator import LoginOperator
from time import sleep


class CardApplicationBasicInfo(LoginOperator):

    def open_login(self, username, identity, phone, url):
        self.open(url)
        self.login(username, identity, phone)

    def login(self, username, identity, phone):
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
        self.send_keys(code.text, (By.XPATH, '//*[@id="identifyCode"]'))
        sleep(1)
        self.click((By.XPATH, '/html/body/div[8]/img'))
        sleep(1)
        self.click((By.XPATH, '//*[@id="next"]'))
        sleep(2)
