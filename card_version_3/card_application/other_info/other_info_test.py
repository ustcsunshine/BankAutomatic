from card_version_3.card_application.other_info.other_info import CardApplicationOtherInfo
from model import unit_init
from utils.url import CardUrl


class CardApplicationOtherInfoTest(unit_init.Base):

    def login_verify(self, username, phone, email, url):
        CardApplicationOtherInfo(self.driver).fast_other_info(username, phone, email, url)

    # 正常提交
    def test_login_other_info(self):
        self.login_verify("皮卡丘", "17777777777", "2736805216@qq.com", CardUrl.CARD_APPLICATION_OTHER_INFO_URL)

    # 其他信息页的亲属姓名为空
    def test_login_other_name_null(self):
        self.login_verify("", "17777777777", "2736805216@qq.com", CardUrl.CARD_APPLICATION_OTHER_INFO_URL)
        other_info_label = self.driver.find_element_by_xpath('/html/body/div[8]')
        self.assertEqual(other_info_label.text, '联系人姓名不能为空')

    # 其他信息页的亲属姓名有英文
    def test_login_other_name_english(self):
        self.login_verify("李大m", "17777777777", "2736805216@qq.com", CardUrl.CARD_APPLICATION_OTHER_INFO_URL)
        other_info_label = self.driver.find_element_by_xpath('/html/body/div[8]')
        self.assertEqual(other_info_label.text, '联系人姓名请输入中文，请输入2-8个汉字')

    # 其他信息页的亲属姓名1个字
    def test_login_other_name_less(self):
        self.login_verify("李", "17777777777", "2736805216@qq.com", CardUrl.CARD_APPLICATION_OTHER_INFO_URL)
        other_info_label = self.driver.find_element_by_xpath('/html/body/div[8]')
        self.assertEqual(other_info_label.text, '联系人姓名请输入中文，请输入2-8个汉字')

    # 其他信息页的亲属姓名9个字
    def test_login_other_name_more(self):
        self.login_verify("李还说时间看见的加", "17777777777", "2736805216@qq.com", CardUrl.CARD_APPLICATION_OTHER_INFO_URL)
        other_info_label = self.driver.find_element_by_xpath('/html/body/div[8]')
        self.assertEqual(other_info_label.text, '联系人姓名请输入中文，请输入2-8个汉字')

    # 其他信息页的手机号码为英文
    def test_login_other_name_more(self):
        self.login_verify("李加一", "1777777777m", "2736805216@qq.com", CardUrl.CARD_APPLICATION_OTHER_INFO_URL)
        other_info_label = self.driver.find_element_by_xpath('/html/body/div[8]')
        self.assertEqual(other_info_label.text, '请输入正确的11位手机号码')

    # 其他信息页的手机号码为中文
    def test_login_other_name_more(self):
        self.login_verify("李加一", "1777777777你", "2736805216@qq.com", CardUrl.CARD_APPLICATION_OTHER_INFO_URL)
        other_info_label = self.driver.find_element_by_xpath('/html/body/div[8]')
        self.assertEqual(other_info_label.text, '请输入正确的11位手机号码')

    # 其他信息页的手机号码为空
    def test_login_other_name_more(self):
        self.login_verify("李加一", "", "2736805216@qq.com", CardUrl.CARD_APPLICATION_OTHER_INFO_URL)
        other_info_label = self.driver.find_element_by_xpath('/html/body/div[8]')
        self.assertEqual(other_info_label.text, '手机号码不能为空')

    # 其他信息页的手机号码少一位
    def test_login_other_name_more(self):
        self.login_verify("李加一", "1200000000", "2736805216@qq.com", CardUrl.CARD_APPLICATION_OTHER_INFO_URL)
        other_info_label = self.driver.find_element_by_xpath('/html/body/div[8]')
        self.assertEqual(other_info_label.text, '请输入正确的11位手机号码')

    # 其他信息页的邮箱少个@，格式不对
    def test_login_other_email_more(self):
        self.login_verify("李加一", "12000000000", "2736805216", CardUrl.CARD_APPLICATION_OTHER_INFO_URL)
        other_info_label = self.driver.find_element_by_xpath('/html/body/div[8]')
        self.assertEqual(other_info_label.text, '请输入正确格式的电子邮箱')

    # 其他信息页的邮箱首位输入_
    def test_login_other_name_more(self):
        self.login_verify("李加一", "12000000000", "_2736805216@qq.com", CardUrl.CARD_APPLICATION_OTHER_INFO_URL)
        other_info_label = self.driver.find_element_by_xpath('/html/body/div[8]')
        self.assertEqual(other_info_label.text, '请输入正确格式的电子邮箱')

    # 其他信息页的邮箱首位输入.
    def test_login_other_name_more(self):
        self.login_verify("李加一", "12000000000", ".2736805216@qq.com", CardUrl.CARD_APPLICATION_OTHER_INFO_URL)
        other_info_label = self.driver.find_element_by_xpath('/html/body/div[8]')
        self.assertEqual(other_info_label.text, '请输入正确格式的电子邮箱')

    # 其他信息页的邮箱输入尾部_
    def test_login_other_name_more(self):
        self.login_verify("李加一", "12000000000", "2736805216_@qq.com", CardUrl.CARD_APPLICATION_OTHER_INFO_URL)
        other_info_label = self.driver.find_element_by_xpath('/html/body/div[8]')
        self.assertEqual(other_info_label.text, '请输入正确格式的电子邮箱')

    # 其他信息页的邮箱尾部输入.
    def test_login_other_name_tail(self):
        self.login_verify("李加一", "12000000000", "2736805216.@qq.com", CardUrl.CARD_APPLICATION_OTHER_INFO_URL)
        other_info_label = self.driver.find_element_by_xpath('/html/body/div[8]')
        self.assertEqual(other_info_label.text, '请输入正确格式的电子邮箱')

    # 其他信息页的邮箱@之前超过18位
    def test_login_other_name_more(self):
        self.login_verify("李加一", "12000000000", "2736805210000000000@qq.com", CardUrl.CARD_APPLICATION_OTHER_INFO_URL)
        other_info_label = self.driver.find_element_by_xpath('/html/body/div[8]')
        self.assertEqual(other_info_label.text, '邮箱前缀不能超过18个字符')
