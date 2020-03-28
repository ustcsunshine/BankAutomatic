import sys
from time import sleep

from model import unit_init
from utils.phone_util import Phone
from utils.url import CardUrl
from web.login_operator import LoginOperator

sys.path.append("./model")
sys.path.append("./card_application")


class SourceRecommendationResultQueryLoginTest(unit_init.Base):

    # 测试用户登陆
    def login(self, phone, url):
        LoginOperator(self.driver).recommendation_login(phone, url)

    # 溯源推荐结果查询行员正常登陆
    def test_login_miss(self):
        self.login("12000000000", CardUrl.SOURCE_RECOMMENDATION_RESULT_QUERY_LOGIN_URL)

    # 手机号码少一位
    def test_phone_miss(self):
        self.login("1200000010", CardUrl.SOURCE_RECOMMENDATION_RESULT_QUERY_LOGIN_URL)
        po = LoginOperator(self.driver)
        sleep(1)
        self.assertIn("手机号格式不正确", po.phone_error_hint())

    # 手机号码有英文
    def test_phone_english(self):
        self.login("120000001m", CardUrl.SOURCE_RECOMMENDATION_RESULT_QUERY_LOGIN_URL)
        po = LoginOperator(self.driver)
        self.assertIn("手机号格式不正确", po.phone_error_hint())

    # 手机号码null
    def test_phone_ull(self):
        self.login("", CardUrl.SOURCE_RECOMMENDATION_RESULT_QUERY_LOGIN_URL)
        po = LoginOperator(self.driver)
        sleep(1)
        self.assertIn("手机号码不能为空", po.phone_error_hint())

    # 手机号码有空格
    def test_phone_miss_space(self):
        self.login("12345 67676", CardUrl.SOURCE_RECOMMENDATION_RESULT_QUERY_LOGIN_URL)
        po = LoginOperator(self.driver)
        sleep(1)
        self.assertIn("手机号格式不正确", po.phone_error_hint())

    # 随意手机号码正常登陆
    def test_phone_random(self):
        self.login(Phone.create_phone(), CardUrl.SOURCE_RECOMMENDATION_RESULT_QUERY_LOGIN_URL)
