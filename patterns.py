'''
Description: init patterns and cells
version: 
Author: TianyuYuan
Date: 2021-01-22 22:44:59
LastEditors: TianyuYuan
LastEditTime: 2021-01-23 12:10:37
'''
from draw import Cell

###### Buttons ######
BUTTON_WIDTH = 5
BUTTON_HEIGHT = 3
BUTTON_BOLD = 'b'
BUTTON = "\
+---+\n\
|   |\n\
+---+"

class RedCell(Cell):
    def __init__(self):
        super().__init__(width=BUTTON_WIDTH,height=BUTTON_HEIGHT,color="r",bold=BUTTON_BOLD,pattern=BUTTON)

class GreenCell(Cell):
    def __init__(self):
        super().__init__(width=BUTTON_WIDTH,height=BUTTON_HEIGHT,color="g",bold=BUTTON_BOLD,pattern=BUTTON)

class PinkCell(Cell):
    def __init__(self):
        super().__init__(width=BUTTON_WIDTH,height=BUTTON_HEIGHT,color='p',bold=BUTTON_BOLD,pattern=BUTTON)

class BlueCell(Cell):
    def __init__(self):
        super().__init__(width=BUTTON_WIDTH,height=BUTTON_HEIGHT,color='b',bold=BUTTON_BOLD,pattern=BUTTON)


pc = PinkCell()
pc.show_cell()