from bank.login.login import Login
from bank.test.models import myunit, function
from selenium.webdriver.common.by import By
from time import sleep


class MgmTest(myunit.MyTest):

    def mgm_login_verify(self, url):
        Login(self.driver).mgm_recommendation("17621523736", "李孝雪", url, 1001)
        sleep(1)

    # mgm选择卡种按钮
    def test_mgm_custom_recommend(self):
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/mgm/index'
        self.mgm_login_verify(url)
        Login(self.driver).recommend_button((By.XPATH, '//*[@id="app"]/div/ul/li[1]/div/div[3]/div/label'))
        sleep(2)
        # message = self.driver.find_element_by_xpath('/html/body/div/div[1]').text
        # self.assertIn(u'客户参与活动，推荐达标后即可自动领取奖品', message)

    # mgm选择卡种按钮
    def test_mgm_custom_recommend(self):
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/mgm/index'
        self.mgm_login_verify(url)
        Login(self.driver).recommend_button((By.XPATH, '//*[@id="app"]/div/ul/li[1]/div/div[4]/div/label'))
        sleep(2)
        # message = self.driver.find_element_by_xpath('/html/body/div/div[1]').text
        # self.assertIn(u'客户参与活动，推荐达标后即可自动领取奖品', message)