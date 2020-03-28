import random
import time
from datetime import date, timedelta


class CreateIDCardTest:

        @staticmethod
        def CreateIDCard():
            """
            随机生成符合规则的身份证号码
            """
            # 随机身份证前六位 townNum
            ProvinceID = ['110000', '120100', '120102', '120103']
            townNum = random.choice(ProvinceID)
            # 随机身份证年份,大于18岁  yearNum
            timeDate = time.time()
            yearDate = time.strftime("%Y", time.localtime(timeDate))
            yearNum = random.randint(1980, int(yearDate) - 18)
            # 随机身份证月 日 dateNum
            someDate = date.today() + timedelta(days=random.randint(1, 366))
            dateNum = someDate.strftime("%m%d")
            # 随机身份证后四位的前三位 lastThree
            lastThree = random.randint(100, 999)
            # 随机身份证的前17位 id17(注：都加str仅仅是为了排版。)
            id17 = str(townNum) + str(yearNum) + str(dateNum) + str(lastThree)

            count = 0
            # 权重项
            weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
            # 校验项
            CheckCode = ["1", "0", "X", "9", "8", "7", "6", "5", "4", "3", "2"]

            for i in range(0, len(id17)):
                count = count + weight[i] * int(id17[i])
            # 获取校验码
            CheckNum = count % 11
            # 得到符合规则的身份证号码
            IDCard = id17 + CheckCode[CheckNum]
            return IDCard

if __name__ == '__main__':

    identity = CreateIDCardTest.CreateIDCard()
    print("生成随机身份证号码：", identity)




