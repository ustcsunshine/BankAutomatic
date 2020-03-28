from time import sleep


from model import unit_init
from utils.url import CardUrl
from web.login_operator import LoginOperator


class MgmGiftDeliveryTest(unit_init.Base):

    def login(self, url):
        LoginOperator(self.driver).mgm_gift_delivery_login('12000000000', url)
        sleep(1)

    # mgm选择卡种按钮
    def test_send_present(self):
        self.login(CardUrl.MGM_GIFT_DELIVERY)
        print("888")
        sleep(2)
        text = self.driver.find_element_by_xpath('//*[@id="app"]/div/ul/li[1]/div/div[2]/input').text
        print(text)
        if text=='李白':
            LoginOperator(self.driver).click((By.XPATH, '//*[@id="app"]/div/div[1]/p'))
            sleep(2)
        else:
            print('miss')








