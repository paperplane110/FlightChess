'''
Description: 飞行棋棋盘，负责棋盘的打印
version: 
Author: TianyuYuan
Date: 2021-01-20 22:44:19
LastEditors: TianyuYuan
LastEditTime: 2021-02-01 00:45:28
'''
import copy
from draw import Cell
from color import color
from patterns import WIDTH,HEIGHT
from patterns import BlankCell,TestCell1,TestCell2,AirlineCell,Airport,Corner
from patterns import C_BOTTOM_RIGHT,C_BOTTOM_LEFT,C_TOP_LEFT,C_TOP_RIGHT
from patterns import create_arrow,create_planecell
from map_info import AIRLINE

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
c_bl = Corner(C_BOTTOM_LEFT)
c_tr = Corner(C_TOP_RIGHT)
c_tl = Corner(C_TOP_LEFT)
a_right = create_arrow('right')
a_up = create_arrow('up')
a_down = create_arrow('down')
a_left = create_arrow('left')

###### Build the Sky ######
class Sky():
    '''
    The sky of the flight chess
    '''
    def __init__(self,cell_width,cell_height,cells_in_edge):
        """
        Initiation of the Sky
        + cell_width：单元格宽度
        + cell_height：单元格高度
        + cells_in_edge：正方形棋盘一边有多少个单元格
        + cell_matrix：单元格矩阵，三维矩阵，矩阵的前两维为cell的平面坐标，第三维为cell所包含的图层，默认为空图层。
        每一个cell都拥有一个list，list中的元素都为'类'，方便后续可直接调用cell中的类的方法
            + e.g. cell_matrix[0][0] = [e_cell,Y_AIRPORT,y1_plane] 
        //此处的y1_plane为class Plane，可直接调用plane.crash()
            + 其意义为，在[0,0]位置绘制三个图层：e_cell空单元格，黄色飞机场，黄色飞机一号
            + 不同图层如有重叠，只允许字符覆盖空格，空格不会覆盖下层字符
        """
        self.width = cell_width
        self.height = cell_height
        self.edge = cells_in_edge
        # init sky
        self.matrix = self.init_sky()
        self.cell_matrix = self.init_cell_matrix()
        self.load_sky_map()
        self.refresh_matrix()
        self.plane_location = {}

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

    def add_pattern2cell_matrix(self,instance,pos:list):
        '''将图案实例添加到cell_matrix中(recalled in plane.py)'''
        m,n = pos[0],pos[1]
        self.cell_matrix[m][n].append(instance)

    def remove_pattern_in_cell_matrix(self,instance,pos:list):
        '''将图案实例从cell_matrix的某一位置移除(recalled in plane.py)'''
        m,n = pos[0],pos[1]
        self.cell_matrix[m][n].remove(instance)
        
    def show_sky(self):
        '''打印单元格，用于刷新屏幕'''
        matrix = self.matrix
        line = ""
        for row in matrix:
            for bit in row:
                line += bit
            line += "\n"
        print(line,end="\r") 

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
        - position: pattern在单元格矩阵上的坐标
        - return: pattern左上角在sky大矩阵上的坐标
        '''
        cell_m = position[0] # row
        cell_n = position[1] # col
        matrix_m = cell_m * self.height
        matrix_n = cell_n * self.width
        return [matrix_m,matrix_n]
    
    def clear_matrix(self):
        '''清空matrix'''
        for m in range(self.height*self.edge):
            for n in range(self.width*self.edge):
                self.matrix[m][n] = color(' ')

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
            c = cell_info[-1] # color
            pos = cell_info[0:2]
            try:
                cell_instance = C2P_DICT[c]
            except KeyError:
                print("Error: Color is not included:{}".format(cell_info))
                exit()
            load_from_list(cell_matrix,cell_instance,pos)   
            
    def refresh_matrix(self) -> list:
        '''根据cell_matrix中各单元格的图案记录，将相应的字符书写到sky的大矩阵中'''
        def strip_color(string:str):
            '''将字符串的颜色标记去掉'''
            return string.split("m")[-2][0]
        def add_pattern(x,y,matrix:list,pattern) -> list:
            '''
            将pattern中的字符写入matrix，pattern位置由其左上角的坐标决定
            - x：pattern绘制的起点的行坐标
            - y：pattern绘制的起点的列坐标
            - matrix：sky_matrix 大矩阵，background
            - pattern：pattern.matrix 单元格矩阵，记录了每个位置的字符和颜色
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
                        # print("Error: Pattern overlapping! Cell matrix position [{},{}]".format(i,j))
                        pass
            return matrix
        # main
        self.clear_matrix()   # 每次都必须在空白的屏幕上重新绘制，因此需要清空画布
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

    def plane_loc_wrt(self,plane_name:str,plane_instance:object):
        '''记录各个飞机的位置'''
        self.plane_location[plane_name] = plane_instance

    def plane_loc_recall(self,plane_name) -> list:
        '''调用plane的位置'''
        return self.plane_location[plane_name]

    def test_zebra_map(self):
        '''测试cell_matrix,refresh_matrix等方法是否可行'''
        cell_matrix = self.cell_matrix
        edge = self.edge
        for i in range(edge):
            for j in range(edge):
                if (i+j)%2 == 0:
                    cell_matrix[i][j]=[t1_cell]
                else:
                    cell_matrix[i][j]=[t2_cell]
        self.clear_matrix()
        self.refresh_matrix()
        self.show_sky()

# mapping from color:str to pattern:object
C2P_DICT = {
    'k':k_cell,
    'r':r_cell,
    'g':g_cell,
    'b':b_cell,
    'y':y_cell,
    'cbl':c_bl,
    'cbr':c_br,
    'ctl':c_tl,
    'ctr':c_tr,
    'au':a_up,
    'ad':a_down,
    'al':a_left,
    'ar':a_right
}
        
SKY = Sky(WIDTH,HEIGHT,15)

###### Test Code ######
# SKY.test_zebra_map()
# SKY.show_sky()