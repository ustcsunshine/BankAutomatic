from bank.test.models import myunit
from bank.login.login import login

from time import sleep


class InteractPlusTest(myunit.MyTest):

    # 测试用户登陆
    def plus_login_verify(self, phone, url):
        # url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/mgm/index'
        login(self.driver).t_code(phone, url)

    def test_login_plusmiss(self):
        '''推荐结果登陆'''
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/interactPlus0/index'
        self.plus_login_verify('12000000000', url)
        login(self.driver)

        sleep(3)