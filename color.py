'''
Description: 赋予字符串以颜色
version: 
Author: TianyuYuan
Date: 2021-01-22 17:21:43
LastEditors: TianyuYuan
LastEditTime: 2021-01-22 21:50:34
'''
def color(string,color="k",bold=False):
    if color == "g":
        return g(string,bold)
    elif color == "r":
        return r(string,bold)
    elif color == "p":
        return p(string,bold)
    elif color == "b":
        return b(string,bold)
    else:
        return k(string,bold)

def g(string,bold=False):
    '''let string become green'''
    if bold == 'b':
        return "\033[1;32m{}\033[0m".format(string)
    else:
        return "\033[32m{}\033[0m".format(string)

def r(string,bold=False):
    '''let string become red'''
    if bold == 'b':
        return "\033[1;31m{}\033[0m".format(string)
    else:
        return "\033[31m{}\033[0m".format(string)

def p(string,bold=False):
    '''let string become pink'''
    if bold == 'b':
        return "\033[1;35m{}\033[0m".format(string)
    else:
        return "\033[35m{}\033[0m".format(string)

def b(string,bold=False):
    '''let string become blue'''
    if bold == 'b':
        return "\033[1;34m{}\033[0m".format(string)
    else:
        return "\033[34m{}\033[0m".format(string)

def k(string,bold=False):
    '''let string become black'''
    if bold == 'b':
        return "\033[1;0m{}\033[0m".format(string)
    else:
        return string