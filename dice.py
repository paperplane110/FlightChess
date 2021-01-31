'''
Description: class Dice. return a random number
version: 
Author: TianyuYuan
Date: 2021-01-29 23:34:06
LastEditors: TianyuYuan
LastEditTime: 2021-02-01 00:38:26
'''
import random
from draw import Cell
from patterns import dice_pattern
from skymap import SKY

# 相应颜色骰子所出现的位置
COLOR_POSITION={
    'r':[9,5],
    'g':[5,9],
    'b':[9,9],
    'y':[5,5]
    }

class Dice():
    def __init__(self,color:str) -> None:
        self.width = 6
        self.height = 3
        self.color = color
        self.point = 6 # 记录骰子所投掷的点数，初始化为6
        self.pos = COLOR_POSITION[self.color]
        self.last_turn_dice = None
        # dice initialization
        self.init_dice()

    def init_dice(self):
        string = 'DICE'
        pattern = dice_pattern(string)
        dice = Cell(self.width,self.height,self.color,'b',pattern)
        SKY.add_pattern2cell_matrix(dice,self.pos)
        SKY.refresh_matrix()
        self.last_turn_dice = dice

    def roll_dice(self):
        '''掷骰子，并将结果打印在terminal上'''
        num = random.randint(1,6)
        self.point = num
        num = " 0{} ".format(str(num))
        pattern = dice_pattern(num)
        dice = Cell(self.width,self.height,self.color,'b',pattern)
        # 先拿起骰子，擦除上一轮骰子在cell上留下的记录，以免写不到sky上
        SKY.remove_pattern_in_cell_matrix(self.last_turn_dice,self.pos)
        SKY.refresh_matrix()
        # 放下骰子，并展示在terminal上
        SKY.add_pattern2cell_matrix(dice,self.pos)
        SKY.refresh_matrix()
        SKY.show_sky()
        self.last_turn_dice = dice