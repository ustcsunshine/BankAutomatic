from selenium.webdriver.common.by import By
from login.login import Login
from time import sleep


class CarPaymentPersonalInfo(Login):

    def car_payment_personal_info(self, company, salary, url):
        res = self.open(url)
        if res is None:
            print('Please input right url')
            return
        self.personal_info(company, salary)

    def personal_info(self, company, salary):
        sleep(2)
        self.login_company(company, (By.XPATH, '//input[@placeholder="请输入工作单位名称"]'))
        sleep(1)
        self.login_button((By.XPATH, '//*[@id="industryPicker"]'))
        sleep(1)
        self.login_button((By.XPATH, '/html/body/div[4]/div/div[1]/div/a'))
        sleep(1)
        self.login_button((By.XPATH, '//*[@id="workPicker"]'))
        sleep(1)
        self.login_button((By.XPATH, '/html/body/div[4]/div/div[1]/div/a'))
        sleep(1)
        self.annual_salary(salary, (By.XPATH, '//*[@id="salary"]'))
        sleep(1)
        self.login_button((By.XPATH, '//*[@id="mid"]/div[5]/div[2]/label[2]'))
        # sleep(2)
        sleep(1)
        self.login_button((By.XPATH, '//*[@id="mid"]/div[7]/div[2]/label[2]'))
        sleep(1)
        self.login_button((By.XPATH, '//*[@id="mid"]/div[9]/div[2]/label[2]'))

        self.login_button((By.XPATH, '//*[@id="bt"]'))
        sleep(1)
