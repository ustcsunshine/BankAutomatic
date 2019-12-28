from time import sleep

from selenium.webdriver.common.by import By

from login.login import Login
from model import unit_init
from utils.url import CardUrl


class RecommendationResultQueryTest(unit_init.Base):

    def login_verify(self, url):
        Login(self.driver).login_recommendation('12000000000', url)
        sleep(1)

    # 推荐结果的'我要推荐按钮跳转'
    def test_recommend_friend(self):
        self.login_verify(CardUrl.RECOMMENDATION_RESULT_QUERY_URL)
        Login(self.driver).recommend_button((By.XPATH, '//*[@id="app"]/div/div[1]/a'))
        sleep(2)
        message = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/p').text
        self.assertIn(u'立即推荐', message)

    # 推荐结果的'我要分享按钮跳转'
    def test_recommend_share(self):
        self.login_verify(CardUrl.RECOMMENDATION_RESULT_QUERY_URL)
        Login(self.driver).recommend_button((By.XPATH, '//*[@id="app"]/div/div[1]/div[3]'))
        sleep(2)
        message = self.driver.find_element_by_xpath('//*[@id="app"]/div/img').get_attribute('textContent')
        print(message)
        # self.assertIn(u'立即推荐', message)
