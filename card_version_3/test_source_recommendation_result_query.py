from time import sleep

from selenium.webdriver.common.by import By

from login.login import Login
from model import unit_init
from utils.url import CardUrl


class SourceRecommendationResultQueryTest(unit_init.Base):

    def login_verify(self, url):
        Login(self.driver).login_recommendation('13000000000', url)
        sleep(1)

    # 溯源推荐的'立即推荐按钮跳转'
    def test_root_share(self):
        self.login_verify(CardUrl.SOURCE_RECOMMENDATION_RESULT_QUERY_URL)
        Login(self.driver).recommend_button((By.XPATH, '//*[@id="app"]/div/div[1]/a'))
        sleep(2)
        message = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/p').text
        self.assertIn(u'立即推荐', message)
