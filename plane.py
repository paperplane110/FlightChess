'''
Description: Class: The chess of the flight-chess game
version: 
Author: TianyuYuan
Date: 2021-01-24 22:19:47
LastEditors: TianyuYuan
LastEditTime: 2021-01-25 02:43:21
'''
from skymap import SKY
from patterns import create_planecell
from map_info import R_ROUTINE,G_ROUTINE,B_ROUTINE,Y_ROUTINE
from map_info import R_AIRPORT,G_AIRPORT,B_AIRPORT,Y_AIRPORT
from map_info import R_WAIT,G_WAIT,B_WAIT,Y_WAIT

class Plane():
    '''飞行棋棋子，包括棋子的初始化，棋子路线、位置、移动、应答等方法'''
    def __init__(self,color,num):
        self.color = color
        self.num = num
        self.planecell = create_planecell(color,num)
        self.object_name = "{}{}_plane".format(color,num)
        self.routine = self.init_routine()
        self.loc = 0
        self.land_on_map()
        
    def init_routine(self) -> list:
        '''Choose the routine based on plane's color'''
        color = self.color
        num = self.num-1
        if color == 'r':
            # airport->waiting area->routine
            # careful with []+[]+[[],[],..], would go wrong
            return [R_AIRPORT[num]]+[R_WAIT]+R_ROUTINE
        elif color == 'g':
            return [G_AIRPORT[num]]+[G_WAIT]+G_ROUTINE
        elif color == 'b':
            return [B_AIRPORT[num]]+[B_WAIT]+B_ROUTINE
        else:
            return [Y_AIRPORT[num]]+[Y_WAIT]+Y_ROUTINE

    def land_on_map(self):
        '''Write the planecell on SKY'''
        # routine = [[0,0,'k],[...],...]
        pos = self.routine[self.loc][0:2]
        SKY.add_pattern2cell_matrix(self.planecell,pos)
        SKY.refresh_matrix()

    def take_off(self):
        '''Remove the last time record on SKY'''
        pos = self.routine[self.loc][0:2]
        SKY.remove_patter_in_cell_matrix(self.planecell,pos)
        SKY.refresh_matrix()

    def fly(self,num):
        '''Move forward <num> locations'''
        self.loc += num

    def crash(self):
        '''Plane crashed and back to the startpoint'''
        self.take_off()
        self.loc = 0
        self.land_on_map()

    def meet_corner(self):
        '''若遇到空白转角，则往前一格'''
        pos_type = self.routine[self.loc][-1]
        if pos_type == 'ctr' or pos_type == 'ctl' or\
            pos_type == 'cbr' or pos_type == 'cbl':
            self.loc += 1

    def meet_same_color(self):
        '''若遇到相同颜色格子，则跳到前方相同颜色的格子上'''
        pos_type = self.routine[self.loc][-1]
        if pos_type == self.color:
            self.loc += 4
            '''前进的四个中出现了空白转角'''
            if pos_type != self.routine[self.loc][-1]:
                self.loc += 1
                
    def check_shortcut(self):
        '''check if the plane meets the shortcut'''
        if self.loc == 21:
            self.loc == 33
    
    def action(self,num):
        '''all action of plane in one turn'''
        self.take_off()
        self.fly(num)
        self.meet_same_color()
        self.land_on_map()

# def init_all_chess
y1_plane = Plane('y',1)
y2_plane = Plane('y',2)
y3_plane = Plane('y',3)
y4_plane = Plane('y',4)
y1_plane.action(3)
SKY.show_sky()