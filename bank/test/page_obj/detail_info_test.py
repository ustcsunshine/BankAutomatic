from bank.test.models import myunit
from bank.login.login import Login
from bank.test.page_obj.detail_info import DetailInfo

from time import sleep

from bank.test.page_obj.base_info_test import DetailInfoTest
from bank.test.page_obj.base_info import BaseInfo

class BaseInfoTest(myunit.MyTest):

    def process_first_page(self, username, identity, phone, url):
        # url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/mgm/index'
        BaseInfo(self.driver).base_info(username, identity, phone, url)

    # 测试用户登陆
    def info_login_verify(self, company, area, line, departaddr, departname, salary, homeaddr, url):
        # url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/mgm/index'
        DetailInfo(self.driver).detail_info(company, area, line, departaddr, departname, salary, homeaddr, url)

    def test_login_detailinfo(self):
        url = 'https://test.xliane.com/html3/webapp/fast-issue-con/process_one.html'
        self.process_first_page("测试书记", "512236197807102659", "15765484677", url)

        url = 'https://test.xliane.com/html3/webapp/fast-issue-con/process_one.html'
        self.info_login_verify("上海蓝天科技有限公司", "021",  "6951691","浦东新区来安路500号","业务部","120", "广兰路200号", url)
        Login(self.driver)

        sleep(3)
