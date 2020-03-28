from time import sleep

from selenium.webdriver.common.by import By

from model import unit_init
from utils.url import CardUrl
from web.login_operator import LoginOperator


class RecommendationResultHistoryTest(unit_init.Base):

    def login(self, url):
        LoginOperator(self.driver).recommendation_login('13311225665', url)

    # 推荐结果的'我要推荐按钮跳转'
    def test_recommend_friend(self):
        self.login(CardUrl.RECOMMENDATION_RESULT_QUERY_URL)
        sleep(2)
        # LoginOperator(self.driver).click((By.XPATH, '//*[@id="app"]/div/div[1]/a'))
        message = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[3]/div[1]/p[2]/text()').text
        self.assertIn(u'您已推荐', message)
        sleep(120)


