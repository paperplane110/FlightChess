<!--
 * @Description: ReadME
 * @version: 
 * @Author: TianyuYuan
 * @Date: 2021-01-23 13:25:37
 * @LastEditors: TianyuYuan
 * @LastEditTime: 2021-02-01 00:41:43
-->
# FlightChess
Flight chess game played on termial

[![Software | 100 Days of Code](https://www.software.com/badges/100-days-of-code)](https://www.software.com/100-days-of-code)
## Usage
Open the terminal and go to a dir where you want to install this game, then clone the code to the local path.
### For example:
```bash
# go to the directory where you feel comfortable
cd ~/Desktop/
# clone the repository
git clone https://github.com/paperplane110/FlightChess.git
# start the Game
python3 flight_chess.py
```
## Game Composition


## DevLog
### 2021.01.23
+ 数字矩阵记录真的好吗？
    + 方便对于空格的覆盖 0+n=n
    + 空格对于下层元素不影响 n+0=n
    + <font color=red>数字与字符需要mapping转换处理
    + 不好处理颜色问题</font>
+ 直接将字符append到地图矩阵中的优劣
    + 方便字符的导入与输出，所见即所得
    + 颜色问题解决了
    + <font color=red>图层之间的覆盖问题，空格位于下层可以直接被覆盖
    + 空格位于上层，会覆盖下层字符
    + 需要另外加上if判断来解决这个问题</font>
### 2021.01.25
+ python没有switch怎么办？
    + 首选利用dict的映射关系来实现switch
    + 实在不行利用多重if-elif-else
+ 实例化不成功的话，多检查一下class()的括号有没有加
+ 需要重复使用的list，使用pop()的时候要谨慎
+ <font color=red>上一轮棋子的图层如何删除？
+ 在一个回合中，棋子移动时各项检查顺序是如何的？每种进行多少次检查？</font>
### 2021.01.26
+ 回复：
    + 上一轮棋子的图层如何删除？
        + 在每次渲染天空之前，清空字符串矩阵
    + 在一个回合中，棋子移动时各项检查顺序是如何的？每种进行多少次检查？
        + 棋子移动结束时，终点检测、捷径检测、颜色检测是高优的
        + 每次结束移动，都需要终点检测、覆盖检测和碰撞检测
### 2021.01.29
+ 飞机怎么运动：
  + 首先得到该回合应该移动的步数
  + 一步一步移动，每移动一步刷新一次屏幕
    + 移动过程中需要进行的检测：
      + 空白转角检测：遇到空白块，移动步长+1
      + 终点检测：遇到终点，反向移动
  + 移动结束，按顺序进行以下检测
    + 终点检测
    + （）格子颜色检测
    + （）格子捷径检测
    + 友方碰撞检测
    + 对手碰撞检测
  + 结果
    + 若到达终点->该棋子消失，玩家得一分
    + 若格子颜色相同->前进至下一个相同颜色的格子
      + 可能情况：
        1. 飞行结束时必然落在相同颜色的格子
        2. 飞行路程中可能有空白转角
        3. 飞行路程中可能碰到终点
        4. 飞行结束后可能发生碰撞
        5. 飞行结束后可能位于捷径起点
        6. 飞行结束时可能位于最后的直线跑道
      + <font color=red>结论：
        + 飞行时进行空白转角检验和终点检验
        + 飞行结束时不再进行颜色和捷径检验
        + 飞行结束时仅进行碰撞检验</font>
    + 若格子为捷径起点->直接跳到捷径终点
      + 可能情况：
        + 飞行结束时必然落在相同颜色格子
        + 捷径的终点可能有棋子
      + <font color=red>结论：
        + 必须是跳转，而不是一格一格移动
        + 飞行结束时不做颜色检验
        + 飞行结束时进行碰撞检验</font>
    + 若发生友方碰撞->前进一格
      + 可能情况：
        + 到达终点
        + 遇到空白转角
        + 继续碰撞
        + 遇到颜色相同格子
        + 遇到捷径起点
      + <font color=red>结论:
        + 结束后进行终点/空白/碰撞检测
        + 颜色和捷径检测视情况而定，碰撞之前已进行过相同颜色或捷径奖励，则不再进行检测；反之则进行检测</font>
    + 若发生对手碰撞->对方返回飞机场
+ ### 结论
  + 每次<font color=green>移动过程中</font>必须进行的检测有
    1. 终点
    2. 空白块
  + 每次<font color=green>移动结束时</font>必须进行的检测有
    1. 终点；
    2. 空白块；
    3. (?)捷径检测；
    4. (?)颜色检测；
    5. 碰撞检测
  + 颜色和捷径检测需要有一个flag，记录该回合是否已经进行了相关的奖励
  + 若已进行过颜色或捷径奖励，则在该回合不再进行第二次奖励

### 2021.01.30
+ 队友检测
  + 首先知道自己在routine上的位置
  + 通过映射关系，得到自己在cell_matrix上的位置
  + 遍历该位置的所有图层
  + 出现己方颜色2次，即为遇到队友
    + 因为棋子本身也位于该位置，所以己方颜色出现的次数应该是2次，而非1次
+ 敌方检测
  + 首先知道自己在routine上的位置
  + 通过映射关系，得到自己在cell_matrix上的位置
  + 遍历该位置的所有图层
  + 若出现颜色含有‘bg’字段，且与己方颜色不相同，则检测到敌方飞机

### 2021.01.31
+ 玩家
  + 初始化：什么颜色，飞机
  + 行为：
    + 投骰子
    + 移动飞机
    + ~~判断自己是否赢了~~ -> 是否应该交给game rule去记录和判断，可能需要重构代码plane.py

### 2021.02.01
+ 屏幕刷新太慢，费眼睛，或许考虑去掉动画
