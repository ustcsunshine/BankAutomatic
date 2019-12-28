from time import sleep

from login.login import Login
from model import unit_init
from utils.url import CardUrl


class CardProcessQueryLoginTest(unit_init.Base):

    # 测试用户登陆
    def login_verify(self, identity, url):
        Login(self.driver).fast_progress(identity, url)

    def test_login_identity_miss(self):
        '''推荐结果登陆'''
        self.login_verify("512236197807102659", CardUrl.CARD_PROCESS_QUERY_LOGIN_URL)
        Login(self.driver)
        sleep(2)
