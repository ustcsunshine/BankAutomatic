from time import sleep

from selenium.webdriver.common.by import By

from web.login_operator import LoginOperator


class ApplyJobInfo(LoginOperator):

    def open_login(self, username, phone, root, degree, major, company, now_major, salary, recommand, recommand_phone, url):
        self.open(url)
        self.login(username, phone, root, degree, major, company,now_major, salary, recommand, recommand_phone)

    def login(self, username, phone, root, degree, major, company, now_major, salary, recommand, recommand_phone):
        sleep(1)
        self.send_keys(username, (By.XPATH, '//*[@id="candidatosName"]'))
        sleep(1)
        self.send_keys(phone, (By.XPATH, '//*[@id="mobile"]'))
        sleep(1)
        # self.send_keys(city, (By.XPATH, '//*[@id="recordPlace"]'))
        self.click((By.XPATH, '//*[@id="mid"]/div[6]/span'))
        sleep(1)
        self.click((By.XPATH, '//*[@id="mid"]/div[3]/div/div[1]/button[2]'))#确定按钮
        sleep(1)
        self.click((By.XPATH, '//*[@id="mid"]/div[9]/span'))
        sleep(1)
        self.click((By.XPATH, '//*[@id="h-picker"]/div/div[1]/div[2]'))#应聘岗位的确定按钮
        sleep(1)

        self.click((By.XPATH, '//*[@id="mid"]/div[11]/span'))
        sleep(1)
        self.click((By.XPATH, '//*[@id="h-picker"]/div/div[1]/div[2]'))#birth岗位的确定按钮
        sleep(1)
        self.send_keys(root, (By.XPATH, '//*[@id="nativePlace"]'))
        sleep(1)
        self.click((By.XPATH, '//*[@id="mid"]/div[14]/span'))
        sleep(1)
        self.click((By.XPATH, '//*[@id="h-picker"]/div/div[1]/div[2]'))#hight degree岗位的确定按钮
        sleep(1)

        self.send_keys(degree, (By.XPATH, '//*[@id="school"]'))
        sleep(1)
        self.send_keys(major, (By.XPATH, '//*[@id="major"]'))
        sleep(1)
        self.click((By.XPATH, '//*[@id="mid"]/div[17]/div[1]/span'))
        sleep(1)
        self.click((By.XPATH, '//*[@id="h-picker"]/div/div[1]/div[2]'))#start job岗位的确定按钮

        sleep(1)
        self.send_keys(company, (By.XPATH, '//*[@id="formerWorkUnit"]'))#
        sleep(1)
        self.send_keys(now_major, (By.XPATH, '//*[@id="formerWorkPosition"]'))

        self.send_keys(salary, (By.XPATH, '//*[@id="expectedSalary"]'))
        sleep(1)
        self.click((By.XPATH, '//*[@id="mid"]/div[19]/span'))#//*[@id="mid"]/div[17]/span
        sleep(1)
        self.click((By.XPATH, '//*[@id="h-picker"]/div/div[1]/div[2]'))
        sleep(2)
        self.send_keys(recommand, (By.XPATH, '//*[@id="referrer"]'))#
        sleep(1)
        self.send_keys(recommand_phone, (By.XPATH, '//*[@id="referrerMobile"]'))
        sleep(1)
        self.click((By.XPATH, '//*[@id="app"]/div/div[2]/p'))
        sleep(2)




