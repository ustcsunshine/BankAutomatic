from time import sleep

from selenium.webdriver.common.by import By

from login.login import Login
from model import unit_init
from utils.url import CardUrl


class MgmGiftDeliveryTest(unit_init.Base):

    def login_verify(self, url):
        Login(self.driver).gift_distribute('13000000000', url)
        sleep(1)

    # mgm选择卡种按钮
    def test_send_present(self):
        self.login_verify(CardUrl.MGM_GIFT_DELIVERY)
        print("888")
        sleep(2)
        text = self.driver.find_element_by_xpath('//*[@id="app"]/div/ul/li[1]/div/div[2]/input').text
        print(text)
        if len(text) == 0:
            Login(self.driver).login_sms((By.XPATH, '//*[@id="app"]/div/ul/li[1]/div/div[2]/input'))
            sleep(2)
        else:
            self.assertIn(u'李白1 ', text)
