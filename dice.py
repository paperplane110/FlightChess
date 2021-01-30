'''
Description: class Dice. return a random number
version: 
Author: TianyuYuan
Date: 2021-01-29 23:34:06
LastEditors: TianyuYuan
LastEditTime: 2021-01-30 10:41:44
'''
import random

class Dice():
    def __init__(self,player:str) -> None:
        self.player = player
    def roll_dice(self) -> int:
        return random.randint(1,6)