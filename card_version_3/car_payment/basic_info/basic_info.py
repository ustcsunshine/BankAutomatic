from time import sleep

from selenium.webdriver.common.by import By

from web.login_operator import LoginOperator


class CarPaymentBasicInfo(LoginOperator):
    def upload_click(self, url, location):
        self.open(url)
        sleep(1)
        self.click((By.XPATH, location))

    def upload_click_no_open(self, location):
        self.click((By.XPATH, location))

    def open_login(self, username, identity, salary, loan, url):
        self.open(url)
        self.login(username, identity, salary, loan)

    def login(self, username, identity, salary, loan):
        sleep(1)
        self.send_keys(username, (By.XPATH, '//input[@placeholder="请输入姓名"]'))
        sleep(1)
        self.send_keys(identity, (By.XPATH, '//input[@placeholder="请输入身份证号"]'))
        sleep(1)
        self.click((By.XPATH, '//*[@id="domicileaddress1"]'))
        sleep(1)
        self.click((By.XPATH, '/html/body/div[5]/div/div[1]/div/a'))
        # sleep(2)
        self.send_keys(salary, (By.XPATH, '//input[@placeholder="请输入车辆价格"]'))
        sleep(1)
        self.send_keys(loan, (By.XPATH, '//input[@placeholder="请输入贷款金额"]'))
        sleep(1)
        # self.login_button((By.XPATH, '//*[@id="mid"]/div[6]/span'))
        self.click((By.XPATH, '//*[@id="picker"]'))
        sleep(1)
        # /html/body/div[5]/div/div[1]/div/a
        self.click((By.XPATH, '/html/body/div[5]/div/div[1]/div/a'))
        sleep(2)
        # /html/body/div[3]/span
        self.click((By.XPATH, '/html/body/div[3]/span/label'))
        sleep(1)
        self.click((By.XPATH, '//*[@id="bt"]'))
