# @Author  : 王博涵

import math

'''
本模块用于计算电阻，感抗，容抗等一系列功能
'''
class Impedance: # 父类，用于提供接口和存放公用量
    _freq = 0 #频率
    _parasvalue = 0 #R，C，L
    _T = 0 # 周期
    _is_freq = True # 是否是频率值
    def Impedance_Value(self):
        pass   

    def get_Impe_val(self):
        pass

    def write_Impe_val(self):
        pass

    def ratio_cal(self, U, I):
        pass

    def modechange(self): # 改变频率模式或周期模式
        _is_freq = False

    def Tf_swap(self, paras): # 频率和周期转换，并将参数分别储存在两个私有变量中
        if self._is_freq:
            self._T = 1/paras
            self._freq = paras
        else:
            self._freq = 1/paras
            self._T = paras

class Resistance(Impedance):   #电阻子类

    def get_Impe_val(self, R): #取电阻值
        self._parasvalue = R
        return self._parasvalue
    
    def write_Impe_val(self):  #打印电阻值，电导值
        print("电阻值为:%.6f"% self._parasvalue)
        print("电导值为:%.6f"% 1/self._parasvalue)
    
    def ratio_cal(self, U, I): #比值法计算
        self._parasvalue = U/I
        return self._parasvalue
     
        
    

class Capacitance(Impedance): #容抗子类
    _impeC_value = 0   # 容抗

    def Impedance_Value(self, paras, Tf): #计算容抗并取容抗值,接口处一定要提前判断模式!!
        self.Tf_swap(Tf)
        self._parasvalue = paras
        self._impeC_value = 1 / (2 * math.pi * self._freq * self._parasvalue)
        return self._impeC_value
    
    def write_Impe_val(self): #打印容抗值
        print("容抗值为:%.6f"% self._impeC_value)
        print("电容值为:%f"% self._parasvalue)
        print(f"频率:{self._freq}, 周期：{self._T}")

    def ratio_cal(self, U, I):#比值法计算，存入所有参数
        self._impeC_value = U/I
        self._freq = 1/(2 * math.pi * self._impeC_value * self._parasvalue)
        self._T = 1/self._freq

class Inductive(Impedance): #感抗子类
    _impeL_value = 0 # 感抗

    def Impedance_Value(self,paras,Tf): #计算感抗并取感抗值,接口处一定要提前判断模式!!
        self.Tf_swap(Tf)
        self._parasvalue = paras
        self._impeL_value = 2 * math.pi * self._freq * self._parasvalue
        return self._impeL_value
    
    def write_Impe_val(self): #打印感抗值
        print("感抗值为:%.6f"% self._impeL_value)
        print("电感值为:%.6f"% self._parasvalue)
        print(f"频率:{self._freq}, 周期：{self._T}")

    def ratio_cal(self, U, I):#比值法计算，存入所有参数
        self._impeL_value = U/I
        self._freq = self._impeL_value/(2 * math.pi * self._parasvalue)
        self._T = 1/self._freq


if __name__ == '__main__':
    A = Capacitance()
    A.Impedance_Value(0.0000001,1000)
    A.write_Impe_val()