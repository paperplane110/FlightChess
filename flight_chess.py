'''
Description: 飞行棋
version: 
Author: TianyuYuan
Date: 2021-01-20 22:40:54
LastEditors: TianyuYuan
LastEditTime: 2021-01-31 23:28:07
'''
from player import Player


def is_moveable(player) -> bool:
    '''检测有可移动的棋子吗？'''
    num = player.dice.point
    if num != 6:
        # 当投掷点数不是6时，存在飞机不在机场，则有可以移动的飞机
        for plane in player.planes:
            if plane.in_airport == False:
                return True
    return False

def is_input_index_valid(player,index) -> bool:
    '''检测用户输入的序号是否合法'''
    try:
        index = int(index)
    except ValueError:
        # input is not number
        print("Please enter digits in range of [1,4], thanks!")
        return False
    num = player.dice.point
    plane = player.planes[index-1]
    if index > 4:
        print("The input number is out of range. Please choose a number between [1,4]")
    if plane.win == True:
        print("This plane is already complete its task. Please choose another plane")
        return False
    if num != 6 and plane.in_airport == True:
        print("The plane{} is not ready to take off. Please choose another plane".format(index))
        return False
    return True

def is_win(player) -> bool:
    '''检测该玩家是否赢了游戏'''
    for plane in player.planes:
        if plane.win == False:
            return False
    return True

def turn(player) -> bool:
    '''在一回合内，player的所有行为
    + return: True to continue
    + return: False to end the game
    '''
    # 投骰子 # 显示骰子
    player.roll_dice()
    # 有可移动的吗？
    if is_moveable(player) == False:
        # TODO 打印信息 下一回合
        return True
    # 有可移动的
    while True:
        # 询问移动哪个
        print("Please choose a plane to fly")
        index = input()
        # 输入检测，是否合法
        if is_input_index_valid(player, index) == False:
            continue
        else:
            player.move_plane(index)
            # 输赢判断
            if is_win(player):
                # TODO 游戏结束，打印结果
                return False
            else:
                return True

def next_player(num):
    if num == 3:
        num = 0
    else:
        num += 1
    return num

def play(players):
    num = 0
    while True:
        player = players[num]
        is_continue = turn(player)
        if is_continue == False:
            break
        num = next_player(num)
    # this round is over
    return 0
                    
def run():
    # TODO打印欢迎

    # 初始化游戏
    player1 = Player('r')
    player2 = Player('g')
    player3 = Player('b')
    player4 = Player('y')
    players = [player1,player2,player3,player4]
    play(players)
    # TODO ask another round
    print("End game")


if __name__ == "__main__":
    run()