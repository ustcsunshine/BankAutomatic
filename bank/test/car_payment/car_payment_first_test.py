from time import sleep

from bank.login.login import Login
from bank.test.car_payment.car_payment_first import CarPaymentBasicInfo
from bank.test.models import myunit


class CarPaymentFirsTest(myunit.MyTest):

    def car_payment_first_page(self, username, identity, salary, loan, url):
        # url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/mgm/index'
        CarPaymentBasicInfo(self.driver).car_payment_basic_info(username, identity, salary, loan, url)

    def test_car_payment_info(self):
        url = 'https://test.xliane.com/html2/car-instalment3/index.html'
        self.car_payment_first_page("李个", "512236197807102659", "110", "10", url)
