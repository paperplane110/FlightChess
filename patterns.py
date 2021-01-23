'''
Description: init patterns and cells
version: 
Author: TianyuYuan
Date: 2021-01-22 22:44:59
LastEditors: TianyuYuan
LastEditTime: 2021-01-23 14:44:07
'''
from draw import Cell
###### Unit #######
WIDTH = 6
HEIGHT = 3

###### Blank ######
BLANK_WIDTH = WIDTH
BLANK_HEIGHT = HEIGHT
BLANK_PATTERN = "\
      \n\
      \n\
      "
class BlankCell(Cell):
    def __init__(self):
        super().__init__(width=BLANK_WIDTH,height=BLANK_HEIGHT,color='k',bold=False,pattern=BLANK_PATTERN)

###### Buttons ######
BUTTON_WIDTH = WIDTH
BUTTON_HEIGHT = HEIGHT
BUTTON_BOLD = 'b'
BUTTON = "\
+----+\n\
|    |\n\
+----+"

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

class BlackCell(Cell):
    def __init__(self):
        super().__init__(width=BUTTON_WIDTH,height=BUTTON_HEIGHT,color='k',bold=BUTTON_BOLD,pattern=BUTTON)

# pc = PinkCell()
# pc.show_cell()