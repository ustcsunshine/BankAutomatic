from model import unit_init
from login.login import Login

from time import sleep
import sys

from utils.url import CardUrl

sys.path.append("./model")
sys.path.append("./card_application")


class RecommendationResultQueryTest(unit_init.Base):

    # 测试用户登陆
    def login_verify(self, phone, url):
        Login(self.driver).login_recommendation(phone, url)

    # 推荐结果正常登陆
    def test_login_normal(self):
        self.login_verify("12000000101", CardUrl.RECOMMENDATION_RESULT_QUERY_LOGIN_URL)

    # 手机号码少一位
    def test_phone_miss(self):
        self.login_verify("1200000010", CardUrl.RECOMMENDATION_RESULT_QUERY_LOGIN_URL)
        po = Login(self.driver)
        sleep(1)
        self.assertIn("手机号格式不正确", po.identity_error_hint())

    # 手机号码有英文
    def test_phone_english(self):
        self.login_verify("120000001m", CardUrl.RECOMMENDATION_RESULT_QUERY_LOGIN_URL)
        po = Login(self.driver)
        sleep(1)
        self.assertIn("手机号格式不正确", po.identity_error_hint())

    # 手机号码null
    def test_phone_ull(self):
        self.login_verify("", CardUrl.RECOMMENDATION_RESULT_QUERY_LOGIN_URL)
        po = Login(self.driver)
        sleep(1)
        self.assertIn("手机号码不能为空", po.identity_error_hint())

    # 手机号码有空格
    def test_phone_miss(self):
        self.login_verify("12345 67676", CardUrl.RECOMMENDATION_RESULT_QUERY_LOGIN_URL)
        po = Login(self.driver)
        sleep(1)
        self.assertIn("手机号格式不正确", po.identity_error_hint())
