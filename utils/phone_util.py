import random


class Phone:

    @staticmethod
    def create_phone():
        # 第一位为1，其余位为0-9
        # 第二位数字
        second = random.randint(0, 9)
        # 第三位数字
        third = {
            3: random.randint(0, 9),
            4: random.randint(0, 9),
            5: random.randint(0, 9),
            7: random.randint(0, 9),
            8: random.randint(0, 9),
        }[second]

        # 最后八位数字
        suffix = random.randint(9999999, 100000000)

        # 拼接手机号
        return "1{}{}{}".format(second, third, suffix)


if __name__ == '__main__':
    phone = Phone.create_phone()
    print(phone)
