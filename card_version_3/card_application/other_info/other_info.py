from time import sleep

from selenium.webdriver.common.by import By

from web.login_operator import LoginOperator


class CardApplicationOtherInfo(LoginOperator):

    def open_login(self, username, phone, email, url):
        self.open(url)
        self.login(username, phone, email)

    def login(self, username, phone, email):
        sleep(2)
        self.send_keys(username, (By.XPATH, '//input[@placeholder="请输入亲属的姓名"]'))
        sleep(1)
        self.click((By.XPATH, '//*[@id="relation_A"]/span'))
        sleep(1)
        self.send_keys(phone, (By.XPATH, '//*[@id="relativetel"]'))
        sleep(2)
        self.send_keys(email, (By.XPATH, '//*[@id="e_mail"]'))
        sleep(1)
        self.click((By.XPATH, '//*[@id="sendaddress_B"]/span'))

        sleep(2)
        self.click((By.XPATH, '//*[@id="next"]'))
        sleep(3)
        print("-----")
