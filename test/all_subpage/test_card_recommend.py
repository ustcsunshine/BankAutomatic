from login.login import Login
from test.models import myunit
from selenium.webdriver.common.by import By
from time import sleep


class CardRecommendationClauseTest(myunit.MyTest):

    def click_login_verify(self, url):
        Login(self.driver).click_login(url)
        sleep(1)

    # 客户推荐界面推荐攻略
    def test_click_custom_recommend(self):
        url = 'https://test.xliane.com/html3/webapp/fastIssue/index.html#/customerRecommend/index'
        self.click_login_verify(url)
        Login(self.driver).recommend_button((By.XPATH, '//*[@id="app"]/div/div[2]/a[1]'))
        sleep(2)
        message = self.driver.find_element_by_xpath('/html/body/div/div[1]').text
        self.assertIn(u'客户参与活动，推荐达标后即可自动领取奖品', message)

    # 客户推荐界面的推荐结果查询
    def test_click_result_recommend(self):
        url = 'https://test.xliane.com/html3/webapp/fastIssue/index.html#/customerRecommend/index'
        self.click_login_verify(url)
        Login(self.driver).recommend_button((By.XPATH, '//*[@id="app"]/div/div[2]/a[2]'))
        sleep(2)
        message = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]').text
        self.assertIn(u'推荐结果查询', message)

    # 客户推荐界面的领奖攻略
    def test_click_method_recommend(self):
        url = 'https://test.xliane.com/html3/webapp/fastIssue/index.html#/customerRecommend/index'
        self.click_login_verify(url)
        Login(self.driver).recommend_button((By.XPATH, '//*[@id="app"]/div/div[2]/a[3]'))
        sleep(2)
        message = self.driver.find_element_by_xpath('/html/body/div/div[1]').text
        self.assertIn(u'礼品太壕，等不及要推荐', message)

    # 客户推荐界面的活动条款
    def test_click_contract_recommend(self):
        url = 'https://test.xliane.com/html3/webapp/fastIssue/index.html#/customerRecommend/index'
        self.click_login_verify(url)
        Login(self.driver).recommend_button((By.XPATH, '//*[@id="app"]/div/a'))
        sleep(2)
        message = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/p').text
        self.assertIn(u'一、活动时间', message)

