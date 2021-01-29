'''
Description: init patterns and cells
version: 
Author: TianyuYuan
Date: 2021-01-22 22:44:59
LastEditors: TianyuYuan
LastEditTime: 2021-01-27 13:27:41
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

###### TestCell ######
TEST_WIDTH = WIDTH
TEST_HEIGHT = HEIGHT
TEST_PATTERN1 = "\
######\n\
######\n\
######"
TEST_PATTERN2 = "\
......\n\
......\n\
......"
class TestCell1(Cell):
    def __init__(self):
        super().__init__(width=TEST_WIDTH,height=TEST_HEIGHT,color='k',bold=False,pattern=TEST_PATTERN1)
class TestCell2(Cell):
    def __init__(self):
        super().__init__(width=TEST_WIDTH,height=TEST_HEIGHT,color='k',bold=False,pattern=TEST_PATTERN2)

###### Airline ######
BUTTON_WIDTH = WIDTH
BUTTON_HEIGHT = HEIGHT
BUTTON_BOLD = 'b'
BUTTON = "\
+----+\n\
|    |\n\
+----+"

class AirlineCell(Cell):
    def __init__(self,color):
        super().__init__(width=BUTTON_WIDTH,height=BUTTON_HEIGHT,color=color,bold=BUTTON_BOLD,pattern=BUTTON)

###### Airport ######
PORT_WIDTH = WIDTH*3
PORT_HEIGHT = HEIGHT*3
PORT_BOLD = False
PORT_PATTERN = "\
@@@@@@@@@@@@@@@@@@\n\
$  \\  :    :  /  $\n\
$    \\:....:/    $\n\
$'''''/----\\'''''$\n\
$    :|    |:    $\n\
$.....\\----/.....$\n\
$    /:'''':\\    $\n\
$  /  :    :  \\  $\n\
@@@@@@@@@@@@@@@@@@"

class Airport(Cell):
    def __init__(self,color):
        super().__init__(width=PORT_WIDTH,height=PORT_HEIGHT,color=color,bold=PORT_BOLD,pattern=PORT_PATTERN)

###### Corner #######
C_BOTTOM_RIGHT = "\
+---+%\n\
|  %' \n\
+%'   "
C_BOTTOM_lEFT = "\
&+---+\n\
 `&  |\n\
   `&+"
C_TOP_RIGHT = "\
+&.   \n\
|  &. \n\
+---+&"
C_TOP_LEFT ="\
   .%+\n\
 .%  |\n\
%+---+"
class Corner(Cell):
    def __init__(self,pattern):
        super().__init__(width=WIDTH,height=HEIGHT,color='k',bold='b',pattern=pattern)

###### Plane ######
def plane_pattern(num:int) -> str:
    '''create plane pattern with the given num'''
    pattern = '\
      \n\
 (p{}) \n\
      '.format(num)
    return pattern

class PlaneCell(Cell):
    def __init__(self,color,pattern):
        super().__init__(width=WIDTH,height=HEIGHT,color=color,bold='b',pattern=pattern)

def create_planecell(color,num) -> object:
    '''According to given color&num, create a PlaneCell object and return it'''
    color_mapping = {
        'r':'rbg',
        'g':'gbg',
        'b':'bbg',
        'y':'ybg'
    }
    pattern = plane_pattern(num)
    planecell = PlaneCell(color_mapping[color],pattern)
    return planecell

###### Arrow ######
A_UP = "\
  /\\  \n\
  ||  \n\
  ||  "
A_DOWN = "\
  ||  \n\
  ||  \n\
  \\/  "
A_LEFT = "\
      \n\
<=====\n\
      "
A_RIGHT = "\
      \n\
=====>\n\
      "
class ArrowUp(Cell):
    def __init__(self):
        super().__init__(width=WIDTH,height=HEIGHT,color='b',bold='b',pattern=A_UP)
class ArrowDown(Cell):
    def __init__(self):
        super().__init__(width=WIDTH,height=HEIGHT,color='y',bold='b',pattern=A_DOWN)
class ArrowLeft(Cell):
    def __init__(self):
        super().__init__(width=WIDTH,height=HEIGHT,color='g',bold='b',pattern=A_LEFT)
class ArrowRight(Cell):
    def __init__(self):
        super().__init__(width=WIDTH,height=HEIGHT,color='r',bold='b',pattern=A_RIGHT)
def create_arrow(direction:str) -> object:
    if direction == 'up':
        arrow = ArrowUp()
    elif direction == 'down':
        arrow = ArrowDown()
    elif direction == 'left':
        arrow = ArrowLeft()
    elif direction == 'right':
        arrow = ArrowRight()
    else:
        print("Error, arrow direction out of range")
        exit()
    return arrow
       
# pc = PinkCell()
# pc.show_cell()
# def strip_color(string:str):
#     return string.split("m")[-2][0]
# print(strip_color(pc.matrix[0][0]))
# g_port = Airport('g')
# g_port.show_cell()
# c_tl = Corner(C_TOP_LEFT)
# c_tl.show_cell()
# p1 = create_planecell('bbg',1)
# p1.show_cell()