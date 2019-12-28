from time import sleep

from login.login import Login
from model import unit_init
from utils import image_util
from utils.url import CardUrl


class CustomerRecommendationLoginTest(unit_init.Base):

    # 测试用户登陆
    def login_verify(self, username, phone, url, org=''):
        Login(self.driver).user_login(username, phone, url, org)

    # 机构是1002的，正常登陆,有机构号1001
    def test_login_org_normal(self):
        self.login_verify("李芽", "17000199918", CardUrl.CUSTOMER_RECO_LOGIN_URL, '1001')
        sleep(3)
        message = self.driver.find_element_by_xpath('//p[@id="copyright"]').text
        self.assertIn(u'©本服务由兴业银行信用卡中心提供', message)
        image_util.insert_img(self.driver, "user_pawd_true1.png")
        sleep(1)

    # 机构是1002的，正常登陆,无机构号
    def test_login_org_null(self):
        self.login_verify("李芽", "17000199916", CardUrl.CUSTOMER_RECO_LOGIN_URL)
        sleep(3)
        message = self.driver.find_element_by_xpath('//p[@id="copyright"]').text
        self.assertIn(u'©本服务由兴业银行信用卡中心提供 v3.6.9', message)
        image_util.insert_img(self.driver, "user_pawd_true2.png")
        sleep(1)

    # 用户名为空
    def test_login_null_name(self):
        self.login_verify("", "17621523737", CardUrl.CUSTOMER_RECO_LOGIN_URL, '1001')
        po = Login(self.driver)
        sleep(3)
        self.assertIn("姓名为空或格式不正确", po.pwd_error_hint())
        image_util.insert_img(self.driver, "user_name_miss2.png")
        print('用户名为空，提示姓名为空或格式不正确')
        sleep(1)

    # 用户名为英文
    def test_login_english_name(self):
        self.login_verify("jingj", "17621523730", CardUrl.CUSTOMER_RECO_LOGIN_URL, '1001')
        po = Login(self.driver)
        sleep(2)
        self.assertIn("姓名为空或格式不正确", po.pwd_error_hint())
        image_util.insert_img(self.driver, "user_name_miss3.png")
        print('用户名为拼音，提示姓名为空或格式不正确')
        sleep(1)

    # 用户名正确，手机号码少一位
    def test_login_numb_miss(self):
        self.login_verify("李孝雪", "1762152373", CardUrl.CUSTOMER_RECO_LOGIN_URL, '1001')
        po = Login(self.driver)
        sleep(2)
        self.assertIn("手机号为空或格式不正确", po.pwd_error_hint())
        image_util.insert_img(self.driver, "user_numb_miss4.png")
        print('用户名正确，手机号码少一位')

    # 手机不正确，不是数字
    def test_login_numb_english(self):
        self.login_verify("李孝雪", "17621523736", CardUrl.CUSTOMER_RECO_LOGIN_URL, '1001')
        po = Login(self.driver)
        sleep(2)
        self.assertIn("手机号为空或格式不正确", po.pwd_error_hint())
        image_util.insert_img(self.driver, "user_numb_english5.png")
        print('手机不正确，不是数字')
