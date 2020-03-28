from time import sleep

from selenium.webdriver.common.by import By

from model import unit_init
from utils.url import CardUrl
from web.login_operator import LoginOperator


class RecommendationResultQueryTest(unit_init.Base):

    def login(self, url):
        LoginOperator(self.driver).recommendation_login('14000000000', url)

    # 推荐结果的'我要推荐按钮跳转'
    def test_recommend_friend(self):
        self.login(CardUrl.RECOMMENDATION_RESULT_QUERY_URL)
        LoginOperator(self.driver).click((By.XPATH, '//*[@id="app"]/div/div[1]/a'))
        sleep(2)
        message = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/p').text
        self.assertIn(u'立即推荐', message)
        sleep(120)

    # 推荐结果的'我要分享按钮跳转'
    def test_recommend_share(self):
        self.login(CardUrl.RECOMMENDATION_RESULT_QUERY_URL)
        LoginOperator(self.driver).click((By.XPATH, '//*[@id="app"]/div/div[1]/div[3]'))
        sleep(2)
        message = self.driver.find_element_by_xpath('//*[@id="app"]/div/img').get_attribute('textContent')
        print(message)
