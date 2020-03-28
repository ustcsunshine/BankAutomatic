from selenium.webdriver.common.by import By

from card_version_3.card_application.other_info.other_info import CardApplicationOtherInfo
from model import unit_init
from utils.phone_util import Phone
from utils.url import CardUrl
from web.login_operator import LoginOperator


class CardApplicationOtherInfoTest(unit_init.Base):

    def login(self, username, phone, email, url):
        CardApplicationOtherInfo(self.driver).open_login(username, phone, email, url)

    def card_error_text(self):
        card_error_hint_loc = (By.XPATH, '/html/body/div[8]')
        operator = LoginOperator(self.driver)
        return operator.get_text(card_error_hint_loc )

    # 正常提交
    def test_login_other_info(self):
        self.login("皮卡丘", Phone.create_phone(), "2736805216@qq.com", CardUrl.CARD_APPLICATION_OTHER_INFO_URL)

    # 其他信息页的亲属姓名为空
    def test_login_other_name_null(self):
        self.login("", Phone.create_phone(), "2736805216@qq.com", CardUrl.CARD_APPLICATION_OTHER_INFO_URL)
        self.assertIn('联系人姓名不能为空', self.card_error_text())

    # 其他信息页的亲属姓名有英文
    def test_login_other_name_english(self):
        self.login("李大m", Phone.create_phone(), "2736805216@qq.com", CardUrl.CARD_APPLICATION_OTHER_INFO_URL)
        self.assertIn('联系人姓名请输入中文，请输入2-8个汉字', self.card_error_text())

    # 其他信息页的亲属姓名1个字
    def test_login_other_name_less(self):
        self.login("李", Phone.create_phone(), "2736805216@qq.com", CardUrl.CARD_APPLICATION_OTHER_INFO_URL)
        self.assertIn('联系人姓名请输入中文，请输入2-8个汉字', self.card_error_text())

    # 其他信息页的亲属姓名9个字
    def test_login_other_name_more(self):
        self.login("李还说时间看见的加", Phone.create_phone(), "2736805216@qq.com", CardUrl.CARD_APPLICATION_OTHER_INFO_URL)
        self.assertIn('联系人姓名请输入中文，请输入2-8个汉字', self.card_error_text())

    # 其他信息页的手机号码为英文
    def test_other_page_phone_english(self):
        self.login("李加一", "1777777777m", "2736805216@qq.com", CardUrl.CARD_APPLICATION_OTHER_INFO_URL)
        other_info_label = self.driver.find_element_by_xpath('/html/body/div[8]')
        self.assertEqual(other_info_label.text, '请输入正确的11位手机号码')

    # 其他信息页的手机号码为中文
    def test_other_page_phone_chinese(self):
        self.login("李加一", "1777777777你", "2736805216@qq.com", CardUrl.CARD_APPLICATION_OTHER_INFO_URL)
        self.assertIn('请输入正确的11位手机号码', self.card_error_text())

    # 其他信息页的手机号码为空
    def test_other_page_phone_null(self):
        self.login("李加一", "", "2736805216@qq.com", CardUrl.CARD_APPLICATION_OTHER_INFO_URL)
        self.assertIn('手机号码不能为空', self.card_error_text())

    # 其他信息页的手机号码少一位
    def test_other_page_phone_less(self):
        self.login("李加一", Phone.create_phone(), "2736805216@qq.com", CardUrl.CARD_APPLICATION_OTHER_INFO_URL)
        self.assertIn('请输入正确的11位手机号码', self.card_error_text())

    # 其他信息页的邮箱少个@，格式不对
    def test_other_page_email_less_at(self):
        self.login("李加一", Phone.create_phone(), "2736805216", CardUrl.CARD_APPLICATION_OTHER_INFO_URL)
        self.assertIn('请输入正确格式的电子邮箱', self.card_error_text())

    # 其他信息页的邮箱首位输入_
    def test_other_page_email_first_format_(self):
        self.login("李加一", Phone.create_phone(), "_2736805216@qq.com", CardUrl.CARD_APPLICATION_OTHER_INFO_URL)
        self.assertIn('请输入正确格式的电子邮箱', self.card_error_text())

    # 其他信息页的邮箱首位输入.
    def test_other_page_email_first_format(self):
        self.login("李加一", Phone.create_phone(), ".2736805216@qq.com", CardUrl.CARD_APPLICATION_OTHER_INFO_URL)
        self.assertIn('请输入正确格式的电子邮箱', self.card_error_text())

    # 其他信息页的邮箱输入尾部_
    def test_other_page_email_tail_(self):
        self.login("李加一", Phone.create_phone(), "2736805216_@qq.com", CardUrl.CARD_APPLICATION_OTHER_INFO_URL)
        self.assertIn('请输入正确格式的电子邮箱', self.card_error_text())

    # 其他信息页的邮箱尾部输入.
    def test_other_page_email_tail(self):
        self.login("李加一", Phone.create_phone(), "2736805216.@qq.com", CardUrl.CARD_APPLICATION_OTHER_INFO_URL)
        self.assertIn('请输入正确格式的电子邮箱', self.card_error_text())

    # 其他信息页的邮箱@之前超过18位
    def test_login_other_email_name_more(self):
        self.login("李加一", Phone.create_phone(), "2736805210000000000@qq.com", CardUrl.CARD_APPLICATION_OTHER_INFO_URL)
        car_apply_label = self.driver.find_element_by_xpath('/html/body/div[9]/div[2]')
        self.assertIn('填写时间过长，请关闭页面重新开始填写', car_apply_label.text)
