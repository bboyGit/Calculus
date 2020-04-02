
class scale_ocnvert(object):
    '任意进制数之间转换的程序'
    def __init__(self, base1, base2, number1: int):
        """
        :param base1: 起始进制
        :param base2: 目标进制
        :param number1: 起始进制的数
        """
        self.base1 = base1
        self.base2 = base2
        self.number1 = number1

    def ten2object(self, number):
        """
        Desc: 将十进制数转换为其他进制数
        :param number: 一个十进制数
        """
        if self.base2 == 10:
            result = number
        else:
            result = []
            while True:
                mod = number % self.base2                # 求余（被除数 = 除数 * 商 + 余数）
                number = number // self.base2
                result.insert(0, str(mod))
                if number == 0:
                    break
            result = int(''.join(result))
        return result

    def object2ten(self):
        """
        Desc: 将任意其他进制的数转换为10进制数
        """
        if self.base1 == 10:
            result = self.number1
        else:
            str_number1 = str(self.number1)
            n = len(str_number1)
            result = sum([int(j) * self.base1**(n-i-1) for i, j in enumerate(str_number1)])
        return result

    def convert(self):
        # (1) 将起始进制数转换为10进制数
        number = self.object2ten()
        # (2）将10进制数转换为目标进制数
        result = self.ten2object(number)
        return result

if __name__=="__main__":
    print(scale_ocnvert(8, 2, 13).convert())
