<!--
 * @Description: ReadME
 * @version: 
 * @Author: TianyuYuan
 * @Date: 2021-01-23 13:25:37
 * @LastEditors: TianyuYuan
 * @LastEditTime: 2021-01-25 02:50:02
-->
# FlightChess
Flight chess game played on termial
## Usage
Open the terminal and go to a dir where you want to install this game, then clone the code to the local path.
### For example:
```bash
cd ~/Desktop/
git clone https://github.com/paperplane110/FlightChess.git
```
## Game Composition



## Thinking
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
---
### 2021.01.25
+ python没有switch怎么办？
    + 首选利用dict的映射关系来实现switch
    + 实在不行利用多重if-elif-else
+ 实例化不成功的话，多检查一下class()的括号有没有加
+ 需要重复使用的list，使用pop()的时候要谨慎
+ <font color=red>上一轮棋子的图层如何删除？</font>
