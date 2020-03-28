from time import sleep
from selenium.webdriver.common.by import By
from model import unit_init
from utils.phone_util import Phone
from utils.url import CardUrl
from web.login_operator import LoginOperator


class TradeDetailTest(unit_init.Base):

    def open(self, url):
        LoginOperator(self.driver).open(url)
        sleep(1)

    def test_trade_click(self):
        self.open(CardUrl.CARD_EXCLE_URL)
        LoginOperator(self.driver).click((By.XPATH, '/html/body/div[3]/ul/li[1]/div[3]/div[1]/span'))
        sleep(2)
        message = self.driver.find_element_by_xpath('/html/body/div[5]/div[1]/span[2]').text
        self.assertIn(u'权益详情', message)

    def test_apply_click(self):
        self.open(CardUrl.CARD_EXCLE_URL)
        LoginOperator(self.driver).click((By.XPATH, '/html/body/div[3]/ul/li[1]/div[3]/div[2]/span'))
        sleep(2)
        message = self.driver.find_element_by_xpath('//*[@id="GbCard"]/h4').text
        self.assertIn(u'本人知晓并同意', message)

    def test_change_active_click(self):
        self.open(CardUrl.CARD_EXCLE_URL)
        LoginOperator(self.driver).click((By.XPATH, '/html/body/div[1]/ul/li[2]/span'))
        sleep(2)
        message = self.driver.find_element_by_xpath('/html/body/div[3]/ul/li[1]/div[1]').text
        self.assertIn(u'行卡银联标白', message)

    def test_change_green_click(self):
        self.open(CardUrl.CARD_EXCLE_URL)
        LoginOperator(self.driver).click((By.XPATH, '/html/body/div[1]/ul/li[3]/span'))
        sleep(2)
        message = self.driver.find_element_by_xpath('/html/body/div[3]/ul/li[1]/div[1]').text
        self.assertIn(u'爱奇艺银联白金联名信用卡（精英版）II', message)

    def test_change_identity_click(self):
        self.open(CardUrl.CARD_EXCLE_URL)
        LoginOperator(self.driver).click((By.XPATH, '/html/body/div[1]/ul/li[4]/span'))
        sleep(2)
        message = self.driver.find_element_by_xpath('/html/body/div[3]/ul/li[1]/div[1]').text
        self.assertIn(u'厦航银联金卡', message)

    def test_change_fashion_click(self):
        self.open(CardUrl.CARD_EXCLE_URL)
        LoginOperator(self.driver).click((By.XPATH, '/html/body/div[1]/ul/li[5]/span'))
        sleep(2)
        message = self.driver.find_element_by_xpath('/html/body/div[3]/ul/li[1]/div[1]').text
        self.assertIn(u'立享卡51公积金2', message)

    def test_change_fashion_click(self):
        self.open(CardUrl.CARD_EXCLE_URL)
        LoginOperator(self.driver).click((By.XPATH, '/html/body/div[1]/ul/li[6]/span'))
        sleep(2)
        message = self.driver.find_element_by_xpath('/html/body/div[3]/ul/li[1]/div[1]').text
        self.assertIn(u'立享卡51公积金2', message)



    def test_apply_card(self):
        self.open(CardUrl.CARD_EXCLE_URL)
        LoginOperator(self.driver).click((By.XPATH, '/html/body/div[3]/ul/li[1]/div[3]/div[2]/span'))
        sleep(2)
        LoginOperator(self.driver).click((By.XPATH, '//*[@id="GbCard"]/a'))
        sleep(2)
        LoginOperator.apply_card('李神经','512236197807102659','16000000000')







