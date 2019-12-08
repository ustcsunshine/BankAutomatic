from selenium.webdriver.common.by import By
from bank.utils.base import Page
from bank.login.login import Login
from time import sleep




class OtherInfo(Login):


    def other_info(self, username, phone, email, url):
        res = self.open(url)
        if res is None:
            print('Please input right url')
            return

        # self.login_username(username, (By.XPATH, '//input[@placeholder="请输入亲属的姓名"]'))
        # sleep(1)
        # self.login_button((By.XPATH, '//*[@id="relation_A"]/span'))
        # sleep(1)
        # self.login_phone(phone, (By.XPATH, '//*[@id="relativetel"]'))
        # sleep(2)
        # self.e_mail(email,(By.XPATH, '//*[@id="e_mail"]'))
        # sleep(1)
        # self.login_button((By.XPATH, '//*[@id="sendaddress_B"]/span'))
        #
        # sleep(2)
        self.login_button((By.XPATH, '//*[@id="next"]'))
        sleep(1)
        print("-----")