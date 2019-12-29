from card_version_3.car_payment.personal_info.personal_info import CarPaymentPersonalInfo
from model import unit_init
from utils.url import CardUrl


class CarPaymentPersonalInfoTest(unit_init.Base):

    def car_payment_personal_info_page(self, company, salary, url):
        CarPaymentPersonalInfo(self.driver).open_login(company, salary, url)

    def test_car_payment_info(self):
        self.car_payment_personal_info_page("上海科技馆", 110, CardUrl.CAR_PAYMENT_PERSONAL_INFO_URL)

    # 单位名称为空
    def test_car_payment_company_null(self):
        self.car_payment_personal_info_page("", 110, CardUrl.CAR_PAYMENT_PERSONAL_INFO_URL)
        car_payment_label = self.driver.find_element_by_xpath('/html/body/div[3]')
        self.assertEqual(car_payment_label.text, '请输入单位名称')

    # 月收入为空
    def test_car_payment_salary_null(self):
        self.car_payment_personal_info_page("上海天蓝科技有限公司", "", CardUrl.CAR_PAYMENT_PERSONAL_INFO_URL)
        car_payment_label = self.driver.find_element_by_xpath('/html/body/div[3]')
        self.assertEqual(car_payment_label.text, '月均收入请输入正整数')

    # 月收入为零
    def test_car_payment_salary_zero(self):
        self.car_payment_personal_info_page("上海天蓝科技有限公司", "0", CardUrl.CAR_PAYMENT_PERSONAL_INFO_URL)
        car_payment_label = self.driver.find_element_by_xpath('/html/body/div[3]')
        self.assertEqual(car_payment_label.text, '月均收入请输入正整数')

    # 月收入为小数
    def test_car_payment_salary_point(self):
        self.car_payment_personal_info_page("上海天蓝科技有限公司", "2.5", CardUrl.CAR_PAYMENT_PERSONAL_INFO_URL)
        car_payment_label = self.driver.find_element_by_xpath('/html/body/div[3]')
        self.assertEqual(car_payment_label.text, '月均收入请输入正整数')
