from bank.login.login import Login
from bank.test.models import myunit, function
from selenium.webdriver.common.by import By
from time import sleep


class RootRecommendTest(myunit.MyTest):

    def root_login_verify(self, url):
        Login(self.driver).login_recommendation('13000000000', url)
        sleep(1)

    # 溯源推荐的'立即推荐按钮跳转'
    def test_root_share(self):
        url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/rootsResult/index'
        self.root_login_verify(url)
        Login(self.driver).recommend_button((By.XPATH, '//*[@id="app"]/div/div[1]/a'))
        sleep(2)
        message = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/p').text
        self.assertIn(u'立即推荐', message)

