from test.models import myunit
from login.login import Login

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

    # 交互式二维码推广人代码为空时
    def test_interact_code_null(self):
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/interactPlus0/index'
        self.plus_login_verify('12345698755', "", url)
        po = Login(self.driver)
        sleep(1)
        self.assertIn("推广人代码不能为空", po.identity_error_hint())

    # 交互式二维码查询人手机号码少一位
    def test_interact_code_miss(self):
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/interactPlus0/index'
        self.plus_login_verify('1234569875', "4484040029", url)
        po = Login(self.driver)
        sleep(1)
        self.assertIn("查询人手机号输入有误", po.phone_error_hint())

    # 交互式二维码查询人手机号码有英文
    def test_interact_code_english(self):
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/interactPlus0/index'
        self.plus_login_verify('1234569875m', "4484040029", url)
        po = Login(self.driver)
        sleep(1)
        self.assertIn("查询人手机号输入有误", po.phone_error_hint())
        sleep(1)

    # 交互式二维码查询人手机号码为空
    def test_interact_code_english(self):
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/interactPlus0/index'
        self.plus_login_verify('', "4484040029", url)
        po = Login(self.driver)
        sleep(1)
        self.assertIn("查询人手机号不能为空", po.phone_error_hint())
        sleep(1)

    # 交互式二维码正常登陆,但没权限
    def test_interact_premission(self):
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/interactPlus0/index'
        self.plus_login_verify('12345698754', 4484040029, url)
        po = Login(self.driver)
        self.assertIn("无权查询", po.interact_error_hint())
