from time import sleep

from selenium.webdriver.common.by import By

from web.login_operator import LoginOperator


class CarPaymentPersonalInfo(LoginOperator):

    def open_login(self, company, salary, url):
        self.open(url)
        self.login(company, salary)

    def login(self, company, salary):
        sleep(2)
        self.send_keys(company, (By.XPATH, '//input[@placeholder="请输入工作单位名称"]'))
        sleep(1)
        self.click((By.XPATH, '//*[@id="industryPicker"]'))
        sleep(1)
        self.click((By.XPATH, '/html/body/div[4]/div/div[1]/div/a'))
        sleep(1)
        self.click((By.XPATH, '//*[@id="workPicker"]'))
        sleep(1)
        self.click((By.XPATH, '/html/body/div[4]/div/div[1]/div/a'))
        sleep(1)
        self.send_keys(salary, (By.XPATH, '//*[@id="salary"]'))
        sleep(1)
        self.click((By.XPATH, '//*[@id="mid"]/div[5]/div[2]/label[2]'))
        # sleep(2)
        sleep(1)
        self.click((By.XPATH, '//*[@id="mid"]/div[7]/div[2]/label[2]'))
        sleep(1)
        self.click((By.XPATH, '//*[@id="mid"]/div[9]/div[2]/label[2]'))

        self.click((By.XPATH, '//*[@id="bt"]'))
        sleep(1)
