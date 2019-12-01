from bank.test.models import myunit
from bank.login.login import login

from time import sleep


class MgmRecommendationTest(myunit.MyTest):

    # 测试用户登陆
    def mgm_login_verify(self, phone, username, url, org):
        # url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/mgm/index'
        #
        login(self.driver).mgm_recommendation(phone, username, url, org)

    def test_login_orgmiss(self):
        '''推荐结果登陆'''
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/mgm/index'
        self.mgm_login_verify("13262576102", "窦路路", url, 1002)
        login(self.driver)

        sleep(3)

        # 测试用户登陆

    # def user_login_verify(self, username, phone, url, numb):
    #     login(self.driver).user_login(username, phone, url, numb)
