from card_version_3.card_application.basic_info.basic_info import CardApplicationBasicInfo
from card_version_3.card_application.detail_info.detail_info import CardApplicationDetailInfo
from card_version_3.card_application.other_info.other_info import CardApplicationOtherInfo
from model import unit_init
from utils.identity_util import CreateIDCardTest
from utils.phone_util import Phone
from time import sleep


class FastCardTest(unit_init.Base):

    def test_fast_card(self):
        url = 'https://test.xliane.com/html2/webapp/fast-issue-con/parnter.html?id=1cdced2a92f841c38792060bbf516c60'
        CardApplicationBasicInfo(self.driver).open_login("元哥", CreateIDCardTest.CreateIDCard(), Phone.create_phone(), url)
        CardApplicationDetailInfo(self.driver).login("上海蓝天科技有限公司", "021", "6951691", "浦东新区来安路500号", "业务部", "120",
                                                           "广兰路200号")
        CardApplicationOtherInfo(self.driver).login("皮卡丘", Phone.create_phone(), "2736805216@qq.com")
        sleep(5)
