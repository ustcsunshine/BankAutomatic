from test.models import function, myunit
from login.login import Login

from time import sleep


class CustomerProgressTest(myunit.MyTest):

    # 测试用户登陆
    def customer_login_verify(self, identity, phone, url):
        # url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/mgm/index'
        Login(self.driver).customer_progress(identity, phone, url)

    def test_login_customer(self):
        '''推荐结果登陆'''
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/customerProgress/index'
        self.customer_login_verify("512236197807102659", "15765484676", url)
        self.assertIn()
        function.insert_img(self.driver, "customer_name.png")
        sleep(3)


    def test_login_identity_miss(self):
        '''推荐结果登陆失败，身份证少于18位'''
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/customerProgress/index'
        self.customer_login_verify("51223619780710265", "15765484670", url)
        sleep(2)
        po = Login(self.driver)
        sleep(3)
        self.assertIn("身份证号码有误，请确认", po.identity_error_hint())
        function.insert_img(self.driver, "identity_miss.png")
        sleep(3)


    def test_login_identity_null(self):
        '''推荐结果登陆失败，身份证为空'''
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/customerProgress/index'
        self.customer_login_verify("", "15765480006", url)
        sleep(2)
        po = Login(self.driver)
        sleep(3)
        self.assertIn("身份证号不能为空", po.identity_error_hint())
        function.insert_img(self.driver, "identity_null.png")
        sleep(1)


    def test_login_phone_miss(self):
        '''推荐结果登陆失败，手机好少于18位'''
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/customerProgress/index'
        self.customer_login_verify("110224199201305248", "1576548467", url)
        sleep(2)
        po = Login(self.driver)
        sleep(1)
        self.assertIn("手机号格式不正确", po.phone_error_hint())
        function.insert_img(self.driver, "phone_miss.png")
        sleep(2)


    def test_login_phone_null(self):
        '''推荐结果登陆失败，手机为空'''
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/customerProgress/index'
        self.customer_login_verify("110224199201305248", "", url)
        sleep(2)
        po = Login(self.driver)
        sleep(1)
        self.assertIn("手机号码不能为空", po.phone_error_hint())
        function.insert_img(self.driver, "phone_null.png")
        sleep(1)


    def test_login_phone_english(self):
        '''推荐结果登陆失败，手机不合法'''
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/customerProgress/index'
        self.customer_login_verify("110224199201305248", "1234567890m", url)
        sleep(2)
        po = Login(self.driver)
        sleep(1)
        self.assertIn("手机号格式不正确", po.phone_error_hint())
        function.insert_img(self.driver, "customer_name.png")
        sleep(1)


    def test_login_null(self):
        '''推荐结果登陆失败，身份证和手机号同时为空'''
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/customerProgress/index'
        self.customer_login_verify("", "", url)
        sleep(2)
        po = Login(self.driver)
        sleep(1)
        self.assertIn("手机号码不能为空", po.phone_error_hint())
        sleep(2)
        self.assertIn("身份证号不能为空", po.identity_error_hint())

        function.insert_img(self.driver, "customer_name.png")
        sleep(3)