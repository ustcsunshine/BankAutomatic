from time import sleep

from selenium.webdriver.common.by import By

from web.page_operator import BasePageOperator


class LoginOperator(BasePageOperator):

    # 手机格式错误提示
    def phone_format_text(self):
        fast_phone_error_hint_loc = (By.XPATH, '//*[@id="app"]/div/ul/li[2]/div/div[3]/p')  # 卡号进度申请查询错误提示弹框定位
        return self.find_element(*fast_phone_error_hint_loc).text

    # 手机错误提示
    def phone_error_hint(self):
        fast_identity_error_hint_loc = (By.XPATH, '//*[@id="app"]/div/ul/li[1]/div/div[3]/p ')  # 卡号进度申请查询错误提示弹框定位
        return self.find_element(*fast_identity_error_hint_loc).text

    # 定义统一登陆接口
    def customer_recommendation_login(self, username, phone, url, org=''):
        self.open(url)
        self.send_keys(username, (By.XPATH, '//input[@placeholder="请输入您的姓名"]'))
        self.send_keys(phone, (By.XPATH, '//input[@placeholder="推荐人获奖短信接收号码"]'))
        if org != '':
            self.send_keys(org, (By.XPATH, '//input[@placeholder="非必填，仅供本行行员使用"]'))
        self.click((By.XPATH, '//div[@id="smscode"]'))
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/label').click()
        self.click((By.XPATH, '//div[@class="reviseBtn"]/p'))
        sleep(3)

    def recommendation_login(self, phone, url):
        self.open(url)
        self.send_keys(phone, (By.XPATH, '//input[@placeholder="请输入您的11位手机号码"]'))
        self.click((By.XPATH, '//*[@id="app"]/div/ul/li[2]/div/div[3]/div'))
        sleep(2)
        code = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]')
        print('code: ' + code.text)

        self.send_keys((By.XPATH, '//*[@id="app"]/div/ul/li[2]/div/div[2]/input'), code.text)
        self.click((By.XPATH, '//button[@class="confirm"]'))
        sleep(3)

    def mgm_recommendation_login(self, phone, username, url, org):
        self.open(url)
        self.send_keys(phone, (By.XPATH, '//input[@placeholder="请输入手机号码"]'))
        self.send_keys(username, (By.XPATH, '//input[@placeholder="请输入姓名"]'))
        self.click((By.XPATH, '//div[@id="smscode"]'))
        self.send_keys(org, (By.XPATH, '//input[@placeholder="请输入合作方代码"]'))
        sleep(3)
        self.click((By.XPATH, '//p[@class="com"]'))
        sleep(3)
        sleep(3)

    def tplus_query_login(self, phone, url, org):
        self.open(url)
        self.send_keys(phone, (By.XPATH, '//input[@placeholder="请输入您的11位手机号码"]'))
        sleep(1)
        self.click((By.XPATH, '//div[@id="smscode"]'))
        sleep(1)
        self.send_keys(org, (By.XPATH, '//input[@placeholder="请输入合作方代码"]'))
        sleep(2)
        self.click((By.XPATH, '//p[@class="com"]'))
        sleep(2)

    def mgm_gift_delivery_login(self, phone, url):
        self.open(url)
        self.send_keys(phone, (By.XPATH, '//input[@placeholder="请输入您的11位手机号码"]'))
        sleep(1)
        self.click((By.XPATH, '//div[@id="smscode"]'))
        sleep(1)
        self.click((By.XPATH, '//p[@class="com"]'))
        sleep(2)

    def card_process_query_login(self, identity, url):
        self.open(url)
        self.send_keys(identity, (By.XPATH, '//input[@placeholder="请输入您的身份证号码"]'))
        sleep(1)
        self.click((By.XPATH, '//p[@class="com"]'))

    def card_number_query_login(self, identity, phone, url):
        self.open(url)
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

    def interact_qr_code_tplus_query_login(self, phone, code, url):
        self.open(url)
        self.send_keys(code, (By.XPATH, '//*[@id="app"]/div/ul/li[1]/div/div[2]/input'))

        self.send_keys(phone, (By.XPATH, '//*[@id="app"]/div/ul/li[2]/div/div[2]/input'))
        sleep(2)
        self.click((By.XPATH, '//*[@id="smscode"]'))
        sleep(3)
        mission = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/p[2]').text
        if mission == '无权查询':
            pass
            sleep(1)
        else:
            self.click((By.XPATH, '//*[@id="app"]/div/div[1]'))
        sleep(2)

    def apply_card(self, username, identity, phone, url):
        self.open(url)
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
