from turtle import *

'''
    函数square用于生成得分小方块放在画布上
    x：表示小方块的横坐标位置
    y：表示小方块的纵坐标位置
    size：表示小方块的大小
    color_name：表示小方块的颜色
'''

def square(x,y,size,color_name):
    up() #提起画笔，避免画笔移动到指定位置时留下痕迹
    goto(x,y) #将画笔移动至制定位置
    down() #画笔移动到指定位置时放下
    color(color_name) #设置画笔颜色
    begin_fill() #开始颜色填充

    for i in range(4): #绘制一个小方块
        forward(size)
        left(90)

    end_fill() #结束颜色填充