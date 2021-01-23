'''
Description: Class Cell, used for create one type of cell, setting the w,h,color,bold,pattern of the cell.
version: 
Author: TianyuYuan
Date: 2021-01-20 23:09:05
LastEditors: TianyuYuan
LastEditTime: 2021-01-23 14:54:40
'''
from color import color

class Cell():
    def __init__(self,width:int,height:int,color,bold,pattern:str):
        '''
        创建一个单元格，所有的图案都绘制在该网格内
        --width：网格宽度
        --height：网格高度（正方形通常为width：height = 2:1）
        --color：单元格内图案的的颜色
        --bold：单元格内字体是否加粗，若加粗则"b"
        '''
        self.width = width
        self.height = height
        self.color = color
        self.bold = bold
        self.pattern = pattern
        # init the blank cell
        self.matrix = self.init_matrix()
        self.read_pattern(self.pattern)

    def init_matrix(self,symbol=" ") -> list:
        '''Init the cell matrix. Each argument in matrix is a symbol (default:space)'''
        matrix = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(symbol)
            matrix.append(row)
        return matrix

    def show_matrix(self):
        '''Print all arguments in matrix, could be used in debugging'''
        matrix = self.matrix
        for row in matrix:
            print(row)        

    def show_cell(self):
        '''Print the final appearence of cell'''
        matrix = self.matrix
        c = self.color
        bold = self.bold
        for row in matrix:
            line = ""
            for bit in row:
                line += color(bit,color=c,bold=bold)
            print(line)

    def read_pattern(self,pattern:str):
        '''Save the pattern in matrix'''
        row_list = pattern.split("\n")
        c = self.color
        bold =self.bold
        for m in range(len(row_list)):
            for n in range(len(row_list[m])):
                self.matrix[m][n] = color(row_list[m][n],color=c,bold=bold)

    def show_range(self):
        '''Show the shape of the cell'''
        self.matrix = self.init_matrix("#")
        self.show_cell() 
        self.read_pattern(self.pattern)

    def shape(self) -> list:
        '''Return the shape of the cell:[row,col]'''
        return [self.height,self.width]


##### Old code ######
    # def zero(self,digit=0):
    #     matrix = []
    #     for i in range(self.height):
    #         row = []
    #         for j in range(self.width):
    #             row.append(digit)
    #         matrix.append(row)
    #     return matrix

    # def show_range(self):
    #     '''打印单元格的范围'''
    #     self.matrix = self.zero(-1)
    #     self.print_cell()
    
    # def print_matrix(self):
    #     '''打印单元格的数字矩阵，用于调试'''
    #     matrix = self.matrix
    #     for row in matrix:
    #         line = ""
    #         for bit in row:
    #             line += str(bit)
    #         print(line)

    # def print_cell(self):
    #     '''打印单元格，用于预览效果'''
    #     matrix = self.matrix
    #     c = self.color
    #     bold = self.bold
    #     for row in matrix:
    #         line = ""
    #         for bit in row:
    #             line += trans_d2s(bit)
    #         print(color(line,color=c,bold=bold))
    
    # def read_pattern(self,pattern:str):
    #     '''将输入的字符串图像转为数字矩阵储存'''
    #     row_list = pattern.split("\n")
    #     for m in range(len(row_list)):
    #         for n in range(len(row_list[m])):
    #             self.matrix[m][n] = trans_s2d(row_list[m][n])

####### 用数字矩阵记录棋盘真的是好主意吗，颜色怎么实现？？----2021.01.22
# def trans_d2s(digit:int) -> str:
#     '''The map from digits to symbols'''
#     d = str(digit)
#     mapping = {
#         "-1":"#",
#         "0":" ",
#         "1":"-",
#         "2":"|",
#         "3":"/",
#         "4":"\\"
#     }
#     return mapping[d]

# def trans_s2d(string:str) -> int:
#     '''Mapping from symbols to digits'''
#     mapping = {
#         " ":0,
#         "-":1,
#         "|":2,
#         "/":3,
#         "\\":4
#     }
#     return mapping[string]
