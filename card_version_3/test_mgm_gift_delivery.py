from time import sleep

from selenium.webdriver.common.by import By

from web.element_operator import ElementOperator
from model import unit_init
from utils.url import CardUrl


class MgmGiftDeliveryTest(unit_init.Base):

    def login_verify(self, url):
        ElementOperator(self.driver).gift_distribute('13000000000', url)
        sleep(1)

    # mgm选择卡种按钮
    def test_send_present(self):
        self.login_verify(CardUrl.MGM_GIFT_DELIVERY)
        print("888")
        sleep(2)
        text = self.driver.find_element_by_xpath('//*[@id="app"]/div/ul/li[1]/div/div[2]/input').text
        print(text)
        if len(text) == 0:
            ElementOperator(self.driver).click((By.XPATH, '//*[@id="app"]/div/ul/li[1]/div/div[2]/input'))
            sleep(2)
        else:
            self.assertIn(u'李白1 ', text)
