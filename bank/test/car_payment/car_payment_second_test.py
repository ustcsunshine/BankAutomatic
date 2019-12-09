from bank.test.car_payment.car_payment_second import CarPaymentPersonalInfo
from bank.test.models import myunit


class CarPaymentPersonalTest(myunit.MyTest):

    def car_payment_personal_page(self, company, salary, url):
        # url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/mgm/index'
        CarPaymentPersonalInfo(self.driver).car_payment_personal_info(company, salary, url)

    def test_car_payment_info(self):
        url = 'https://test.xliane.com/html2/car-instalment3/second.html'
        self.car_payment_personal_page("上海科技馆", 110, url)
