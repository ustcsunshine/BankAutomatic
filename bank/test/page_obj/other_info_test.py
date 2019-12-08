from bank.test.models import myunit
from bank.login.login import Login
from bank.test.page_obj.other_info import OtherInfo

from time import sleep

from bank.test.page_obj.base_info_test import DetailInfoTest
from bank.test.page_obj.base_info import BaseInfo

class OtherInfoTest(myunit.MyTest):




    def other_login_verify(self, username, phone, email, url):
        # url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/mgm/index'
        OtherInfo(self.driver).other_info(username, phone, email, url)

    def test_login_detail_info(self):
        url = 'https://test.xliane.com/html/webapp/fast-issue-con/process_three.html'

        self.other_login_verify("皮卡丘", "17777777777",  "2736805216@qq.com", url)
        Login(self.driver)

        sleep(3)
