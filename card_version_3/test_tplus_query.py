from time import sleep

from selenium.webdriver.common.by import By
from model import unit_init
from utils.url import CardUrl
from web.login_operator import LoginOperator


class TPlusQueryTest(unit_init.Base):

    # 测试用户登陆
    def login(self, phone, url, org):
        LoginOperator(self.driver).tplus_query_login(phone, url, org)

    def test_t_login_all(self):
        self.login("16000000000", CardUrl.T_PLUS_URL, 1001)
        sleep(1)
        table = self.driver.find_element_by_xpath('//*[@id="app"]/div/table')
        trlist = self.driver.find_elements_by_tag_name('tr')
        print(len(trlist))

        for row in trlist:
            tdlist = row.find_elements_by_tag_name('td')
            for col in tdlist:
                if col.text=='项目代码':
                    self.assertIn(col.text,'项目代码')
                    print(col.text)
                elif col.text == '申请量':
                    self.assertIn(col.text,'申请量')
                    print(col.text)

                elif col.text == '自动过件量':
                    self.assertIn(col.text,'自动过件量')
                    print(col.text)
                elif col.text == '自动拒件量':
                    self.assertIn(col.text,'自动拒件量')
                    print(col.text)
                elif col.text == '转人工审核':
                    self.assertIn(col.text,'转人工审核')
                    print(col.text)
                elif col.text == '待处理':
                    self.assertIn(col.text,'待处理')
                    print(col.text)
                else:
                    print(col.text)




                # print(col.text + '\t',end=" ")
            print('\n')
