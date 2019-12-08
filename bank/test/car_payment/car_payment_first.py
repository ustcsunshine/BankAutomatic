from selenium.webdriver.common.by import By
from bank.utils.base import Page
from bank.login.login import Login
from time import sleep
from selenium.webdriver.support.select import Select



class CarPaymentBasicInfo(Login):


    def car_payment_basic_info(self,username, identity, salary, loan, url):
        res = self.open(url)
        if res is None:
            print('Please input right url')
            return
        self.login_username(username, (By.XPATH, '//input[@placeholder="请输入姓名"]'))
        sleep(1)
        self.login_identity(identity, (By.XPATH, '//input[@placeholder="请输入身份证号"]'))
        sleep(1)
        self.login_button((By.XPATH, '//*[@id="domicileaddress1"]'))
        sleep(1)
        self.login_button((By.XPATH, '/html/body/div[5]/div/div[1]/div/a')) # /html/body/div[5]/div/div[1]/div
        # sleep(2)
        self.annual_salary(salary, (By.XPATH, '//input[@placeholder="请输入车辆价格"]'))
        sleep(1)
        self.bank_loan(loan, (By.XPATH, '//input[@placeholder="请输入贷款金额"]'))
        sleep(1)
        # self.login_button((By.XPATH, '//*[@id="mid"]/div[6]/span'))
        self.login_button((By.XPATH, '//*[@id="picker"]'))
        sleep(1)
        # /html/body/div[5]/div/div[1]/div/a
        self.login_button((By.XPATH, '/html/body/div[5]/div/div[1]/div/a'))
        sleep(2)
        # /html/body/div[3]/span
        self.login_button((By.XPATH, '/html/body/div[3]/span/label'))
        sleep(1)
        self.login_button((By.XPATH, '//*[@id="bt"]'))


