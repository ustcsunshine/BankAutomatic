from bank.test.models import myunit
from bank.login.login import login

from time import sleep


class MgmRecommendationTest(myunit.MyTest):

    # 测试用户登陆
    def t_login_verify(self, phone, url, org):
        # url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/mgm/index'
        #
        login(self.driver).t_recommendation(phone, url, org)

    def test_login_orgmiss(self):
        '''推荐结果登陆'''
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/tplus0/index'
        self.t_login_verify("17621523736", url, 1001)
        login(self.driver)

        sleep(3)


