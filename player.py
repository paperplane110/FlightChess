'''
Description: class: player 
version: 
Author: TianyuYuan
Date: 2021-01-31 18:21:40
LastEditors: TianyuYuan
LastEditTime: 2021-01-31 18:21:41
'''
from plane import Plane

class Player():
    '''玩家类：包括玩家的初始化，掷骰子，决定移动哪个棋子，输赢判断等'''
    def __init__(self,color:int):
        self.color = color

    def init_planes(self):
        '''initialize four planes'''
        for i in range(4):
            plane1 = Plane(self.color,1)
