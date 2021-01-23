'''
Description: init patterns and cells
version: 
Author: TianyuYuan
Date: 2021-01-22 22:44:59
LastEditors: TianyuYuan
LastEditTime: 2021-01-24 00:11:24
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
$  \\          /  $\n\
$    \\      /    $\n\
$     /----\\     $\n\
$     |    |     $\n\
$     \\----/     $\n\
$    /      \\    $\n\
$  /          \\  $\n\
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

# pc = PinkCell()
# pc.show_cell()
# def strip_color(string:str):
#     return string.split("m")[-2][0]
# print(strip_color(pc.matrix[0][0]))
# g_port = Airport('g')
# g_port.show_cell()
# c_tl = Corner(C_TOP_LEFT)
# c_tl.show_cell()