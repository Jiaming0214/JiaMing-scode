#函数引用区
from turtle import *
from snake_base import square
from random import randrange
from time import sleep

#变量声明区
apple_x=randrange(-200,180,10)
apple_y=randrange(-190,190,10) #生成第一个苹果的坐标
snake=[[0,0],[10,0],[20,0],[30,0],[40,0],[50,0]] #生成蛇的初始位置，后面的坐标为前
ward_x=10 #控制蛇移动的方向
ward_y=0

#函数定义区
def ward_change(x,y): #此函数用于调整蛇的移动方向
    global ward_x
    global ward_y
    ward_x=x
    ward_y=y

def is_inside():  #此函数用于判断蛇是否还是限定区域内
    if -200<=snake[-1][0]<=180 and -190<=snake[-1][1]<=190:
        return True
    else:
        return False

def is_self(): #此函数用于判断蛇是否咬到了自身
    for n in range(len(snake)-1):
        if snake[-1][0] == snake[n][0] and snake[-1][1] == snake[n][1]:
            return True
    return False

def gameLoop(): #游戏进行中
    global apple_x,apple_y,snake,ward_x,ward_y

    listen() #读取键盘上的反应
    if ward_y == 0: #当蛇在水平移动时，a，d左右移动无法实现
        onkey(lambda:ward_change(0,10),"w")
        onkey(lambda:ward_change(0,-10),"s")
        onkey(None,"a")
        onkey(None,"d")
    elif ward_x == 0: #当蛇在垂直移动式，w，s上下移动无法实现
        onkey(lambda: ward_change(10, 0), "d")
        onkey(lambda:ward_change(-10,-0),"a")
        onkey(None,"w")
        onkey(None,"s")

    snake.append([snake[-1][0]+ward_x,snake[-1][1]+ward_y]) #生成蛇移动后的数组

    if snake[-1][0]!=apple_x or snake[-1][1]!=apple_y: #判断蛇是否吃到了苹果
        snake.pop(0) #若没有吃到，则长度不变，将蛇原来的第一节删除，保证蛇的长度不变
    else: #若吃到了，则长度加长，蛇原来的第一节不必要删除，保证蛇长度的增加
        apple_x=randrange(-200,180,10)
        apple_y=randrange(-190,190,10)
    
    if not is_inside() or is_self(): #确定了蛇的变化后，判断蛇是否达到游戏死亡条件
        square(snake[-1][0], snake[-1][-1], 10, "red") #若蛇已经达到了死亡条件，则蛇的头部变为红色
        update()
        sleep(2) #等待两秒后，游戏回归初始化，重新开始
        apple_x = randrange(-200, 180, 10)
        apple_y = randrange(-190, 190, 10)
        snake = [[0, 0], [10, 0], [20, 0], [30, 0], [40, 0], [50, 0]]
        ward_x = 10
        ward_y = 0
    #若蛇未达到死亡条件，则无事发生，游戏继续

    clear()
    square(-210,-200,410,"black")
    square(-200,-190,390,"white")
    for n in range(len(snake)):
        square(snake[n][0],snake[n][1],10,"black")
    square(apple_x,apple_y,10,"red")
    ontimer(gameLoop,100)
    update()

#主程序区
setup(420,420,0,0) #设置画布及开始时画笔位置
hideturtle() #隐藏画笔
tracer(False) #隐藏绘制过程
gameLoop()
done() #结束，同时不让画布消失