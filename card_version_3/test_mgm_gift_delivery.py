from time import sleep

from selenium.webdriver.common.by import By

from model import unit_init
from utils.url import CardUrl
from web.login_operator import LoginOperator


class MgmGiftDeliveryTest(unit_init.Base):

    def login(self, url):
        LoginOperator(self.driver).mgm_gift_delivery_login('13000000000', url)
        sleep(1)

    # mgm选择卡种按钮
    def test_send_present(self):
        self.login(CardUrl.MGM_GIFT_DELIVERY)
        print("888")
        sleep(2)
        text = self.driver.find_element_by_xpath('//*[@id="app"]/div/ul/li[1]/div/div[2]/input').text
        print(text)
        if len(text) == 0:
            LoginOperator(self.driver).click((By.XPATH, '//*[@id="app"]/div/ul/li[1]/div/div[2]/input'))
            sleep(2)
        else:
            self.assertIn(u'李白1 ', text)
