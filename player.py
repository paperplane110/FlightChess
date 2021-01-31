'''
Description: class: player 
version: 
Author: TianyuYuan
Date: 2021-01-31 18:21:40
LastEditors: TianyuYuan
LastEditTime: 2021-01-31 21:19:27
'''
from plane import Plane
from dice import Dice

class Player():
    '''玩家类：包括玩家的初始化，掷骰子，决定移动哪个棋子'''
    def __init__(self,color:str):
        self.color = color
        self.planes = self.init_planes()
        self.dice = self.init_dice()

    def init_planes(self) -> list:
        '''initialize four planes'''
        plane1 = Plane(self.color,1)
        plane2 = Plane(self.color,2)
        plane3 = Plane(self.color,3)
        plane4 = Plane(self.color,4)
        return [plane1,plane2,plane3,plane4]

    def init_dice(self):
        return Dice(self.color)

    def roll_the_dice(self):
        '''行为：掷骰子'''
        self.dice.roll_dice()

    def move_plane(self,index:int) -> bool:
        '''
        行为：移动飞机
        + index: 飞机的序号
        + return: 是否移动成功
        '''
        num = self.dice.point
        plane = self.planes[index-1]
        # check if the plane is in the airport
        if plane.in_airport:
            if num == 6:
                plane.animate(1)
            else:
                return False
        else:
            plane.animate(num)
        return True


