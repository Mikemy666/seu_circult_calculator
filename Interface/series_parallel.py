# @Author  : 王博涵
'''
本模块用于计算串并联，有功功率，无功功率和视在功率
'''
import re
import cmath

def series(in_text): #串联
    in_text = text_turn(in_text)
    in_text = in_text.replace(" ","+")
    sum = eval(in_text)
    result = [sum, phase_angle(sum)]
    return result

def parallel(in_text): #并联
    in_text = text_turn(in_text)
    impe_list = in_text.split(' ')
    sum = 0
    for i in impe_list:
        i= 1/eval(i)
        sum = sum+i
    sum = 1/sum
    result = [sum, phase_angle(sum)]
    return result

def P_Var_VA(U, I): #求功率
    print(U)
    print(I)
    if '+' in I:
        I = I.replace('+', '-')
    elif '-' in I:   
        I = I.replace('-', '+')
    S = eval(U)*eval(I)
    result = [S, S.real, S.imag]
    return result


def text_turn(test_str): # 用于将式子变成能够识别于复数计算的式子
    # 定义一个正则表达式模式，用于匹配不是数字的 j
    pattern = r'(?<![0-9])j'
    # 使用正则表达式替换将 j 替换为 1j
    result_str = re.sub(pattern, '1j', test_str)
    return result_str


def phase_angle(complex_num):
    mod = cmath.sqrt(complex_num.real**2+complex_num.imag**2)
    phase_angle = cmath.phase(complex_num)
    phase_angle_degrees = phase_angle * (180 / cmath.pi)
    phase_result = [mod.real, phase_angle_degrees]
    return phase_result


