from bank.test.models import myunit
from bank.login.login import Login
from bank.test.page_obj.detail_info import DetailInfo

from time import sleep

from bank.test.page_obj.base_info_test import BaseInfo
from bank.test.page_obj.base_info import BaseInfo


class DetailInfoTest(myunit.MyTest):

    # def process_first_page(self, username, identity, phone, url):
    #     # url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/mgm/index'
    #     DetailInfo(self.driver).fast_detail_info(username, identity, phone, url)

    def info_login_verify(self, company, area, line, departaddr, departname, salary, homeaddr, url):
        # url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/mgm/index'
        DetailInfo(self.driver).fast_detail_info(company, area, line, departaddr, departname, salary, homeaddr, url)

    def test_login_detailinfo(self):
        url = 'https://test.xliane.com/html3/webapp/fast-issue-con/process_two.html'
        self.info_login_verify("上海蓝天科技有限公司", "021", "6951691", "浦东新区来安路500号", "业务部", "120", "广兰路200号", url)

        sleep(3)
