from time import sleep

from web.login_operator import LoginOperator
from model import unit_init
from utils.url import CardUrl


class CardProcessQueryLoginTest(unit_init.Base):

    # 测试用户登陆
    def login(self, identity, url):
        LoginOperator(self.driver).card_process_query_login(identity, url)

    # 申请进度查询
    def test_login_identity_miss(self):
        self.login("512236197807102659", CardUrl.CARD_PROCESS_QUERY_LOGIN_URL)
        LoginOperator(self.driver)
        sleep(2)
