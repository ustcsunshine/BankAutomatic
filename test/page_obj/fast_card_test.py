
from test.page_obj import BaseInfo
from test.page_obj.detail_info import DetailInfo
from test.page_obj.other_info import OtherInfo
from test.models import myunit


class FastCardTest(myunit.MyTest):

    def test_fast_card(self):
        url = 'https://test.xliane.com/html2/webapp/fast-issue-con/parnter.html?id=1cdced2a92f841c38792060bbf516c60'
        BaseInfo(self.driver).fast_base_info("茶浓红谷", "11010119870104203X", "15765484601", url)
        DetailInfo(self.driver).detail_info("上海蓝天科技有限公司", "021",  "6951691","浦东新区来安路500号","业务部","120", "广兰路200号")
        OtherInfo(self.driver).other_info("皮卡丘", "17777777777",  "2736805216@qq.com")


