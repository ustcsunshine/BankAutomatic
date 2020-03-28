from card_version_3.card_application.basic_info.basic_info import CardApplicationBasicInfo
from model import unit_init
import unittest

from time import sleep

from utils.phone_util import Phone
from utils.url import CardUrl


class CardApplicationBasicInfoTest(unit_init.Base):

    def basic_info_page(self, username, identity, phone, url):
        CardApplicationBasicInfo(self.driver).open_login(username, identity, phone, url)
        return self.driver

    # 测试用户正常登陆
    def test_login_customer_miss(self):
        self.basic_info_page("测试书记", "110101198701045257", Phone.create_phone(), CardUrl.CARD_APPLICATION_BASIC_INFO_URL)
        base_info_label = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[1]/label')
        self.assertTrue(base_info_label is not None)
        self.assertEqual(base_info_label.text, '单位名称')
        sleep(3)

    # 测试用户姓名为英文
    def test_login_custom_name_english(self):
        self.basic_info_page("ff", "512236197807102659", Phone.create_phone(), CardUrl.CARD_APPLICATION_BASIC_INFO_URL)
        base_info_label = self.driver.find_element_by_xpath('/html/body/div[11]')
        self.assertEqual(base_info_label.text, '姓名请输入中文，请输入2-8个汉字')

    # 测试用户姓名只有一个字
    def test_login_custom_name_one(self):
        self.basic_info_page("你", "512236197807102659", Phone.create_phone(), CardUrl.CARD_APPLICATION_BASIC_INFO_URL)
        base_info_label = self.driver.find_element_by_xpath('/html/body/div[11]')
        self.assertEqual(base_info_label.text, '姓名请输入中文，请输入2-8个汉字')

    # 测试用户姓名为数字
    def test_login_custom_name_number(self):
        self.basic_info_page("111", "512236197807102659", Phone.create_phone(), CardUrl.CARD_APPLICATION_BASIC_INFO_URL)
        base_info_label = self.driver.find_element_by_xpath('/html/body/div[11]')
        self.assertEqual(base_info_label.text, '姓名请输入中文，请输入2-8个汉字')

    # 测试用户姓名为null
    def test_login_custom_name_null(self):
        self.basic_info_page("", "512236197807102659", Phone.create_phone(), CardUrl.CARD_APPLICATION_BASIC_INFO_URL)
        base_info_label = self.driver.find_element_by_xpath('/html/body/div[11]')
        self.assertEqual(base_info_label.text, '姓名不能为空')

    # 测试用户身份证少一位
    def test_login_custom_identity_miss(self):
        self.basic_info_page("你好", "51223619780710265", Phone.create_phone(), CardUrl.CARD_APPLICATION_BASIC_INFO_URL)
        base_info_label = self.driver.find_element_by_xpath('/html/body/div[11]')
        self.assertEqual(base_info_label.text, '请输入正确的18位证件号码')

    # 测试用户身份证有一位是英文
    def test_login_custom_identity_english(self):
        self.basic_info_page("你好", "51223619780710265m", Phone.create_phone(), CardUrl.CARD_APPLICATION_BASIC_INFO_URL)
        base_info_label = self.driver.find_element_by_xpath('/html/body/div[11]')
        self.assertEqual(base_info_label.text, '请输入正确的18位证件号码')

    # 测试用户身份证没填
    def test_login_custom_identity_null(self):
        self.basic_info_page("你好", "", Phone.create_phone(), CardUrl.CARD_APPLICATION_BASIC_INFO_URL)
        base_info_label = self.driver.find_element_by_xpath('/html/body/div[11]')
        self.assertEqual(base_info_label.text, '证件号码不能为空')

    # 测试用户身份证不合法
    def test_login_custom_identity_no(self):
        self.basic_info_page("你好", "512236197807102650", Phone.create_phone(), CardUrl.CARD_APPLICATION_BASIC_INFO_URL)
        base_info_label = self.driver.find_element_by_xpath('/html/body/div[11]')
        self.assertEqual(base_info_label.text, '请输入正确的18位证件号码')

    # 测试用户手机号码少一位
    def test_login_custom_phone_miss(self):
        self.basic_info_page("你好", "110224199201305248", "1576548467", CardUrl.CARD_APPLICATION_BASIC_INFO_URL)
        base_info_label = self.driver.find_element_by_xpath('/html/body/div[11]')
        self.assertEqual(base_info_label.text, '请输入正确的11位手机号码')

    # 测试用户手机号有一位是英文
    def test_login_custom_identity_english1(self):
        self.basic_info_page("你好", "110224199201305248", "1200000000m", CardUrl.CARD_APPLICATION_BASIC_INFO_URL)
        base_info_label = self.driver.find_element_by_xpath('/html/body/div[11]')
        self.assertEqual(base_info_label.text, '请输入正确的11位手机号码')

    # 测试用户手机号为空
    def test_login_custom_phone_null(self):
        self.basic_info_page("你好", "110224199201305248", "", CardUrl.CARD_APPLICATION_BASIC_INFO_URL)
        base_info_label = self.driver.find_element_by_xpath('/html/body/div[11]')
        self.assertEqual(base_info_label.text, '手机号不能为空')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(CardApplicationBasicInfoTest('test_login_custom_phone_null'))

    runner = unittest.TextTestRunner()
    runner.run(suite)

