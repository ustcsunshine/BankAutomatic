from bank.test.models import myunit
from bank.login.login import Login

from time import sleep
import sys


sys.path.append("./models")
sys.path.append("./page_obj")


class GiftDistributeTest(myunit.MyTest):

    # 测试用户登陆
    def user_login_verify(self, phone, url):
        Login(self.driver).gift_distribute(phone, url)

    def test_login_normal(self):
        '''正常登陆礼品配送登陆'''
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html?bz1=0#/giftDistribute/index'
        self.user_login_verify( "13262576101", url)
        message = self.driver.find_element_by_xpath('//*[@id="app"]/div/p[1]').text
        print(message)
        sleep(2)
        self.assertIn("礼品配送信息登记", message)
        sleep(1)


    def test_login_phone_miss(self):
        '''手机号少一位'''
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html?bz1=0#/giftDistribute/index'
        self.user_login_verify( "1326257610", url)
        sleep(1)
        po = Login(self.driver)
        sleep(1)
        self.assertIn("手机号输入有误", po.identity_error_hint())
        sleep(1)




    def test_login_phone_english(self):
        '''手机号不合法'''
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html?bz1=0#/giftDistribute/index'
        self.user_login_verify( "1326257610m", url)
        sleep(1)
        po = Login(self.driver)
        sleep(1)
        self.assertIn("手机号输入有误", po.identity_error_hint())
        sleep(1)


    def test_login_phone_null(self):
        '''手机号为空'''
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html?bz1=0#/giftDistribute/index'
        self.user_login_verify( "", url)
        sleep(1)
        po = Login(self.driver)
        sleep(1)
        self.assertIn("手机号不能为空", po.identity_error_hint())
        sleep(1)
        #//*[@id="app"]/div/div[3]/div/p[2]