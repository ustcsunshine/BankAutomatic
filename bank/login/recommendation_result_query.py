from bank.test.models import myunit
from bank.login.login import Login

from time import sleep
import sys


sys.path.append("./models")
sys.path.append("./page_obj")


class RecommendationResultQueryTest(myunit.MyTest):

    # 测试用户登陆
    def user_login_verify(self, phone, url):
        Login(self.driver).login_recommendation(phone, url)

    def test_login_orgmiss(self):
        '''推荐结果登陆'''
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/recommendResult/index'
        self.user_login_verify( "12000000101", url)
        Login(self.driver)

        sleep(3)