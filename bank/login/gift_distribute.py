from bank.test.models import myunit
from bank.login.login import login

from time import sleep
import sys


sys.path.append("./models")
sys.path.append("./page_obj")


class GiftDistributeTest(myunit.MyTest):

    # 测试用户登陆
    def user_login_verify(self, phone, url):
        login(self.driver).gift_distribute(phone, url)

    def test_login_orgmiss(self):
        '''礼品配送登陆'''
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html?bz1=0#/giftDistribute/index'
        self.user_login_verify( "13262576101", url)
        login(self.driver)

        sleep(3)