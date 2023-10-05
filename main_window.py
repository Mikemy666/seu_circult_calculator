# @Author  : 罗易康(UI设计), 王博涵(交互)

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette, QBrush, QPixmap, QPainter
from PyQt5 import QtCore
from MainWindow import Ui_MainWindow
from child import Ui_Form
from Interface import elecitem, Equation, Laplace, series_parallel
import printall
from PyQt5 import QtGui



m = 2
q = 2


# eqal_num = 0
# start = True
# 面向对象创建一个子窗口
class Child(QWidget, Ui_Form):
    _signal = QtCore.pyqtSignal(int)  # 定义信号
    _signal_2 = QtCore.pyqtSignal(int)

    def __init__(self):
        super(Child, self).__init__()  # 改写QWidget
        self.setupUi(self)  # 启动QtDesigner编辑好的界面
        self.retranslateUi(self)  # 调用改写内容函数
        self.setWindowTitle("模式选择")
        self.setWindowIcon(QtGui.QIcon("./dianxiaoxin.jpg"))
        # 以下是按钮绑定信号
        self.pushButton_2.clicked.connect(self.slot1)  # 功率
        self.pushButton_3.clicked.connect(self.slot2)  # 容抗
        self.pushButton_4.clicked.connect(self.slot3)  # 感抗
        self.pushButton_5.clicked.connect(self.slot4)  # 阻抗
        self.pushButton_6.clicked.connect(self.slot5)  # 标量运算
        self.pushButton_7.clicked.connect(self.slot6)  # 复数运算
        self.pushButton_8.clicked.connect(self.slot7)  # L
        self.pushButton_9.clicked.connect(self.slot8)  # I_L

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QPainter(self)
        pixmap = QPixmap("./picture2.jpg")
        painter.drawPixmap(self.rect(), pixmap)

    # 以下是发送信号函数
    def slot1(self):
        self._signal.emit(0)
        self._signal_2.emit(0)
        self.close()

    def slot2(self):
        self._signal.emit(1)
        self._signal_2.emit(1)
        self.close()

    def slot3(self):
        self._signal.emit(2)
        self._signal_2.emit(2)
        self.close()

    def slot4(self):
        self._signal.emit(3)
        self._signal_2.emit(3)
        self.close()

    def slot5(self):
        self._signal.emit(4)
        self._signal_2.emit(4)
        self.close()

    def slot6(self):
        self._signal.emit(5)
        self._signal_2.emit(5)
        self.close()

    def slot7(self):
        self._signal.emit(6)
        self._signal_2.emit(6)
        self.close()

    def slot8(self):
        self._signal.emit(7)
        self._signal_2.emit(7)
        self.close()


# 面向对象建立一主个窗口
class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()  # 改写QMainWindow
        self.setupUi(self)
        self.Child_form = Child()  # 定义子窗口变量
        self.setWindowTitle("电路计算器")
        self.setWindowIcon(QtGui.QIcon("./dianxiaoxin.jpg"))
        cau_btn = self.pushButton  # 计算按钮`
        mod_btn = self.pushButton_2  # 模式按钮
        con_btn = self.pushButton_3  # 连接方式按钮
        fang_btn = self.pushButton_4  # 运算方程按钮
        self.input_label = self.label  # ”在这里输入"文本
        self.output_label = self.label_2  # "输出结果"文本
        self.input_edit = self.textEdit  # “在这里输入”编辑框
        self.output_bro = self.textBrowser_3  # 输出栏
        self.con_bro = self.textBrowser_2  # 连接方式显示框
        self.mod_bro = self.textBrowser  # 模式方式显示框
        self.fang_bro = self.textBrowser_4  # 方程运算显示框



        # 给计算按钮被点击绑定槽函数
        cau_btn.clicked.connect(self.login)
        # 给模式按钮绑定槽函数
        mod_btn.clicked.connect(self.trans)
        # 给连接方式绑定槽函数
        con_btn.clicked.connect(self.lianjie)
        # 给当成运算按钮绑定槽函数
        fang_btn.clicked.connect(self.fun)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QPainter(self)
        pixmap = QPixmap("./picture.jpg")
        painter.drawPixmap(self.rect(), pixmap)

    def printout(self, num):
        if num % 8 == 0:
            self.output_bro.setText("请先输入复数形式的电压值，单位：V，后输入复数形式的电流值，单位：A，以空格分割,数字与j之间不用写'*'")
        elif num % 8 == 1:
            self.output_bro.setText("请先输入电容值，单位：F，后输入频率值，单位：Hz，以空格分割")
        elif num % 8 == 2:
            self.output_bro.setText("请先输入电感值，单位：H，后输入频率值，单位：Hz，以空格分割")
        elif num % 8 == 3:
            self.output_bro.setText("请先输入电压有效值，单位：V，后输入电流有效值，单位：A，以空格分割")
        elif num % 8 == 4:
            self.output_bro.setText("已退出")
        elif num % 8 == 5:
            self.output_bro.setText("请输入计算式,数字与j之间不用写'*'")
        elif num % 8 == 6:
            self.output_bro.setText("此模式为laplace正变换，请输入时域表达式。\n范例：exp(-2*t)+1+5*exp(-3*t)")
        elif num % 8 == 7:
            self.output_bro.setText(
                "此模式为laplace反变换，请输入复频域表达式。\n范例： ((s + 1)*(s + 2)* (s + 3))/((s + 4)*(s + 5)*(s + 6))")

    # 计算按钮对应的槽函数
    def login(self):
        if self.mod_bro.toPlainText() == "功率":
            in_text = self.input_edit.toPlainText()   
            in_text = series_parallel.text_turn(in_text)
            val_list = in_text.split(' ')
            try:
                result = series_parallel.P_Var_VA(val_list[0],val_list[1])
            except Exception as e:
                self.output_bro.setText("输入不符合要求:" + str(e) + "\n请重新输入!")
            else:
                printall.write_PVS_val(self, result)


        elif self.mod_bro.toPlainText() == "容抗":
            in_text = self.input_edit.toPlainText()
            try:
                val = in_text.split(' ')
                C = float(val[0])
                f = float(val[1])
            except:
                self.output_bro.setText("不符合要求，重新输入!")
            else:
                result = elecitem.Capacitance()
                result.Impedance_Value(C, f)
                printall.write_C_val(self, result)

        elif self.mod_bro.toPlainText() == "感抗":
            in_text = self.input_edit.toPlainText()
            try:
                val = in_text.split(' ')
                C = float(val[0])
                f = float(val[1])
            except:
                self.output_bro.setText("不符合要求，重新输入!")
            else:
                result = elecitem.Inductive()
                result.Impedance_Value(C, f)
                printall.write_L_val(self, result)

        elif self.mod_bro.toPlainText() == "阻抗":
            in_text = self.input_edit.toPlainText()
            try:
                val = in_text.split(' ')
                U = float(val[0])
                I = float(val[1])
            except:
                self.output_bro.setText("不符合要求，重新输入!")
            else:
                result = elecitem.Resistance()
                result.ratio_cal(U, I)
                printall.write_R_val(self, result)

        elif self.mod_bro.toPlainText() == "   ":
            pass

        elif self.mod_bro.toPlainText() == "复数运算":
            in_text = self.input_edit.toPlainText()
            try:
                in_text = series_parallel.text_turn(in_text)
                result = eval(in_text)
                Result = [result, series_parallel.phase_angle(result)] 
            except Exception as e:
                self.output_bro.setText("输入不符合要求:" + str(e) + "\n请重新输入!")
            else:
                printall.write_complex_cal_val(self, Result)

        elif self.mod_bro.toPlainText() == "Laplace":
            in_text = self.input_edit.toPlainText()
            calculator = Laplace.LaplaceTransformCalculator()
            calculator.get_str(in_text)
            result = calculator.laplace_transform()
            if result == None:
                self.output_bro.setText("不符合要求，重新输入!")
            else:
                printall.write_laplace_val(self, result)

        elif self.mod_bro.toPlainText() == "I_Laplace":
            in_text = self.input_edit.toPlainText()
            calculator = Laplace.LaplaceTransformCalculator()
            calculator._is_t2s = False
            calculator.get_str(in_text)
            result = calculator.laplace_transform()
            if result == None:
                self.output_bro.setText("不符合要求，重新输入!")
            else:
                printall.write_inverse_laplace_val(self, result)

        elif q % 3 == 0:
            in_text = self.input_edit.toPlainText()
            solver = Equation.LinearEquationSolver()
            result = solver.solve_equations(in_text)
            printall.write_linear_equation_val(self, result)

        elif q % 3 == 1:
            in_text = self.input_edit.toPlainText()
            solver = Equation.ComplexEquationSolver()
            result = solver.solve_equations(in_text)
            printall.write_complex_equation_val(self, result)

        elif m % 3 == 0: 
            in_text = self.input_edit.toPlainText()
            try:
                result = series_parallel.series(in_text)
            except Exception as e:
                self.output_bro.setText("输入不符合要求:" + str(e) + "\n请重新输入!")
            else:
                printall.write_series_val(self, result)
        
        elif m % 3 == 1:
            in_text = self.input_edit.toPlainText()
            try:
                result = series_parallel.parallel(in_text)
            except Exception as e:
                self.output_bro.setText("输入不符合要求:" + str(e) + "\n请重新输入!")
            else:
                printall.write_parallel_val(self, result)

            # 模式按钮对应的槽函数

    def trans(self):
        self.Child_form.show()
        # 连接信号
        self.Child_form._signal.connect(self.getData)
        self.Child_form._signal_2.connect(self.printout)

    # 返回模式编辑栏文本
    def getData(self, n):
        if n % 8 == 0:
            self.mod_bro.setText("功率")
            self.mod_bro.repaint()
        elif n % 8 == 1:
            self.mod_bro.setText("容抗")
            self.mod_bro.repaint()
        elif n % 8 == 2:
            self.mod_bro.setText("感抗")
            self.mod_bro.repaint()
        elif n % 8 == 3:
            self.mod_bro.setText("阻抗")
            self.mod_bro.repaint()
        elif n % 8 == 4:
            self.mod_bro.setText("   ")
            self.mod_bro.repaint()
        elif n % 8 == 5:
            self.mod_bro.setText("复数运算")
            self.mod_bro.repaint()
        elif n % 8 == 6:
            self.mod_bro.setText("Laplace")
            self.mod_bro.repaint()
        elif n % 8 == 7:
            self.mod_bro.setText("I_Laplace")
            self.mod_bro.repaint()
        self.output_bro.setText("")
        self.con_bro.setText("")
        self.fang_bro.setText("")

    # 链接方式按钮对应的槽函数
    def lianjie(self):
        self.mod_bro.setText("")
        self.fang_bro.setText("")
        self.output_bro.setText("")
        global m
        m = m + 1
        if m % 3 == 0:
            self.con_bro.setText("串联")

            self.output_bro.setText("请依次输入阻抗值(复数形式)，以空格分割!,注意，每一个阻抗值请写成5+2j,而不是5 + 2 * j,此外,数字与j之间不用写'*'")
        elif m % 3 == 1:
            self.con_bro.setText("并联")

            self.output_bro.setText("请依次输入阻抗值(复数形式)，以空格分割!,注意，每一个阻抗值请写成5+2j,而不是5 + 2 * j,此外,数字与j之间不用写'*'")
        else:
            self.con_bro.setText("")


    def fun(self):
        self.mod_bro.setText("")
        self.con_bro.setText("")
        self.output_bro.setText("")
        global q
        q = q + 1
        if q % 3 == 1:
            self.fang_bro.setText("复数方程")

            self.output_bro.setText("您已进入求解复数方程模式，请注意以下几点:\n1. 不能写成2a的形式，只能写成2*a的形式\n2. 变量名从a开始，a,b,c...以此类推,不要写大写!!，此外只能支持9元方程组\n3. 用户输入虚数符号为j，不是i。此外，答案输出的I就是j\n以下是示例\
                                    > 请输入方程组: \n>>> a+b = 1+j\n>>> 2*a-b = 2+3*j\n> 方程组的解为:\n> a = 1 + 4*I/3  b = -I/3\nNow it's your turn!\n> 请输入方程组:")
        elif q % 3 == 0:
            self.fang_bro.setText("标量方程")
            self.output_bro.setText("您已进入求解标量方程模式，请注意以下几点:\n1. 不能写成2a的形式，只能写成2*a的形式\n2. 变量名从a开始，a,b,c...以此类推,不要写大写!!\n以下是示例\
                                    > 请输入方程组: \n>>> 2*a+b = 0\n>>> a+2*b = 3\n> 方程组的解为:\n> a = -1  b = 2\nNow it's your turn!\n> 请输入方程组:")
        else:
            self.fang_bro.setText("")
            self.output_bro.setText("")




if __name__ == '__main__':
    app = QApplication(sys.argv)

    MainWindow = MyWindow()
    ChildWindow = Child()
    MainWindow.show()
    # 进入消息循环
    sys.exit(app.exec())
