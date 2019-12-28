from card_version_3.car_payment.basic_info.basic_info import CarPaymentBasicInfo
from model import unit_init


class CarPaymentFirsTest(unit_init.Base):

    def car_payment_first_page(self, username, identity, salary, loan, url):
        # url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/mgm/index'
        CarPaymentBasicInfo(self.driver).car_payment_basic_info(username, identity, salary, loan, url)

    # 正常输入基本信息页
    def test_car_payment_info(self):
        url = 'https://test.xliane.com/html2/car-instalment3/index.html'
        self.car_payment_first_page("李个", "512236197807102659", "110", "10", url)

    # 基本信息页姓名为空
    def test_car_payment_name_null(self):
        url = 'https://test.xliane.com/html2/car-instalment3/index.html'
        self.car_payment_first_page("", "512236197807102659", "110", "10", url)
        car_payment_label = self.driver.find_element_by_xpath('/html/body/div[4]')
        self.assertEqual(car_payment_label.text, '姓名请输入中文，不少于2个汉字')

    # 基本信息页姓名少于2位中文时
    def test_car_payment_name_less(self):
        url = 'https://test.xliane.com/html2/car-instalment3/index.html'
        self.car_payment_first_page("", "512236197807102659", "110", "10", url)
        car_payment_label = self.driver.find_element_by_xpath('/html/body/div[4]')
        self.assertEqual(car_payment_label.text, '姓名请输入中文，不少于2个汉字')

    # 基本信息页姓名有英文时
    def test_car_payment_name_english(self):
        url = 'https://test.xliane.com/html2/car-instalment3/index.html'
        self.car_payment_first_page("张一y", "512236197807102659", "110", "10", url)
        car_payment_label = self.driver.find_element_by_xpath('/html/body/div[4]')
        self.assertEqual(car_payment_label.text, '姓名请输入中文，不少于2个汉字')

    # 基本信息页姓名有数字时
    def test_car_payment_name_english(self):
        url = 'https://test.xliane.com/html2/car-instalment3/index.html'
        self.car_payment_first_page("12", "512236197807102659", "110", "10", url)
        car_payment_label = self.driver.find_element_by_xpath('/html/body/div[4]')
        self.assertEqual(car_payment_label.text, '姓名请输入中文，不少于2个汉字')

    # 基本信息页身份证为空时
    def test_car_payment_identity_null(self):
        url = 'https://test.xliane.com/html2/car-instalment3/index.html'
        self.car_payment_first_page("姚芽", "", "110", "10", url)
        car_payment_label = self.driver.find_element_by_xpath('/html/body/div[4]')
        self.assertEqual(car_payment_label.text, '请输入正确的18位证件号')

    # 基本信息页身份证少一位
    def test_car_payment_identity_less(self):
        url = 'https://test.xliane.com/html2/car-instalment3/index.html'
        self.car_payment_first_page("姚芽", "51223619780710265", "110", "10", url)
        car_payment_label = self.driver.find_element_by_xpath('/html/body/div[4]')
        self.assertEqual(car_payment_label.text, '请输入正确的18位证件号')

    # 基本信息页身份证有一位是英文
    def test_car_payment_identity_english(self):
        url = 'https://test.xliane.com/html2/car-instalment3/index.html'
        self.car_payment_first_page("姚芽", "5122361978071026m", "110", "10", url)
        car_payment_label = self.driver.find_element_by_xpath('/html/body/div[4]')
        self.assertEqual(car_payment_label.text, '请输入正确的18位证件号')

    # 基本信息页身份证不合法
    def test_car_payment_identity_miss(self):
        url = 'https://test.xliane.com/html2/car-instalment3/index.html'
        self.car_payment_first_page("姚芽", "51223619780710260", "110", "10", url)
        car_payment_label = self.driver.find_element_by_xpath('/html/body/div[4]')
        self.assertEqual(car_payment_label.text, '请输入正确的18位证件号')

    # 基本信息页车辆价格为空时
    def test_car_payment_price_null(self):
        url = 'https://test.xliane.com/html2/car-instalment3/index.html'
        self.car_payment_first_page("姚芽", "512236197807102659", "", "10", url)
        car_payment_label = self.driver.find_element_by_xpath('/html/body/div[4]')
        self.assertEqual(car_payment_label.text, '车辆价格请输入正整数')

    # 基本信息页车辆价格为零时
    def test_car_payment_price_zero(self):
        url = 'https://test.xliane.com/html2/car-instalment3/index.html'
        self.car_payment_first_page("姚芽", "512236197807102659", "0", "10", url)
        car_payment_label = self.driver.find_element_by_xpath('/html/body/div[4]')
        self.assertEqual(car_payment_label.text, '车辆价格请输入正整数')

    # 基本信息页车辆价格为小数时
    def test_car_payment_price_point(self):
        url = 'https://test.xliane.com/html2/car-instalment3/index.html'
        self.car_payment_first_page("姚芽", "512236197807102659", "1.5", "10", url)
        car_payment_label = self.driver.find_element_by_xpath('/html/body/div[4]')
        self.assertEqual(car_payment_label.text, '车辆价格请输入正整数')

    # 基本信息页贷款金额为空时
    def test_car_payment_loan_null(self):
        url = 'https://test.xliane.com/html2/car-instalment3/index.html'
        self.car_payment_first_page("姚芽", "512236197807102659", "100", "", url)
        car_payment_label = self.driver.find_element_by_xpath('/html/body/div[4]')
        self.assertEqual(car_payment_label.text, '贷款金额请输入正整数')

    # 基本信息页贷款金额零时
    def test_car_payment_loan_zero(self):
        url = 'https://test.xliane.com/html2/car-instalment3/index.html'
        self.car_payment_first_page("姚芽", "512236197807102659", "100", "0", url)
        car_payment_label = self.driver.find_element_by_xpath('/html/body/div[4]')
        self.assertEqual(car_payment_label.text, '贷款金额请输入正整数')

    # 基本信息页贷款金额为小数时
    def test_car_payment_loan_point(self):
        url = 'https://test.xliane.com/html2/car-instalment3/index.html'
        self.car_payment_first_page("姚芽", "512236197807102659", "15", "1.1", url)
        car_payment_label = self.driver.find_element_by_xpath('/html/body/div[4]')
        self.assertEqual(car_payment_label.text, '贷款金额请输入正整数')

    # 基本信息页贷款金额大于车辆价格
    def test_car_payment_loan_more(self):
        url = 'https://test.xliane.com/html2/car-instalment3/index.html'
        self.car_payment_first_page("姚芽", "512236197807102659", "15", "16", url)
        car_payment_label = self.driver.find_element_by_xpath('/html/body/div[4]')
        self.assertEqual(car_payment_label.text, '您好，贷款金额不得大于车辆价格')

    # 基本信息页未勾选协议
    def test_car_payment_loan_click(self):
        url = 'https://test.xliane.com/html2/car-instalment3/index.html'
        self.car_payment_first_page("姚芽", "512236197807102659", "15", "11", url)
        car_payment_label = self.driver.find_element_by_xpath('/html/body/div[4]')
        self.assertEqual(car_payment_label.text, '请勾选同意协议')

