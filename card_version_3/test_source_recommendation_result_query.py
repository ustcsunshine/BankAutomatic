from time import sleep

from selenium.webdriver.common.by import By

from model import unit_init
from utils.url import CardUrl
from web.login_operator import LoginOperator


class SourceRecommendationResultQueryTest(unit_init.Base):

    def login(self, url):
        LoginOperator(self.driver).recommendation_login('13000000000', url)
        sleep(1)

    # 溯源推荐的'立即推荐按钮跳转'
    def test_root_share(self):
        self.login(CardUrl.SOURCE_RECOMMENDATION_RESULT_QUERY_URL)
        LoginOperator(self.driver).click((By.XPATH, '//*[@id="app"]/div/div[1]/a'))
        sleep(2)
        message = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/p').text
        self.assertIn('立即推荐', message)
