'''
Description: Class: The chess of the flight-chess game
version: 
Author: TianyuYuan
Date: 2021-01-24 22:19:47
LastEditors: TianyuYuan
LastEditTime: 2021-01-30 10:45:07
'''
import time
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
        self.routine_lenght = len(self.routine)
        self.loc = 0 # 棋子的当前位置
        self.dst = 0 # 棋子该回合的应该到达的终点
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
        SKY.remove_pattern_in_cell_matrix(self.planecell,pos)
        SKY.refresh_matrix()

    def fly(self,num):
        '''Move forward <num> locations'''
        self.loc += num

    def crash(self):
        '''Plane crashed and go back to the startpoint'''
        self.take_off()
        self.loc = 0
        self.land_on_map()

    def meet_corner(self) -> int:
        '''若遇到空白转角，则往前一格'''
        pos_type = self.routine[self.loc][-1]
        if pos_type == 'ctr' or pos_type == 'ctl' or\
            pos_type == 'cbr' or pos_type == 'cbl':
            return 1
        else:
            return 0

    def meet_same_color(self) -> bool:
        '''若遇到相同颜色格子，则跳到前方相同颜色的格子上'''
        pos_type = self.routine[self.loc][-1]
        if pos_type == self.color:
            return True
        else:
            return False
    
    def meet_friends(self) -> bool:
        # FIXME '''检测是否遇到自己的飞机，遇到则返回1'''
        pos_m = self.routine[self.loc][0]
        pos_n = self.routine[self.loc][1]
        pattern_list = SKY.cell_matrix[pos_m][pos_n]
        for pattern in pattern_list:
            if pattern.color == self.color:
                return True
            else:
                continue
        return False

    def meet_enemies(self) -> bool:
        # TODO'''检测是否遇到对手，遇到则返回1'''
        pos_m = self.routine[self.loc][0]
        pos_n = self.routine[self.loc][1]
        return False

    def check_end(self) -> bool:
        '''检查是否位于终点'''
        if self.loc == self.routine_lenght:
            return True
        else:
            return False

    def check_shortcut(self) -> bool:
        '''check if the plane meets the shortcut'''
        if self.loc == 21:
            return True
        else:
            return False
    
    def onestep(self,step:int):
        '''行动一步，包括刷新屏幕，停留1s'''
        if step > 0:
            step = 1
        else:
            step = -1
        self.take_off()
        self.fly(step)
        self.land_on_map()
        SKY.show_sky()
        time.sleep(0.5)

    def check_while_moving(self,steps:int) ->int:
        '''移动过程中的检查，返回还应该移动的步数'''
        if self.check_end():
            # 遇到重点，反向且移动步数减一
            return steps*(-1)+1
        else:
            pass
        if self.meet_corner():
            return steps
        else:
            # 若棋子在正向移动，则步数减1；反之加一
            signal = steps/abs(steps)
            steps = signal*(abs(steps)-1)
            return steps

    def checking_when_done(self,flag) -> tuple:
        '''
        移动结束时进行的检测
        + return 100: reach the end
        + return 32: reach the shortcut, change the flag
        + return 4: meet the same color cell, change the flag
        + return 1: one step more
        + return -1: meet the enemy
        + return 0: end the turn
        '''
        #  终点检测
        if self.check_end():
            return 100,flag
        # 空白转角检测
        if self.meet_corner():
            return 1,flag
        # 颜色捷径检测
        if flag == False:
            if self.check_shortcut():
                return 33,True
            if self.meet_same_color():
                return 4,True
        # 碰撞检测
        if self.meet_friends():
            return 1,flag
        elif self.meet_enemies():
            return -1,flag
        else: 
            return 0,flag

    def animate(self,steps,flag=False):
        while steps != 0:
            self.onestep(steps)
            # 移动中的检查
            steps = self.check_while_moving(steps)

        # 移动后的检查    
        signal,flag = self.checking_when_done(flag)
        if signal == 100:
            # TODO add winning method
            print("Congrates!")
        elif signal == 33:
            self.take_off()
            self.loc = 33
            self.land_on_map()
            SKY.show_sky()
            time.sleep(0.5)
            self.animate(0,flag)
        elif signal == 4:
            self.animate(4,flag)
        elif signal == 1:
            self.animate(1,flag)
        elif signal == -1:
            # TODO 触发他人坠毁
            print("OOps!")
        else:
            pass

# def init_all_chess
y1_plane = Plane('y',1)
y2_plane = Plane('y',2)
y3_plane = Plane('y',3)
y4_plane = Plane('y',4)
y1_plane.animate(19)