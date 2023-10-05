# @Author  : 王博涵

'''
此模块用于解标量方程和复数方程
此模块只适合线性方程组，非线性不行

'''
import sympy as sp
from sympy import symbols, Eq, solve


var_list = [chr(ord('a') + i) for i in range(26)] #变量列表

class LinearEquationSolver: #标量方程
    __n = 0 #方程数
    __eqns = []  #储存方程式
    def __init__(self):
        self.symbols_list = None
    
    def solve_linear_equations_with_variables(self, eqns, variables): # 求解标量方程
        self.symbols_list = symbols(variables)
        solutions = solve(eqns, self.symbols_list)
        return solutions

    def geteqns(self, str_eq): #获取方程组
        try:
            eqn_str = str_eq
            eqn = Eq(sp.sympify(eqn_str.split('=')[0].strip()), sp.sympify(eqn_str.split('=')[1].strip()))
        except:
            print("不符合要求，请重新输入方程组!")
            return False
        else:
            global var_list
            for i in var_list[self.__n:]:
                if i in eqn_str:
                    print("出现未知变量,请重新输入方程组!")
                    return False
            self.__eqns.append(eqn)
            return True


    def solve_equations(self,str_text): #封装函数,求解标量方程
        str_eq = str_text.split('\n')
        self.__n = len(str_eq)
        variables = self.var_rec()
        for i in range(self.__n):
            error = self.geteqns(str_eq[i])
            if error == False:
                return -1
        
        solutions = self.solve_linear_equations_with_variables(self.__eqns, variables)
        result_var = []
        result_val = []
        if solutions:
            # print("方程组的解为：")
            for var, val in solutions.items():
                result_var.append(var)
                result_val.append(val)
            result = [result_var,result_val]
            return result
        else:
            return None
    
    def var_rec(self): #记录使用的变量，从小写a开始
        var_str = ' '
        var = 'a'
        for _ in range(self.__n):
            var_str = var_str + var + ' '
            var = chr(ord(var)+1)
        return var_str
    


class ComplexEquationSolver:
    __n = 0 #方程数
    __eqns = []  #储存方程式
    def __init__(self):
        self.symbols_list = None

    def solve_complex_equations_with_variables(self, eqns, variables): # 求解复数方程
        self.symbols_list = symbols(variables)
        try:
            solutions = solve(eqns, self.symbols_list)
            return solutions
        except:
            return None
        
    def geteqns(self, str_eq): #获取方程组
            try:
                eqn_str = str_eq
                pos = 0
                for i in eqn_str:
                    if i == 'j' or i == 'J':
                        new_eqn_str = eqn_str[:pos] + 'I' + eqn_str[pos+1:]
                    pos += 1
                eqn = Eq(sp.sympify(new_eqn_str.split('=')[0].strip()), sp.sympify(new_eqn_str.split('=')[1].strip()))
            except:
                print("不符合要求，请重新输入方程组!")
                return False
            else:
                global var_list
                for i in var_list[self.__n:9]:
                    if i in eqn_str:
                        print("出现未知变量,请重新输入方程组!")
                        return False
                self.__eqns.append(eqn)
                return True
    
    def solve_equations(self,str_text): #封装函数,求解复数方程
        str_eq = str_text.split('\n')
        self.__n = len(str_eq)
        variables = self.var_rec()
        for i in range(self.__n):
            error = self.geteqns(str_eq[i])
            if error == False:
                return -1
        
        solutions = self.solve_complex_equations_with_variables(self.__eqns, variables)
        result_var = []
        result_val = []
        if solutions:
            # print("方程组的解为：")
            for var, val in solutions.items():
                result_var.append(var)
                result_val.append(val)
            result = [result_var,result_val]
            return result
        else:
            return None
    
    def var_rec(self): #记录使用的变量，从小写a开始，最多到i
        var_str = ' '
        var = 'a'
        for _ in range(self.__n):
            var_str = var_str + var + ' '
            var = chr(ord(var)+1)
        return var_str




if __name__ == "__main__":
    text = input()
#    solver = LinearEquationSolver()
#    result = solver.solve_equations(text)
    solver = ComplexEquationSolver()
    result = solver.solve_equations(text)
    print(result)


