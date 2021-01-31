'''
Description: Class: The chess of the flight-chess game
version: 
Author: TianyuYuan
Date: 2021-01-24 22:19:47
LastEditors: TianyuYuan
LastEditTime: 2021-01-31 23:21:41
'''
import time
from skymap import SKY
from patterns import create_planecell
from map_info import R_ROUTINE,G_ROUTINE,B_ROUTINE,Y_ROUTINE
from map_info import R_AIRPORT,G_AIRPORT,B_AIRPORT,Y_AIRPORT
from map_info import R_WAIT,G_WAIT,B_WAIT,Y_WAIT

class Plane():
    '''飞行棋棋子，包括棋子的初始化，棋子路线、位置、移动、应答等方法'''
    def __init__(self,color:str,num:int):
        '''
        初始化飞行棋棋子
        + color: 颜色['r','y','g','b']
        + num: 编号[1,2,3,4]
        '''
        self.color = color
        self.num = num
        self.object_name = "{}{}_plane".format(color,num) # 实例名与object_name是无关的，object_name是程序内部对于该棋子的叫法
        self.in_airport = True
        self.win = False
        # init plane's pattern
        self.planecell = create_planecell(color,num)
        self.routine = self.init_routine()
        self.routine_lenght = len(self.routine)
        self.loc = 0 # 棋子的当前在航线中的位置
        self.pos = self.routine[self.loc] # 棋子在cell_matrix上的位置
        self.dst = 0 # FIXME 用途？：棋子该回合的应该到达的终点 
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
        pos = self.pos[0:2]
        SKY.add_pattern2cell_matrix(self.planecell,pos)
        SKY.plane_loc_wrt(self.object_name,self)
        SKY.refresh_matrix()

    def take_off(self):
        '''Remove the last time record on SKY'''
        pos = self.pos[0:2]
        SKY.remove_pattern_in_cell_matrix(self.planecell,pos)
        SKY.refresh_matrix()

    def refresh_pos(self):
        '''每次更新loc后，需要刷新pos'''
        self.pos = self.routine[self.loc]

    def fly(self,num):
        '''Move forward <num> locations'''
        self.loc += num
        self.refresh_pos()

    def crash(self):
        '''Plane crashed and go back to the startpoint'''
        self.take_off()
        self.loc = 0
        self.refresh_pos()
        self.land_on_map()

    def meet_corner(self) -> int:
        '''若遇到空白转角，则往前一格'''
        pos_type = self.pos[-1]
        if pos_type == 'ctr' or pos_type == 'ctl' or\
            pos_type == 'cbr' or pos_type == 'cbl':
            return 1
        else:
            return 0

    def meet_same_color(self) -> bool:
        '''若遇到相同颜色格子，则跳到前方相同颜色的格子上'''
        pos_type = self.pos[-1]
        if pos_type == self.color:
            return True
        else:
            return False
    
    def meet_friends(self) -> bool:
        '''检测是否遇到自己的飞机，遇到则返回True'''
        for name,plane_instance in SKY.plane_location.items():
            if plane_instance.color == self.color and plane_instance.num != self.num and plane_instance.pos == self.pos:
                return True
            else:
                continue
        return False

    def meet_enemies(self) -> bool:
        '''检测是否遇到对手，遇到则返回1'''
        for name,plane_instance in SKY.plane_location.items():
            if plane_instance.color != self.color and plane_instance.pos == self.pos:
                #触发对方的坠毁方法
                plane_instance.crash()
                SKY.show_sky()
                return True
            else:
                continue
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
        '''行动一步，包括刷新屏幕，停留0.5s'''
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

    def event_of_check(self,signal,flag):
        '''移动后的检查，所触发的事件'''
        if signal == 100:
            # TODO add winning method
            print("Congrates!")
        elif signal == 33:
            self.take_off()
            self.loc = 33
            self.refresh_pos()
            self.land_on_map()
            SKY.show_sky()
            time.sleep(0.5)
            self.animate(0,flag)
        elif signal == 4:
            self.animate(4,flag)
        elif signal == 1:
            self.animate(1,flag)
        elif signal == -1:
            # 触发对方坠毁的事件写在了检测方法中，方便一些
            print("OOps!")
        else:
            pass

    def animate(self,steps,flag=False):
        # 移动动画
        while steps != 0:
            self.onestep(steps)
            # 移动中的检查
            steps = self.check_while_moving(steps)

        # 移动后的检查    
        signal,flag = self.checking_when_done(flag)
        self.event_of_check(signal,flag)

###### Test Code ######
# def init_all_chess
y1_plane = Plane('y',1)
y2_plane = Plane('y',2)
y3_plane = Plane('y',3)
y4_plane = Plane('y',4)
r1_plane = Plane('r',1)
r2_plane = Plane('r',2)
def test_shortcuts():
    y1_plane.animate(19)
def test_meet_same_color():
    y1_plane.animate(3)
def test_meet_friend():
    y1_plane.animate(19)
    y2_plane.animate(19)
def test_meet_enemy():
    y1_plane.animate(4)
    r1_plane.animate(16)
    r2_plane.animate(16)
if __name__ == '__main__':
    # test_shortcuts()
    # test_meet_same_color()
    # test_meet_friend()
    test_meet_enemy()
