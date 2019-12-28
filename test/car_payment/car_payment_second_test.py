from test.car_payment import CarPaymentPersonalInfo
from test.models import myunit


class CarPaymentPersonalTest(myunit.MyTest):

    def car_payment_personal_page(self, company, salary, url):
        # url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/mgm/index'
        CarPaymentPersonalInfo(self.driver).car_payment_personal_info(company, salary, url)

    def test_car_payment_info(self):
        url = 'https://test.xliane.com/html2/car-instalment3/second.html'
        self.car_payment_personal_page("上海科技馆", 110, url)

     #单位名称为空
    def test_car_payment_company_null(self):
        url = 'https://test.xliane.com/html2/car-instalment3/second.html'
        self.car_payment_personal_page("", 110, url)
        car_payment_label = self.driver.find_element_by_xpath('/html/body/div[3]')
        self.assertEqual(car_payment_label.text, '请输入单位名称')

     #月收入为空
    def test_car_payment_salary_null(self):
        url = 'https://test.xliane.com/html2/car-instalment3/second.html'
        self.car_payment_personal_page("上海天蓝科技有限公司", "", url)
        car_payment_label = self.driver.find_element_by_xpath('/html/body/div[3]')
        self.assertEqual(car_payment_label.text, '月均收入请输入正整数')

     #月收入为零
    def test_car_payment_salary_zero(self):
        url = 'https://test.xliane.com/html2/car-instalment3/second.html'
        self.car_payment_personal_page("上海天蓝科技有限公司", "0", url)
        car_payment_label = self.driver.find_element_by_xpath('/html/body/div[3]')
        self.assertEqual(car_payment_label.text, '月均收入请输入正整数')

     #月收入为小数
    def test_car_payment_salary_point(self):
        url = 'https://test.xliane.com/html2/car-instalment3/second.html'
        self.car_payment_personal_page("上海天蓝科技有限公司", "2.5", url)
        car_payment_label = self.driver.find_element_by_xpath('/html/body/div[3]')
        self.assertEqual(car_payment_label.text, '月均收入请输入正整数')

