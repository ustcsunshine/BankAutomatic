from time import sleep

from selenium.webdriver.common.by import By

from web.page_operator import BasePageOperator


class ElementOperator(BasePageOperator):
    url = '/'
    login_org_loc = (By.XPATH, '//input[@placeholder="非必填，仅供本行行员使用"]')

    sms_error_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[5]/div/p[2]')  # 推荐客户错误提示弹框定位
    fast_identity_error_hint_loc = (By.XPATH, '//*[@id="app"]/div/ul/li[1]/div/div[3]/p ')  # 卡号进度申请查询错误提示弹框定位
    fast_phone_error_hint_loc = (By.XPATH, '//*[@id="app"]/div/ul/li[2]/div/div[3]/p')  # 卡号进度申请查询错误提示弹框定位
    user_login_success_loc = (By.XPATH, '//*[@id="app"]/div/img')
    mgm_login_loc = (By.XPATH, '//*[@id="app"]/div/ul/li[3]/div/div[3]/p')  # 合作方代码错误提示
    present_login_success_loc = (By.XPATH, '//*[@id="app"]/div/p[1]')
    interact_error_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/p[2]')  # 交互式二维码的无权限弹框

    def send_keys(self, key, key_loc):
        self.find_element(*key_loc).send_keys(key)

    # 点击验证码
    def click(self, click_loc):
        self.find_element(*click_loc).click()

    # 客户推荐界面的推荐攻
    def click_login(self, url):
        res = self.open(url)
        if res is None:
            print('Please input right index')
            return

    # 定义统一登陆接口
    def user_login(self, username, phone, url, org=''):
        res = self.open(url)
        if res is None:
            print('Please input right index')
            return
        self.send_keys(username, (By.XPATH, '//input[@placeholder="请输入您的姓名"]'))
        self.send_keys(phone, (By.XPATH, '//input[@placeholder="推荐人获奖短信接收号码"]'))
        if org != '':
            self.send_keys(org, (By.XPATH, '//input[@placeholder="非必填，仅供本行行员使用"]'))
        self.click((By.XPATH, '//div[@id="smscode"]'))
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/label').click()
        self.click((By.XPATH, '//div[@class="reviseBtn"]/p'))
        sleep(3)

    def login_recommendation(self, phone, url):
        res = self.open(url)
        if res is None:
            print('Please input right index')
            return
        self.send_keys(phone, (By.XPATH, '//input[@placeholder="请输入您的11位手机号码"]'))
        self.click((By.XPATH, '//*[@id="app"]/div/ul/li[2]/div/div[3]/div'))
        sleep(2)
        code = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]')
        print('code: ' + code.text)

        self.send_keys((By.XPATH, '//*[@id="app"]/div/ul/li[2]/div/div[2]/input'), code.text)
        self.click((By.XPATH, '//button[@class="confirm"]'))
        sleep(3)

    def mgm_recommendation(self, phone, username, url, org):
        res = self.open(url)
        if res is None:
            print('Please input right index')
            return
        # self.bbs_login()
        self.send_keys(phone, (By.XPATH, '//input[@placeholder="请输入手机号码"]'))
        self.send_keys(username, (By.XPATH, '//input[@placeholder="请输入姓名"]'))
        self.click((By.XPATH, '//div[@id="smscode"]'))
        self.send_keys(org, (By.XPATH, '//input[@placeholder="请输入合作方代码"]'))
        sleep(3)
        self.click((By.XPATH, '//p[@class="com"]'))
        sleep(3)
        sleep(3)

    def t_recommendation(self, phone, url, org):
        res = self.open(url)
        if res is None:
            print('Please input right index')
            return
        # self.bbs_login()
        self.send_keys(phone, (By.XPATH, '//input[@placeholder="请输入您的11位手机号码"]'))
        sleep(1)
        self.click((By.XPATH, '//div[@id="smscode"]'))
        sleep(1)
        self.send_keys(org, (By.XPATH, '//input[@placeholder="请输入合作方代码"]'))
        sleep(2)
        self.click((By.XPATH, '//p[@class="com"]'))
        sleep(2)

    def gift_distribute(self, phone, url):
        res = self.open(url)
        if res is None:
            print('Please input right url')
            return
        # self.bbs_login()
        self.send_keys(phone, (By.XPATH, '//input[@placeholder="请输入您的11位手机号码"]'))
        sleep(1)
        self.click((By.XPATH, '//div[@id="smscode"]'))
        sleep(1)
        self.click((By.XPATH, '//p[@class="com"]'))
        sleep(2)

    def fast_progress(self, identity, url):

        res = self.open(url)
        if res is None:
            print('Please input right url')
            return
        self.send_keys(identity, (By.XPATH, '//input[@placeholder="请输入您的身份证号码"]'))
        sleep(1)
        self.click((By.XPATH, '//p[@class="com"]'))

    def customer_progress(self, identity, phone, url):
        res = self.open(url)
        if res is None:
            print('Please input right url')
            return
        self.send_keys(identity, (By.XPATH, '//input[@placeholder="请输入您的身份证号码"]'))
        sleep(1)
        self.send_keys(phone, (By.XPATH, '//input[@placeholder="请输入办卡所用手机号"]'))
        sleep(1)
        self.click((By.XPATH, '//*[@id="app"]/div/ul/li[3]/div/div[3]/button'))
        sleep(2)
        code = self.driver.find_element_by_xpath('//*[@id="app"]/div/ul/div')
        print('code: ' + code.text)

        self.send_keys((By.XPATH, '//input[@placeholder="请输入获取的验证码"]'), code.text)
        sleep(2)
        self.click((By.XPATH, '//p[@class="com"]'))

    def t_code(self, phone, code, url):
        res = self.open(url)
        if res is None:
            print('Please input right url')
            return
        self.send_keys(code, (By.XPATH, '//*[@id="app"]/div/ul/li[1]/div/div[2]/input'))

        self.send_keys(phone, (By.XPATH, '//*[@id="app"]/div/ul/li[2]/div/div[2]/input'))
        sleep(2)
        self.click((By.XPATH, '//*[@id="smscode"]'))
        sleep(3)
        mission = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/p[2]').text
        if mission == '无权查询':
            # self.login_button((By.XPATH, '//*[@id="app"]/div/div[3]/div/span'))
            pass
            sleep(1)
        else:
            self.click((By.XPATH, '//*[@id="app"]/div/div[1]'))

        sleep(2)

    def apply_card(self, username, identity, phone, url):
        res = self.open(url)
        if res is None:
            print('Please input right url')
            return
        self.send_keys(username, (By.XPATH, '//input[@placeholder="请输入身份证上的姓名"]'))
        sleep(1)
        self.send_keys(identity, (By.XPATH, '//input[@placeholder="请输入您的18位身份证号码"]'))
        sleep(1)
        self.send_keys(phone, (By.XPATH, '//*[@id="tel"]'))
        sleep(1)
        self.click((By.XPATH, '//button[@id="yz"]'))
        sleep(2)
        code = self.driver.find_element_by_xpath('//*[@id="smsCodeShow"]')
        print('code: ' + code.text)

        sleep(1)
        self.send_keys((By.XPATH, '//*[@id="identifyCode"]'), code.text)
        sleep(1)
        self.click((By.XPATH, '//*[@id="next"]'))

    # 用户名错误提示
    def pawd_error_hint(self):
        return self.find_element(*self.sms_error_hint_loc).text

    # 客户推荐验证码错误提示
    def pwd_error_hint(self):
        return self.find_element(*self.sms_error_hint_loc).text

    # 登陆成功用户名
    def user_login_success(self):
        return self.find_element(*self.user_login_success_loc).text

    # 身份证错误提示
    def identity_error_hint(self):
        return self.find_element(*self.fast_identity_error_hint_loc).text

    # 手机错误提示
    def phone_error_hint(self):
        return self.find_element(*self.fast_phone_error_hint_loc).text

    #  合作方错误提示
    def org_error_hint(self):
        return self.find_element(*self.mgm_login_loc).text

    #  交互式二维码错误提示
    def interact_error_hint(self):
        return self.find_element(*self.interact_error_hint_loc).text
