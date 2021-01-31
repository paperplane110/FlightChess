'''
Description: class Dice. return a random number
version: 
Author: TianyuYuan
Date: 2021-01-29 23:34:06
LastEditors: TianyuYuan
LastEditTime: 2021-01-31 19:41:36
'''
import random
from draw import Cell
from patterns import dice_pattern
from skymap import SKY

# 相应颜色骰子所出现的位置
COLOR_POSITION={
    'r':[13,1],
    'g':[1,13],
    'b':[13,13],
    'y':[1,1]
    }

class Dice():
    def __init__(self,color:str) -> None:
        self.width = 6
        self.height = 3
        self.color = color
        self.pos = COLOR_POSITION[self.color]
        self.last_turn_dice = None

    def init_dice(self):
        num = "06"
        pattern = dice_pattern(num)
        dice = Cell(self.width,self.height,self.color,'b',pattern)
        SKY.add_pattern2cell_matrix(dice,self.pos)
        SKY.refresh_matrix()
        self.last_turn_dice = dice

    def roll_dice(self):
        '''掷骰子，并将结果打印在terminal上'''
        num = random.randint(1,6)
        pattern = dice_pattern(num)
        dice = Cell(self.width,self.height,self.color,'b',pattern)
        # 先拿起骰子，擦除上一轮骰子在cell上留下的记录，以免写不到sky上
        SKY.remove_pattern_in_cell_matrix(self.last_turn_dice)
        SKY.refresh_matrix()
        # 放下骰子，并展示在terminal上
        SKY.add_pattern2cell_matrix(dice,self.pos)
        SKY.refresh_matrix()
        SKY.show_sky()
        self.last_turn_dice = dice