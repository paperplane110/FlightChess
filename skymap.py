'''
Description: 飞行棋棋盘，负责棋盘的打印
version: 
Author: TianyuYuan
Date: 2021-01-20 22:44:19
LastEditors: TianyuYuan
LastEditTime: 2021-01-23 15:31:24
'''
import copy
from draw import Cell
from color import color
from patterns import BlankCell,BlackCell

# Init patterns
blank_cell = BlankCell()
black_cell = BlackCell()

class Sky():
    '''The sky of the flight chess'''
    def __init__(self,cell_width,cell_height,cells_in_edge):
        """
        Initiation of the Sky
        --width：单元格宽度
        --height：单元格高度
        --cells_in_edge：正方形棋盘一边有多少个单元格
        --cell_matrix：单元格矩阵，三维矩阵，矩阵的前两维为cell的平面坐标，第三维为cell所包含的图层，默认为空图层
        """
        self.width = cell_width
        self.height = cell_height
        self.edge = cells_in_edge
        # init sky
        self.matrix = self.init_sky()
        self.cell_matrix = self.init_cell_matrix()

    def init_sky(self,symbol=" ") -> list:
        '''生成sky的二维矩阵，将sky所有位置赋值=symbol'''
        matrix = []
        edge = self.edge
        for i in range(self.height*edge):
            row = []
            for j in range(self.width*edge):
                row.append(symbol)
            matrix.append(row)
        return matrix

    def init_cell_matrix(self,pattern=blank_cell) -> list:
        '''生成单元格矩阵，默认每个单元格为空图层'''
        matrix = []
        edge = self.edge
        for i in range(edge):
            row = []
            for j in range(edge):
                row.append([pattern])
            matrix.append(row)
        return matrix
        
    def show_sky(self):
        '''打印单元格，用于预览效果'''
        matrix = self.matrix
        for row in matrix:
            line = ""
            for bit in row:
                line += bit
            print(line) 

    def show_range(self):
        matrix = copy.deepcopy(self.matrix)
        matrix = self.init_sky('#')
        for row in matrix:
            line = ""
            for bit in row:
                line += bit
            print(line) 

    def cell2matrix(self,position:list) -> list:
        '''
        单元格矩阵与sky大矩阵的映射关系
        --position: pattern在单元格矩阵上的坐标
        --return: pattern左上角在sky大矩阵上的坐标
        '''
        cell_m = position[0] # row
        cell_n = position[1] # col
        matrix_m = cell_m * self.height
        matrix_n = cell_n * self.width
        return [matrix_m,matrix_n]
    
    def refresh_matrix(self) -> list:
        '''根据cell_matrix中各单元格的图案记录，将相应的字符书写到sky的大矩阵中'''
        cell_matrix = self.cell_matrix
        sky_matrix = self.matrix
        edge = self.edge
        for i in range(edge):
            for j in range(edge):
                for pattern in cell_matrix[i][j]:
                    position = self.cell2matrix([i,j])
                    x = position[0]
                    y = position[1]
                    # 该函数已经改写了sky_matrix，因此无需return
                    add_pattern(x,y,sky_matrix,pattern.matrix)




def add_pattern(x,y,matrix:list,pattern:list) -> list:
    '''
    将pattern中的字符写入matrix，pattern位置由其左上角的坐标决定
    --x：pattern绘制的起点的行坐标
    --y：pattern绘制的起点的列坐标
    --matrix：sky_matrix 大矩阵，background
    --pattern：pattern.matrix 单元格矩阵，记录了每个位置的字符和颜色
    '''
    m,n = pattern.shape()
    for i in range(m):
        for j in range(n):
            bg_symbol = strip_color(matrix[x+i][y+j])
            fg_symbol = strip_color(pattern[i][j])
            if fg_symbol == " ":
                continue
            elif bg_symbol == " ":
                matrix[x+i][y+j] = pattern[i][j]
            else:
                print("Error: Pattern overlapping! Cell matrix position [{},{}]".format(i,j))
    return matrix

def strip_color(string:str):
    '''将字符串的颜色标记去掉'''
    return string.split("m")[-2][0]

sky = Sky(6,3,7)
sky.show_range()
sky.show_sky()