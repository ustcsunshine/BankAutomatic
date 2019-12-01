from bank.test.models import myunit
from bank.login.login import login

from time import sleep


class MgmRecommendationTest(myunit.MyTest):

    # 测试用户登陆
    def mgm_login_verify(self, phone,username, url,numb):
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/mgm/index'

        login(self.driver).mgm_recommendation(phone,username,url,numb)

    def test_login_orgmiss(self):
        '''推荐结果登陆'''
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/recommendResult/index'
        self.mgm_login_verify("13262576102","窦路路", url,1002)
        login(self.driver)

        sleep(3)

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
        # function.insert_img(self.driver, "user_pawd_true3.png")

        sleep(1)