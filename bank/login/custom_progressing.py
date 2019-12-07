from bank.test.models import myunit
from bank.login.login import Login

from time import sleep


class CustomerProgressTest(myunit.MyTest):

    # 测试用户登陆
    def customer_login_verify(self, identity, phone, url):
        # url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/mgm/index'
        Login(self.driver).customer_progress(identity, phone, url)

    def test_login_customermiss(self):
        '''推荐结果登陆'''
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/customerProgress/index'
        self.customer_login_verify("512236197807102659",  "15765484676", url)
        Login(self.driver)

        sleep(3)