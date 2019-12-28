from time import sleep

from web.element_operator import ElementOperator
from model import unit_init
from utils.url import CardUrl


class CardProcessQueryLoginTest(unit_init.Base):

    # 测试用户登陆
    def login_verify(self, identity, url):
        ElementOperator(self.driver).fast_progress(identity, url)

    def test_login_identity_miss(self):
        '''推荐结果登陆'''
        self.login_verify("512236197807102659", CardUrl.CARD_PROCESS_QUERY_LOGIN_URL)
        ElementOperator(self.driver)
        sleep(2)
