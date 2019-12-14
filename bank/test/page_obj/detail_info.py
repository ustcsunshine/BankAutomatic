from selenium.webdriver.common.by import By
from bank.utils.base import Page
from bank.login.login import Login
from time import sleep




class DetailInfo(Login):


    def fast_detail_info(self, company, area, line, departaddr, departname, salary, homeaddr, url):
        # url = 'https://test.xliane.com/html/webapp/fast-issue-con/process_one.html'
         # second_page = self.process_first_page("测试书记", "512236197807102659", "15765484677", url)
        #
        res = self.open(url)
        if res is None:
            print('Please input right url')
            return
        self.detail_info(company, area, line, departaddr, departname, salary, homeaddr)




    def detail_info(self, company, area, line, departaddr, departname, salary, homeaddr):
        sleep(2)
        self.login_company(company, (By.XPATH, '//input[@placeholder="请输入您现单位名称"]'))

        self.area_code(area, (By.XPATH, '//input[@placeholder="单位区号"]'))
        sleep(1)
        self.fixed_phone(line, (By.XPATH, '//input[@placeholder="单位电话"]'))
        sleep(1)
        self.department_addr(departaddr, (By.XPATH, '//input[@placeholder="请输入详细单位地址(22个字内)"]'))
        self.department_name(departname, (By.XPATH, '//input[@placeholder="请输入您任职的部门"]'))
        sleep(1)
        self.login_button((By.XPATH, '//*[@id="workvocation"]'))#行业类别旁边的按钮
        sleep(2)
        self.login_button((By.XPATH, '//*[@id="career"]/div/div[2]/div[2]/ul/li[2]/p'))#行业类别第一个默认行业
        sleep(1)
        self.login_button((By.XPATH, '//*[@id="postSelect"]'))#个人职务
        sleep(1)
        self.login_button((By.XPATH, '/html/body/div[7]/div/div[1]/div/a'))#个人职务的完成
        sleep(1)
        self.login_button((By.XPATH, '//*[@id="workingYearsSelect"]'))  # 工作年限
        sleep(1)
        self.login_button((By.XPATH, '/html/body/div[7]/div/div[1]/div/a'))  # 工作年限的完成
        sleep(1)
        self.annual_salary(salary, (By.XPATH, '//input[@placeholder="请输入您的年收入"]'))
        sleep(1)
        self.marry_status((By.XPATH, '//*[@id="marriage_A"]/span'))
        sleep(1)
        self.educational_status((By.XPATH, '//*[@id="education_A"]/span'))
        sleep(1)
        self.home_addr(homeaddr, (By.XPATH, '//input[@placeholder="请输入详细住宅地址(22个字内)"]'))


        sleep(1)
        self.login_button((By.XPATH, '//*[@id="next"]'))
        sleep(1)