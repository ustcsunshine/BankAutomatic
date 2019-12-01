
from bank.login.login import login
from bank.test.models import myunit, function

from time import sleep


class CardRecommendationTest(myunit.MyTest):

    # 测试用户登陆
    def user_login_verify(self, username, phone, url, numb):
        login(self.driver).user_login(username, phone, url, numb)

    def test_login_orgmiss(self):
        '''机构是1002的，正常登陆'''
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/customerRecommend/index'
        self.user_login_verify("李芽", "17000199909", url, '1002')
        login(self.driver)

        sleep(3)
        message = self.driver.find_element_by_xpath('//p[@id="copyright"]').text
        self.assertIn(u'©本服务由兴业银行信用卡中心提供 v3.6.8', message)
        function.insert_img(self.driver, "user_pawd_true3.png")

        sleep(1)

    # def test_login1(self):
    #     # 用户名、手机号正确
    #
    #     self.user_login_verify(username="李孝雪", phone="17621523735")
    #     po = login(self.driver)
    #     sleep(3)
    #     message = self.driver.find_element_by_xpath('//p[@id="copyright"]').text
    #
    #     self.assertIn(u'©本服务由兴业银行信用卡中心提供 v3.6.8', message)
    #     # self.assertEqual(po.pawd_error_hint(),"密码不能为空")
    #     print('成功登陆')
    #     function.insert_img(self.driver, "user_pawd_true1.png")
    #
    #     sleep(1)


'''
    def test_login1(self):
        用户名、手机号正确


        self.user_login_verify(username="李孝雪",phone="17621523735")
        po=login(self.driver)
        sleep(3)
        message = self.driver.find_element_by_xpath('//p[@id="copyright"]').text

        self.assertIn(u'©本服务由兴业银行信用卡中心提供 v3.6.7',message)
        # self.assertEqual(po.pawd_error_hint(),"密码不能为空")
        print('成功登陆')
        function.insert_img(self.driver,"user_pawd_true1.png")
        sleep(1)



    def test_login_usermiss(self):
        用户名不正确，手机号码正常
        self.user_login_verify(username="jingj",phone="17621523730")
        po = login(self.driver)

        sleep(3)
        self.assertIn("姓名为空或格式不正确", po.pawd_error_hint())
        function.insert_img(self.driver,"user_pawd_true2.png")
        print('用户名为拼音，提示姓名为空或格式不正确')
        sleep(1)

    def test_login_smsmiss(self):
       用户名正确，手机号码不正常
        self.user_login_verify(username="李孝雪", phone="1762152373")
        po = login(self.driver)

        sleep(3)
        self.assertIn("手机号为空或格式不正确", po.pawd_error_hint())
        function.insert_img(self.driver, "user_pawd_true3.png")
        print('手机不正确，少了一位数')
        sleep(1)


    def test_login_smsmiss(self):
       用户名正确，手机号码不正常
        self.user_login_verify(username="李孝雪", phone="176215237x")
        po = login(self.driver)

        sleep(3)
        self.assertIn("手机号为空或格式不正确", po.pawd_error_hint())
        function.insert_img(self.driver, "user_pawd_true3.png")
        print('手机不正确，不是数字')
        sleep(1)
     

    def test_login2(self):
        用户名正确，密码错误
        self.user_login_verify(username="lixiaoxue@csii.com.cn",password='12sd3456')
        po=login(self.driver)
        self.assertIn("密码不正确",po.pawd_error_hint())
        function.insert_img(self.driver,"pawd_empty.png")

'''
if __name__ == "__main__":
    unittest.main()
