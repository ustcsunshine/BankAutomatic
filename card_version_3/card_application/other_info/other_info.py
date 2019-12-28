from time import sleep

from selenium.webdriver.common.by import By

from web.element_operator import ElementOperator


class CardApplicationOtherInfo(ElementOperator):

    def fast_other_info(self, username, phone, email, url):
        res = self.open(url)
        if res is None:
            print('Please input right url')
            return
        self.other_info(username, phone, email)

    def other_info(self, username, phone, email):
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
