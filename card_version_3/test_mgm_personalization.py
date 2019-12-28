from time import sleep

from selenium.webdriver.common.by import By

from web.element_operator import ElementOperator
from model import unit_init
from utils.url import CardUrl


class MgmPersonalizationTest(unit_init.Base):

    def login_verify(self, url):
        ElementOperator(self.driver).mgm_recommendation("17621523736", "李孝雪", url, 1001)
        sleep(1)

    # mgm选择卡种按钮
    def test_mgm_custom_recommend(self):
        self.login_verify(CardUrl.MGM_PERSONALIZATION_URL)
        ElementOperator(self.driver).click((By.XPATH, '//*[@id="app"]/div/ul/li[1]/div/div[3]/div/label'))
        sleep(2)
        # message = self.driver.find_element_by_xpath('/html/body/div/div[1]').text
        # self.assertIn(u'客户参与活动，推荐达标后即可自动领取奖品', message)

    # mgm选择卡种按钮
    def test_mgm_custom_recommend1(self):
        self.login_verify(CardUrl.MGM_PERSONALIZATION_URL)
        ElementOperator(self.driver).click((By.XPATH, '//*[@id="app"]/div/ul/li[1]/div/div[4]/div/label'))
        sleep(2)
        # message = self.driver.find_element_by_xpath('/html/body/div/div[1]').text
        # self.assertIn(u'客户参与活动，推荐达标后即可自动领取奖品', message)
