# @Author  : 王博涵

'''
本模块用于计算拉普拉斯变换
'''


import sympy as sp
from sympy import inverse_laplace_transform, exp, Symbol


class LaplaceTransformCalculator:
    __expr_str = None  
    __laplace_expr = None
    __inverse_laplace_expr = None
    _is_t2s = True
    __error = True
    __test_arr = None
    __expr = None


    def __init__(self): #构造函数，将特殊符号sym化
        self.t = sp.symbols('t', real=True)
        self.s = sp.symbols('s', complex=True)
        self.omega = sp.symbols('omega', real = True)
        self.exp = sp.exp
        self.sin = sp.sin
        self.cos = sp.cos
    
    def laplace_condition(self): #用于验证式子是否满足拉普拉斯正反变换，若不满足，__error = True.此外，此函数将会不断进行完善
        is_s = False
        is_t = False
        self.__test_arr = ['s', 'S', 't', 'T', 'omega', 'exp', 'sin', 'cos', '+', '-', '*', '/']
        t = self.t
        T = self.t
        s = self.s
        S = self.s
        # 判别法0：判断用户瞎写
        try:
            self.__expr = eval(self.__expr_str)
        except:
            pass
            # print("不符合要求，请重新输入")
        #end
        else:
            # 判别法1:判断测试列表里的元素是否存在
            for i in self.__test_arr :
                if i in self.__expr_str:
                    self.__error = False    
            #end            

            # 判别法2:判断t, s不能同时出现
            if ('s' in self.__expr_str) or ('S' in self.__expr_str):
                is_s = True
                if  'sin' in self.__expr_str or 'cos' in self.__expr_str:
                    is_s = False
            elif ('t' in self.__expr_str) or ('T' in self.__expr_str):
                is_t = True

            if not(is_s and is_t) and (is_s or is_t):
                self.__error = False
            #end


            #判别法3
            if 'exp(-' in self.__test_arr :
                self.__error  = False       
            elif self.__expr_str.isdigit() == True:
                self.__error = False
            #end

            # if self.__error == True:    
                # print("不符合要求，请重新输入")


    def get_str(self, strtext): #获取用户书写的表达式
        # stop = 1
        t = self.t
        T = self.t
        # S = self.S
        s = self.s

        # while stop:
        self.__expr_str = strtext
        self.laplace_condition()
        if self.__error == False:
            # if ('s' in self.__expr_str) or ('S' in self.__expr_str):
            #     self._is_t2s = False
            #     # stop = 0
            self.__expr = eval(self.__expr_str)


    
    def laplace_transform(self): #进行拉普拉斯正反变换变换
        if self.__error == True:
            return None
        if self._is_t2s == True :#正变换
            t = self.t
            T = self.t
            self.__laplace_expr = sp.laplace_transform(self.__expr, self.t, self.s, noconds = True)
            return self.__laplace_expr

        else:#反变换
            s = self.s
            S = self.s
            self.__inverse_laplace_expr = sp.inverse_laplace_transform(self.__expr, self.s, self.t)
            return self.__inverse_laplace_expr

if __name__ == "__main__":
    calculator = LaplaceTransformCalculator()

    calculator.get_str("exp(-2*t)")
    laplace_result = calculator.laplace_transform()

    print("拉普拉斯变换结果:", laplace_result)

    # ((s + 1)*(s + 2)* (s + 3))/((s + 4)*(s + 5)*(s + 6))
    # exp(-2*t)

