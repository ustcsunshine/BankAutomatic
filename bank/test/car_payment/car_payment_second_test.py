from bank.test.models import myunit
from bank.login.login import Login
from bank.test.car_payment.car_payment_first import CarPaymentBasicInfo

from time import sleep

from bank.test.page_obj.base_info_test import DetailInfoTest
from bank.test.page_obj.base_info import BaseInfo

class CarPaymentFirsTest(myunit.MyTest):

    def car_payment_first_page(self, username, identity, salary, loan, url):
        # url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/mgm/index'
        CarPaymentBasicInfo(self.driver).car_payment_basic_info(username, identity, salary, loan, url)



    def test_car_paymentinfo(self):
        url = 'https://test.xliane.com/html2/car-instalment3/index.html'
        self.car_payment_first_page("李个", "512236197807102659", "110", "10", url)


        Login(self.driver)

        sleep(30000)
