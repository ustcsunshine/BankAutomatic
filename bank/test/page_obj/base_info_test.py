from bank.test.models import myunit
from bank.login.login import login
from bank.test.page_obj.base_info import info

from time import sleep


class BaseInfoTest(myunit.MyTest):

    # 测试用户登陆
    def info_login_verify(self, username, identity, phone, url):
        # url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/mgm/index'
        info(self.driver).base_info(username, identity, phone, url)

    def test_login_customermiss(self):
        '''推荐结果登陆'''
        url = 'https://test.xliane.com/html2/webapp/fast-issue-con/process_one.html'
        self.info_login_verify("测试书记", "512236197807102659",  "15765484677", url)
        login(self.driver)

        sleep(3)

