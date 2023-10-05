# @Author  : 王博涵

import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
# import elecitem
from MainWindow import Ui_MainWindow
from child import Ui_Form
from Interface import elecitem, Equation, Laplace, series_parallel

def write_C_val(self, result):
    self.output_bro.setText(f"容抗值为:{result._impeC_value} \n电容值为:{result._parasvalue}F \n频率:{result._freq}Hz, 周期：{result._T}s" )

def write_L_val(self, result):
    self.output_bro.setText(f"感抗值为:{result._impeL_value} \n电感值为:{result._parasvalue}H \n频率:{result._freq}, 周期：{result._T}s" )

def write_R_val(self, result):
    self.output_bro.setText(f"电阻值为:{result._parasvalue}欧\n电导值为:{1/result._parasvalue}S" )    

def write_laplace_val(self, result):
    self.output_bro.setText(f"拉普拉斯变换结果:{result}" )       

def write_inverse_laplace_val(self, result):
    self.output_bro.setText(f"反拉普拉斯变换结果:{result}" )    

def write_linear_equation_val(self, result):
    if result == None:
        self.output_bro.setText("方程组无解或有无穷多解。" )
    elif result == -1:
        self.output_bro.setText("不符合要求，请重新启动输入" )
    else:
        result_str = "方程式的解:\n "
        for i in range(len(result[0])):
            equation_str = f"{result[0][i]} = {result[1][i]}"
            result_str += equation_str + "  "
        self.output_bro.setText(result_str)

def write_complex_equation_val(self, result):
    if result == None:
        self.output_bro.setText("方程组无解或有无穷多解。" )
    elif result == -1:
        self.output_bro.setText("不符合要求，请重新启动输入" )
    else:
        result_str = "方程式的解:\n "
        for i in range(len(result[0])):
            equation_str = f"{result[0][i]} = {result[1][i]}"
            result_str += equation_str + "  "
        self.output_bro.setText(result_str)
   
def write_complex_cal_val(self, result):
    self.output_bro.setText(f"{result[0]}(复数形式)\n{result[1]}(辐角形式)")

def write_series_val(self, result):
    self.output_bro.setText(f"串联等效电阻为:{result[0]}(复数形式)\n{result[1]}(辐角形式)")

def write_parallel_val(self, result):
    self.output_bro.setText(f"并联等效电阻为:{result[0]}(复数形式)\n{result[1]}(辐角形式)")

def write_PVS_val(self, result):
    self.output_bro.setText(f"视在功率为:{result[0]}VA\n有功功率为:{result[1]}w\n无功功率为:{result[2]}var")
