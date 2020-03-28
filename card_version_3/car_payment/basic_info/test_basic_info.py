import time

from card_version_3.car_payment.basic_info.basic_info import CarPaymentBasicInfo
from model import unit_init
from utils.url import CardUrl
from utils import file_util


class CarPaymentBasicInfoTest(unit_init.Base):
    def test_upload(self):
        file_util.upload_file(CarPaymentBasicInfo(self.driver).upload_click,
                              'https://test.xliane.com/html3/webapp/fastIssue/index.html#/recruit/entry1',
                              '//*[@id="app"]/div/div[2]/div[2]/img', "/Users/jingjing.li/Downloads/kong.jpeg")
        time.sleep(3600)

    def test_no_url(self):
        CarPaymentBasicInfo(self.driver).open('https://test.xliane.com/html3/webapp/fastIssue/index.html#/recruit/entry1')
        file_util.upload_file(CarPaymentBasicInfo(self.driver).upload_click_no_open,
                              '//*[@id="app"]/div/div[2]/div[2]/img', "/Users/jingjing.li/Downloads/kong.jpeg")
        time.sleep(3600)

    def car_payment_basic_info_page(self, username, identity, salary, loan, url):
        CarPaymentBasicInfo(self.driver).open_login(username, identity, salary, loan, url)

    # 正常输入基本信息页
    def test_car_payment_info(self):
        self.car_payment_basic_info_page("李个", "512236197807102659", "110", "10", CardUrl.CAR_PAYMENT_BASIC_INFO_URL)

    # 基本信息页姓名为空
    def test_car_payment_name_null(self):
        self.car_payment_basic_info_page("", "512236197807102659", "110", "10", CardUrl.CAR_PAYMENT_BASIC_INFO_URL)
        car_payment_label = self.driver.find_element_by_xpath('/html/body/div[4]')
        self.assertEqual(car_payment_label.text, '姓名请输入中文，不少于2个汉字')

    # 基本信息页姓名少于2位中文时
    def test_car_payment_name_less(self):
        self.car_payment_basic_info_page("", "512236197807102659", "110", "10", CardUrl.CAR_PAYMENT_BASIC_INFO_URL)
        car_payment_label = self.driver.find_element_by_xpath('/html/body/div[4]')
        self.assertEqual(car_payment_label.text, '姓名请输入中文，不少于2个汉字')

    # 基本信息页姓名有英文时
    def test_car_payment_name_english(self):
        self.car_payment_basic_info_page("张一y", "512236197807102659", "110", "10", CardUrl.CAR_PAYMENT_BASIC_INFO_URL)
        car_payment_label = self.driver.find_element_by_xpath('/html/body/div[4]')
        self.assertEqual(car_payment_label.text, '姓名请输入中文，不少于2个汉字')

    # 基本信息页姓名有数字时
    def test_car_payment_name_english1(self):
        self.car_payment_basic_info_page("12", "512236197807102659", "110", "10", CardUrl.CAR_PAYMENT_BASIC_INFO_URL)
        car_payment_label = self.driver.find_element_by_xpath('/html/body/div[4]')
        self.assertEqual(car_payment_label.text, '姓名请输入中文，不少于2个汉字')

    # 基本信息页身份证为空时
    def test_car_payment_identity_null(self):
        self.car_payment_basic_info_page("姚芽", "", "110", "10", CardUrl.CAR_PAYMENT_BASIC_INFO_URL)
        car_payment_label = self.driver.find_element_by_xpath('/html/body/div[4]')
        self.assertEqual(car_payment_label.text, '请输入正确的18位证件号')

    # 基本信息页身份证少一位
    def test_car_payment_identity_less(self):
        self.car_payment_basic_info_page("姚芽", "51223619780710265", "110", "10", CardUrl.CAR_PAYMENT_BASIC_INFO_URL)
        car_payment_label = self.driver.find_element_by_xpath('/html/body/div[4]')
        self.assertEqual(car_payment_label.text, '请输入正确的18位证件号')

    # 基本信息页身份证有一位是英文
    def test_car_payment_identity_english(self):
        self.car_payment_basic_info_page("姚芽", "5122361978071026m", "110", "10", CardUrl.CAR_PAYMENT_BASIC_INFO_URL)
        car_payment_label = self.driver.find_element_by_xpath('/html/body/div[4]')
        self.assertEqual(car_payment_label.text, '请输入正确的18位证件号')

    # 基本信息页身份证不合法
    def test_car_payment_identity_miss(self):
        self.car_payment_basic_info_page("姚芽", "51223619780710260", "110", "10", CardUrl.CAR_PAYMENT_BASIC_INFO_URL)
        car_payment_label = self.driver.find_element_by_xpath('/html/body/div[4]')
        self.assertEqual(car_payment_label.text, '请输入正确的18位证件号')

    # 基本信息页车辆价格为空时
    def test_car_payment_price_null(self):
        self.car_payment_basic_info_page("姚芽", "512236197807102659", "", "10", CardUrl.CAR_PAYMENT_BASIC_INFO_URL)
        car_payment_label = self.driver.find_element_by_xpath('/html/body/div[4]')
        self.assertEqual(car_payment_label.text, '车辆价格请输入正整数')

    # 基本信息页车辆价格为零时
    def test_car_payment_price_zero(self):
        self.car_payment_basic_info_page("姚芽", "512236197807102659", "0", "10", CardUrl.CAR_PAYMENT_BASIC_INFO_URL)
        car_payment_label = self.driver.find_element_by_xpath('/html/body/div[4]')
        self.assertEqual(car_payment_label.text, '车辆价格请输入正整数')

    # 基本信息页车辆价格为小数时
    def test_car_payment_price_point(self):
        self.car_payment_basic_info_page("姚芽", "512236197807102659", "1.5", "10", CardUrl.CAR_PAYMENT_BASIC_INFO_URL)
        car_payment_label = self.driver.find_element_by_xpath('/html/body/div[4]')
        self.assertEqual(car_payment_label.text, '车辆价格请输入正整数')

    # 基本信息页贷款金额为空时
    def test_car_payment_loan_null(self):
        self.car_payment_basic_info_page("姚芽", "512236197807102659", "100", "", CardUrl.CAR_PAYMENT_BASIC_INFO_URL)
        car_payment_label = self.driver.find_element_by_xpath('/html/body/div[4]')
        self.assertEqual(car_payment_label.text, '贷款金额请输入正整数')

    # 基本信息页贷款金额零时
    def test_car_payment_loan_zero(self):
        self.car_payment_basic_info_page("姚芽", "512236197807102659", "100", "0", CardUrl.CAR_PAYMENT_BASIC_INFO_URL)
        car_payment_label = self.driver.find_element_by_xpath('/html/body/div[4]')
        self.assertEqual(car_payment_label.text, '贷款金额请输入正整数')

    # 基本信息页贷款金额为小数时
    def test_car_payment_loan_point(self):
        self.car_payment_basic_info_page("姚芽", "512236197807102659", "15", "1.1", CardUrl.CAR_PAYMENT_BASIC_INFO_URL)
        car_payment_label = self.driver.find_element_by_xpath('/html/body/div[4]')
        self.assertEqual(car_payment_label.text, '贷款金额请输入正整数')

    # 基本信息页贷款金额大于车辆价格
    def test_car_payment_loan_more(self):
        self.car_payment_basic_info_page("姚芽", "512236197807102659", "15", "16", CardUrl.CAR_PAYMENT_BASIC_INFO_URL)
        car_payment_label = self.driver.find_element_by_xpath('/html/body/div[4]')
        self.assertEqual(car_payment_label.text, '您好，贷款金额不得大于车辆价格')

    # 基本信息页未勾选协议
    def test_car_payment_loan_click(self):
        self.car_payment_basic_info_page("姚芽", "512236197807102659", "15", "11", CardUrl.CAR_PAYMENT_BASIC_INFO_URL)
        car_payment_label = self.driver.find_element_by_xpath('/html/body/div[4]')
        self.assertEqual(car_payment_label.text, '请勾选同意协议')
