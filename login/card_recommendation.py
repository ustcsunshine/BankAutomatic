from login.login import Login
from test.models import function, myunit
from time import sleep


class CardRecommendationTest(myunit.MyTest):

    # 测试用户登陆
    def user_login_verify(self, username, phone, url, org=''):
        if org:
            Login(self.driver).user_login(username, phone, url, org)
        else:
            Login(self.driver).user_login(username, phone, url)

    # 机构是1002的，正常登陆,有机构号1001
    def test_login_org_normal(self):
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/customerRecommend/index'
        self.user_login_verify("李芽", "17000199918", url, 1001)
        sleep(3)
        message = self.driver.find_element_by_xpath('//p[@id="copyright"]').text
        self.assertIn(u'©本服务由兴业银行信用卡中心提供', message)
        function.insert_img(self.driver, "user_pawd_true1.png")
        sleep(1)

    # 机构是1002的，正常登陆,无机构号
    def test_login_org_null(self):
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/customerRecommend/index'
        self.user_login_verify("李芽", "17000199916", url)
        sleep(3)
        message = self.driver.find_element_by_xpath('//p[@id="copyright"]').text
        self.assertIn(u'©本服务由兴业银行信用卡中心提供 v3.6.9', message)
        function.insert_img(self.driver, "user_pawd_true2.png")
        sleep(1)

    # 用户名为空
    def test_login_null_name(self):
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/customerRecommend/index'
        self.user_login_verify("", "17621523737", url, 1001)
        po = Login(self.driver)
        sleep(3)
        self.assertIn("姓名为空或格式不正确", po.pwd_error_hint())
        function.insert_img(self.driver, "user_name_miss2.png")
        print('用户名为空，提示姓名为空或格式不正确')
        sleep(1)

    # 用户名为英文
    def test_login_english_name(self):
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/customerRecommend/index'
        self.user_login_verify("jingj", "17621523730", url, 1001)
        po = Login(self.driver)
        sleep(2)
        self.assertIn("姓名为空或格式不正确", po.pwd_error_hint())
        function.insert_img(self.driver, "user_name_miss3.png")
        print('用户名为拼音，提示姓名为空或格式不正确')
        sleep(1)

    # 用户名正确，手机号码少一位
    def test_login_numb_miss(self):
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/customerRecommend/index'
        self.user_login_verify("李孝雪", "1762152373", url, 1001)
        po = Login(self.driver)
        sleep(2)
        self.assertIn("手机号为空或格式不正确", po.pwd_error_hint())
        function.insert_img(self.driver, "user_numb_miss4.png")
        print('用户名正确，手机号码少一位')

    # 手机不正确，不是数字
    def test_login_numb_english(self):
        url = 'https://test.xliane.com/html3/webapp/fastIssue/index.html#/customerRecommend/index'
        self.user_login_verify("李孝雪", "17621523736", url, 1001)
        po = Login(self.driver)
        sleep(2)
        self.assertIn("手机号为空或格式不正确", po.pwd_error_hint())
        function.insert_img(self.driver, "user_numb_english5.png")
        print('手机不正确，不是数字')

