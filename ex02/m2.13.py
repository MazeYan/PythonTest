# 使用turtle库函数绘制一个包含9个同心圆的靶盘

from turtle import *

setup(650, 300, 200, 200)
pensize(1)
pencolor("#EE82EE")
for i in range(10):
    penup()
    goto(0, -(i+1)*10)
    pendown()
    circle(10 * (i+1), None)
    penup()
    goto(0, 0)
    pendown()
