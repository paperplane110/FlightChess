'''
Description: 飞行棋棋盘，负责棋盘的打印
version: 
Author: TianyuYuan
Date: 2021-01-20 22:44:19
LastEditors: TianyuYuan
LastEditTime: 2021-01-24 01:03:58
'''
import copy
from draw import Cell
from color import color
from patterns import BlankCell,TestCell1,TestCell2,AirlineCell,Airport,Corner
from patterns import C_BOTTOM_RIGHT,C_BOTTOM_lEFT,C_TOP_LEFT,C_TOP_RIGHT
from map_info import AIRLINE,R_ROUTINE,B_ROUTINE,G_ROUTINE,Y_ROUTINE

###### Instantiation patterns #######
e_cell = BlankCell()
t1_cell = TestCell1()
t2_cell = TestCell2()
k_cell = AirlineCell('k')
r_cell = AirlineCell('r')
g_cell = AirlineCell('g')
y_cell = AirlineCell('y')
b_cell = AirlineCell('b')
r_air = Airport('r')
g_air = Airport('g')
y_air = Airport('y')
b_air = Airport('b')
c_br = Corner(C_BOTTOM_RIGHT)
c_bl = Corner(C_BOTTOM_lEFT)
c_tr = Corner(C_TOP_RIGHT)
c_tl = Corner(C_TOP_LEFT)

###### Build the Sky ######
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
        self.load_sky_map()
        self.refresh_matrix()

    def init_sky(self,symbol=" ") -> list:
        '''生成sky的二维矩阵，将sky所有位置赋值=symbol'''
        matrix = []
        edge = self.edge
        for i in range(self.height*edge):
            row = []
            for j in range(self.width*edge):
                row.append(color(symbol))
            matrix.append(row)
        return matrix

    def init_cell_matrix(self,pattern=e_cell) -> list:
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
                    add_pattern(x,y,sky_matrix,pattern)

    def test_zebra_map(self):
        '''测试cell_matrix,refresh_matrix等方法是否可行'''
        cell_matrix = self.cell_matrix
        edge = self.edge
        for i in range(edge):
            for j in range(edge):
                if (i+j)%2 == 0:
                    cell_matrix[i][j].append(b_cell)
                else:
                    cell_matrix[i][j].append(g_cell)
        self.refresh_matrix()
        self.show_sky()

    def load_sky_map(self):
        '''将飞行棋盘手动写入cell_matrix'''
        def load_from_list(cell_matrix,cell,pos):
            m = pos[0]
            n = pos[1]
            cell_matrix[m][n].append(cell)
        # init
        cell_matrix = self.cell_matrix
        # Airport
        cell_matrix[0][0].append(y_air)
        cell_matrix[0][12].append(g_air)
        cell_matrix[12][0].append(r_air)
        cell_matrix[12][12].append(b_air)
        # Airline Cell
        for cell_info in AIRLINE:
            c = cell_info.pop(-1)
            if c == 'r':
                load_from_list(cell_matrix,r_cell,cell_info)
            elif c == 'b':
                load_from_list(cell_matrix,b_cell,cell_info)
            elif c == 'g':
                load_from_list(cell_matrix,g_cell,cell_info)
            elif c == 'y':
                load_from_list(cell_matrix,y_cell,cell_info)
            elif c == 'cbl':
                load_from_list(cell_matrix,c_bl,cell_info)
            elif c == 'cbr':
                load_from_list(cell_matrix,c_br,cell_info)
            elif c == 'ctl':
                load_from_list(cell_matrix,c_tl,cell_info)
            elif c == 'ctr':
                load_from_list(cell_matrix,c_tr,cell_info)
            else:
                print("Fatal Error, wrong color in CELL_DICT:{}".format(cell_info))
                exit()


def add_pattern(x,y,matrix:list,pattern) -> list:
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
            fg_symbol = strip_color(pattern.matrix[i][j])
            if fg_symbol == " ":
                continue
            elif bg_symbol == " ":
                matrix[x+i][y+j] = pattern.matrix[i][j]
            else:
                print("Error: Pattern overlapping! Cell matrix position [{},{}]".format(i,j))
    return matrix

def strip_color(string:str):
    '''将字符串的颜色标记去掉'''
    return string.split("m")[-2][0]
        
sky = Sky(6,3,15)
sky.show_sky()