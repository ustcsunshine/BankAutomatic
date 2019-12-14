from bank.test.models import myunit
from bank.login.login import Login

from time import sleep


class InteractPlusTest(myunit.MyTest):

    # 测试用户登陆
    def plus_login_verify(self, phone, code, url):
        # url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/mgm/index'
        Login(self.driver).t_code(phone, code, url)

    # 交互式二维码正常登陆
    def test_interact_plus(self):
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/interactPlus0/index'
        self.plus_login_verify('12345698755', 4484040029, url)
