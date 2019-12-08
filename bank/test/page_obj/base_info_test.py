from bank.test.models import myunit
from bank.login.login import Login
from bank.test.page_obj.base_info import BaseInfo

from time import sleep


class DetailInfoTest(myunit.MyTest):

    # 测试用户登陆
    def process_first_page(self, username, identity, phone, url):
        # url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/mgm/index'
        BaseInfo(self.driver).base_info(username, identity, phone, url)
        return self.driver

    def test_login_customermiss(self):
        url = 'https://test.xliane.com/html/webapp/fast-issue-con/process_one.html'
        self.process_first_page("测试书记", "512236197807102659", "15765484677", url)
        ## assert
        detail_info_label = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[1]/label')
        self.assertTrue(detail_info_label is not None)
        self.assertEqual(detail_info_label.text, '单位名称')
        sleep(3)

