from bank.login.login import Login
from bank.test.models import myunit, function
import unittest
from time import sleep


class CardRecommendationTest(myunit.MyTest):

    # 测试用户登陆
    def user_login_verify(self, username, phone, url, number):
        Login(self.driver).user_login(username, phone, url, number)

    def test_login_orgmiss(self):
        '''机构是1002的，正常登陆'''
        url = 'https://test.xliane.com/html3/webapp/fastIssue/index.html#/customerRecommend/index'
        self.user_login_verify("李芽", "17000199909", url, '1002')
        # login(self.driver)

        sleep(3)
        message = self.driver.find_element_by_xpath('//p[@id="copyright"]').text
        self.assertIn(u'©本服务由兴业银行信用卡中心提供 v3.6.8', message)
        function.insert_img(self.driver, "user_pawd_true1.png")

        sleep(1)

    def test_login_nullname(self):
        # 用户名、手机号正确
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/customerRecommend/index'
        self.user_login_verify("", "17621523737", url, 1001)
        po = Login(self.driver)
        sleep(3)
        self.assertIn("姓名为空或格式不正确", po.pwd_error_hint())
        function.insert_img(self.driver, "user_name_miss2.png")
        print('用户名为空，提示姓名为空或格式不正确')
        sleep(1)

    def test_login_englishname(self):
        # 用户名不正确，手机号码正常
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/customerRecommend/index'
        self.user_login_verify("jingj", "17621523730", url, 1001)
        po = Login(self.driver)

        sleep(3)
        self.assertIn("姓名为空或格式不正确", po.pwd_error_hint())
        function.insert_img(self.driver, "user_name_miss3.png")
        print('用户名为拼音，提示姓名为空或格式不正确')
        sleep(1)

    def test_login_numbmiss(self):
        # 用户名正确，手机号码少一位
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/customerRecommend/index'

        self.user_login_verify("李孝雪", "1762152373", url, 1001)
        po = Login(self.driver)

        sleep(3)
        self.assertIn("手机号为空或格式不正确", po.pwd_error_hint())
        function.insert_img(self.driver, "user_numb_miss4.png")
        print('用户名正确，手机号码少一位')
        sleep(1)

    def test_login_numbenglish(self):
        # 手机不正确，不是数字
        url = 'https://test.xliane.com/html3/webapp/fastIssue/index.html#/customerRecommend/index'

        self.user_login_verify("李孝雪", "17621523736", url, 1001)
        po = Login(self.driver)

        sleep(3)
        self.assertIn("手机号为空或格式不正确", po.pwd_error_hint())
        function.insert_img(self.driver, "user_numb_english5.png")
        print('手机不正确，不是数字')
        sleep(1)
