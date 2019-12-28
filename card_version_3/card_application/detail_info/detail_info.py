from time import sleep

from selenium.webdriver.common.by import By

from web.element_operator import ElementOperator


class CardApplicationDetailInfo(ElementOperator):

    def fast_detail_info(self, company, area, line, departaddr, departname, salary, homeaddr, url):
        res = self.open(url)
        if res is None:
            print('Please input right url')
            return
        self.detail_info(company, area, line, departaddr, departname, salary, homeaddr)

    def detail_info(self, company, area, line, departaddr, departname, salary, homeaddr):
        sleep(2)
        self.send_keys(company, (By.XPATH, '//input[@placeholder="请输入您现单位名称"]'))

        self.send_keys(area, (By.XPATH, '//input[@placeholder="单位区号"]'))
        sleep(1)
        self.send_keys(line, (By.XPATH, '//input[@placeholder="单位电话"]'))
        sleep(1)
        self.send_keys(departaddr, (By.XPATH, '//input[@placeholder="请输入详细单位地址(22个字内)"]'))
        self.send_keys(departname, (By.XPATH, '//input[@placeholder="请输入您任职的部门"]'))
        sleep(1)
        self.click((By.XPATH, '//*[@id="workvocation"]'))  # 行业类别旁边的按钮
        sleep(2)
        self.click((By.XPATH, '//*[@id="career"]/div/div[2]/div[2]/ul/li[2]/p'))  # 行业类别第一个默认行业
        sleep(1)
        self.click((By.XPATH, '//*[@id="postSelect"]'))  # 个人职务
        sleep(1)
        self.click((By.XPATH, '/html/body/div[7]/div/div[1]/div/a'))  # 个人职务的完成
        sleep(1)
        self.click((By.XPATH, '//*[@id="workingYearsSelect"]'))  # 工作年限
        sleep(1)
        self.click((By.XPATH, '/html/body/div[7]/div/div[1]/div/a'))  # 工作年限的完成
        sleep(1)
        self.send_keys(salary, (By.XPATH, '//input[@placeholder="请输入您的年收入"]'))
        sleep(1)
        self.click((By.XPATH, '//*[@id="marriage_A"]/span'))
        sleep(1)
        self.click((By.XPATH, '//*[@id="education_A"]/span'))
        sleep(1)
        self.send_keys(homeaddr, (By.XPATH, '//input[@placeholder="请输入详细住宅地址(22个字内)"]'))

        sleep(1)
        self.click((By.XPATH, '//*[@id="next"]'))
        sleep(1)
