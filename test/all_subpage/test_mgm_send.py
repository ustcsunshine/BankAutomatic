from login.login import Login
from test.models import myunit
from selenium.webdriver.common.by import By
from time import sleep


class MgmSendTest(myunit.MyTest):

    def send_login_verify(self, url):
        Login(self.driver).gift_distribute('13000000000', url)
        sleep(1)

    # mgm选择卡种按钮
    def test_send_prsent(self):
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html?bz1=0#/giftDistribute/index'
        self.send_login_verify(url)
        print("888")
        sleep(2)
        text = self.driver.find_element_by_xpath('//*[@id="app"]/div/ul/li[1]/div/div[2]/input').text
        print(text)
        if len(text) == 0:
            Login(self.driver).login_sms((By.XPATH, '//*[@id="app"]/div/ul/li[1]/div/div[2]/input'))
            sleep(2)
        else:
            self.assertIn(u'李白1 ', text)

