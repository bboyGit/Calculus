
class scale_ocnvert(object):
    '任意进制数之间转换的程序'
    def __init__(self, base1, base2, number1, max_iter, acurate):
        """
        :param base1: 起始进制
        :param base2: 目标进制
        :param number1: 起始进制的数
        :param max_iter: 最大迭代次数
        :param acurate: 精度
        """
        self.base1 = base1
        self.base2 = base2
        self.number1 = number1
        self.max_iter = max_iter
        self.acurate = acurate

    def ten2object(self, number):
        """
        Desc: 将十进制数转换为其他进制数
        :param number: 一个十进制数
        """
        if self.base2 == 10:
            result = number
        else:
            number_int_part = int(number)
            number_float_part = number - number_int_part
            # 整数部分
            int_part = []
            while True:
                mod = number_int_part % self.base2                # 求余（被除数 = 除数 * 商 + 余数）
                number_int_part = number_int_part // self.base2
                int_part.insert(0, str(mod))
                if number_int_part == 0:
                    break
            int_part = ''.join(int_part)
            # 小数部分
            float_part = []
            count = 0
            while True:
                number_float_part = self.base2 * number_float_part
                _int = int(number_float_part)
                number_float_part = number_float_part - _int
                float_part.append(str(_int))
                if number_float_part < self.acurate or count > self.max_iter:
                    break
            float_part = ''.join(float_part)
            # 整合
            result = float(int_part + '.' + float_part)
        return result

    def object2ten(self):
        """
        Desc: 将任意其他进制的数转换为10进制数
        """
        if self.base1 == 10:
            result = self.number1
        else:
            str_number1 = str(self.number1)
            int_part, float_part = str_number1.split('.')
            len_int_part = len(int_part)
            result_int_part = sum([self.base1**(len_int_part - 1 - i) * int(j) for i, j in enumerate(int_part)])
            result_float_part = sum([self.base1**(-(i+1)) * int(j) for i, j in enumerate(float_part)])
            result = result_int_part + result_float_part
        return result

    def convert(self):
        # (1) 将起始进制数转换为10进制数
        number = self.object2ten()
        # (2）将10进制数转换为目标进制数
        result = self.ten2object(number)
        return result

if __name__=="__main__":
    print(scale_ocnvert(base1=10, base2=2, number1=11.01, max_iter=10, acurate=10**(-6)).convert())
