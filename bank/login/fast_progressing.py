from bank.test.models import myunit
from bank.login.login import Login

from time import sleep


class FastProgressTest(myunit.MyTest):

    # 测试用户登陆
    def fast_login_verify(self, identity, url):
        # url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/mgm/index'
        #
        Login(self.driver).fast_progress(identity, url)

    def test_login_identitymiss(self):
        '''推荐结果登陆'''
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/fastProgress/index'
        self.fast_login_verify("512236197807102659",  url)
        Login(self.driver)

        sleep(3)