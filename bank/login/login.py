from selenium.webdriver.common.by import By
from bank.utils.base import Page
from time import sleep


class login(Page):
    url = '/'

    # bbs_login_user_loc=(By.XPATH,"//div[@id='mzCust']/div/img")
    # bbs_login_button_loc =(By.ID,"mzLogin")
    #
    # def bbs_login(self):
    #     self.find_element(*self.bbs_login_user_loc).click()
    #     sleep(1)
    #     self.find_element(*self.bbs_login_button_loc).click()

    # login_username_loc = (By.XPATH, '//input[@placeholder="请输入您的姓名"]')
    # login_phone_loc = (By.XPATH, '//input[@placeholder="推荐人获奖短信接收号码"]')
    # login_sms_loc = (By.XPATH, '//div[@id="smscode"]')
    login_org_loc = (By.XPATH, '//input[@placeholder="非必填，仅供本行行员使用"]')

    # login_button_loc = (By.XPATH, '//div[@class="reviseBtn"]/p')

    # 登陆用户名
    def login_username(self, username, login_username_loc):
        self.find_element(*login_username_loc).send_keys(username)

    # 登陆手机号码
    def login_phone(self, phone, login_phone_loc):
        self.find_element(*login_phone_loc).send_keys(phone)

    # 点击验证码
    def login_sms(self, login_sms_loc):
        self.find_element(*login_sms_loc).click()

    # 填写验证码
    def fill_login_sms(self, send_sms_loc, code):
        self.find_element(*send_sms_loc).send_keys(code)

    # 输入机构代码
    def login_org(self, *numb):
        self.find_element(*self.login_org_loc).send_keys(numb)

    # 登陆按钮
    def login_button(self, login_button_loc):
        self.find_element(*login_button_loc).click()

    # 定义统一登陆接口
    def user_login(self, username, phone, url, *numb):
        # self.open()
        res = self.open(url)
        if res is None:
            print('Please input right index')
            return
        # self.bbs_login()
        self.login_username(username, (By.XPATH, '//input[@placeholder="请输入您的姓名"]'))
        self.login_phone(phone, (By.XPATH, '//input[@placeholder="推荐人获奖短信接收号码"]'))
        self.login_org(*numb)
        self.login_sms((By.XPATH, '//div[@id="smscode"]'))
        sleep(3)
        self.login_button((By.XPATH, '//div[@class="reviseBtn"]/p'))
        sleep(3)

    def login_recommendation(self, phone, url):
        res = self.open(url)
        if res is None:
            print('Please input right index')
            return
        # self.bbs_login()
        self.login_phone(phone, (By.XPATH, '//input[@placeholder="请输入您的11位手机号码"]'))
        self.login_sms((By.XPATH, '//*[@id="app"]/div/ul/li[2]/div/div[3]/div'))
        sleep(2)
        code = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]')
        print('code: ' + code.text)

        self.fill_login_sms((By.XPATH, '//*[@id="app"]/div/ul/li[2]/div/div[2]/input'), code.text)
        self.login_button((By.XPATH, '//button[@class="confirm"]'))
        sleep(3)

    def mgm_recommendation(self, phone,username,org,url):
        res = self.open(url)
        if res is None:
            print('Please input right index')
            return
        # self.bbs_login()
        self.login_phone(phone, (By.XPATH, '//input[@placeholder="请输入手机号码"]'))
        self.login_username(username, (By.XPATH, '//input[@placeholder="请输入姓名"]'))
        self.login_sms((By.XPATH, '//div[@id="smscode"]'))
        self.login_org((By.XPATH, '//input[@placeholder="请输入合作方代码"]'))


        self.login_button((By.XPATH, '//p[@class="com"]'))
        sleep(3)
        sleep(3)

    def userLogin(self):
        print('-----1')
        self.open(0)
        print('------2')

    sms_error_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[5]/div/p[2]')
    # pawd_error_hint_loc=(By.XPATH,"//ng-tip/div")
    user_login_success_loc = (By.XPATH, '//*[@id="app"]/div/img')

    # 用户名错误提示
    def pawd_error_hint(self):
        return self.find_element(*self.sms_error_hint_loc).text

    # 验证码错误提示
    def pawd_error_hint(self):
        return self.find_element(*self.sms_error_hint_loc).text

    # 等了成功用户名
    def user_login_success(self):
        return self.find_element(*self.user_login_success_loc).text
