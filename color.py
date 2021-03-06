'''
Description: 赋予字符串以颜色
version: 
Author: TianyuYuan
Date: 2021-01-22 17:21:43
LastEditors: TianyuYuan
LastEditTime: 2021-01-24 22:58:51
'''
def color(string,color="k",bold=False):
    if color == "g":
        return g(string,bold)
    elif color == "r":
        return r(string,bold)
    elif color == "y":
        return y(string,bold)
    elif color == "b":
        return b(string,bold)
    elif color == "gbg":
        return g_bg(string,bold)
    elif color == "rbg":
        return r_bg(string,bold)
    elif color == "ybg":
        return y_bg(string,bold)
    elif color == "bbg":
        return b_bg(string,bold)
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

def y(string,bold=False):
    '''let string become pink'''
    if bold == 'b':
        return "\033[1;33m{}\033[0m".format(string)
    else:
        return "\033[33m{}\033[0m".format(string)

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
        return "\033[0m{}\033[0m".format(string)

def g_bg(string,bold=False):
    '''return green background and white bold string'''
    return "\033[1;7;32m{}\033[0m".format(string)

def r_bg(string,bold=False):
    '''return red background and white bold string'''
    return "\033[1;7;31m{}\033[0m".format(string)

def y_bg(string,bold=False):
    '''return yellow background and white bold string'''
    return "\033[1;7;33m{}\033[0m".format(string)

def b_bg(string,bold=False):
    '''return blue background and white bold string'''
    return "\033[1;7;34m{}\033[0m".format(string)