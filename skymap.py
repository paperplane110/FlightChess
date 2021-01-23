'''
Description: 飞行棋棋盘，负责棋盘的打印
version: 
Author: TianyuYuan
Date: 2021-01-20 22:44:19
LastEditors: TianyuYuan
LastEditTime: 2021-01-22 23:48:58
'''
from draw import Cell,trans_s2d,trans_d2s
from color import color

class SkyMap():
    '''The sky of the flight chess'''
    def __init__(self,cell_width,cell_height,cells_in_edge):
        """
        Initiation of the SkyMap
        --width：单元格宽度
        --height：单元格高度
        --cells_in_edge：正方形棋盘一边有多少个单元格
        """
        self.width = cell_width
        self.height = cell_height
        self.edge = cells_in_edge
        self.matrix = []
        self.matrix = self.zero()

    def zero(self,digit=0):
        '''生成sky的二维数字矩阵，将sky所有位置赋值=digit'''
        matrix = []
        edge = self.edge
        for i in range(self.height*edge):
            row = []
            for j in range(self.width*edge):
                row.append(digit)
            matrix.append(row)
        return matrix

    def print_sky(self):
        '''打印单元格，用于预览效果'''
        matrix = self.matrix
        for row in matrix:
            line = ""
            for bit in row:
                line += trans_d2s(bit)
            print(color(line)) 

    def show_range(self):
        self.matrix = self.zero(-1)
        self.print_sky()
        self.matrix = self.zero()

    def divide_map(self):
        print(self.edge)
    

def shape(matrix):
    m = len(matrix)
    n = len(matrix[0])
    return m,n

def add_pattern(x,y,matrix,pattern):
    m,n = shape(pattern)
    for i in range(m):
        for j in range(n):
            matrix[x+i][y+j] = pattern[i][j]
    return matrix

def scale_map(matrix,cells,button):
    for position in cells:
        m = position[0]
        n = position[1]
        x = (m)*3
        y = (n)*6
        matrix = add_pattern(x,y,matrix,button)
    return matrix

sky = SkyMap(6,3,7)
sky.show_range()
sky.print_sky()