import time
import threading
import turtle

# print(now)
# print(time.strftime("%Y-%m-%d %H:%M:%S",now))


def drawLine(psize,line,draw):
    turtle.pensize(psize)
    turtle.pu()
    turtle.fd(line)
    if draw:
        turtle.pd()
    else:
        turtle.pu()
    
    turtle.fd(3*line+5)
    turtle.pu()
    turtle.fd(line)
    turtle.right(90)

def drawNum(psize,line,num):
    # turtle.colormode(255)
    # turtle.color(eval(color))
    # 第一条线
    if num in [2, 3, 4, 5, 6, 8, 9]:
        drawLine(psize,line,True)
    else:
        drawLine(psize,line,False)
 
    if num in [0, 1, 3, 4, 5, 6, 7, 8, 9]:
        drawLine(psize,line,True)
    else:
        drawLine(psize,line,False)
 
    if num in [0, 2, 3, 5, 6, 8, 9]:
        drawLine(psize,line,True)
    else:
        drawLine(psize,line,False)
 
    if num in [0, 2, 6, 8]:
        drawLine(psize,line,True)
    else:
        drawLine(psize,line,False)
 
    turtle.left(90)
 
    if num in [0, 4, 5, 6, 8, 9]:
        drawLine(psize,line,True)
    else:
        drawLine(psize,line,False)
 
    if num in [0, 2, 3, 5, 6, 7, 8, 9]:
        drawLine(psize,line,True)
    else:
        drawLine(psize,line,False)
 
    if num in [0, 1, 2, 3, 4, 7, 8, 9]:
        drawLine(psize,line,True)
    else:
        drawLine(psize,line,False)
 
    turtle.pu()
    turtle.left(180)
    # turtle.fd(40)  # 绘制后面数字间隔位置
    turtle.update()

def numReturn(num):
    x = list(map(int,str(num)))
    # print(len(x))
    return x

def penRun(l):
    turtle.pu()
    turtle.fd(l)
    turtle.pd()


def drawData(tm_year,tm_mon,tm_mday):
    turtle.goto(-265,-80)
    year = numReturn(tm_year)
    month = numReturn(tm_mon)
    day = numReturn(tm_mday)
    for i in range(len(year)):
        num_year = year[i]
        drawNum(3,3,num_year)
        penRun(10)
    turtle.fd(30)
    penRun(10)
    if len(month) == 1:
        drawNum(3,3,0)
        penRun(10)
        drawNum(3,3,month[0])
        penRun(10)
    else:
        for i in range(len(month)):
            num_month = month[i]
            drawNum(3,3,num_month)
            penRun(10)
    turtle.fd(30)
    penRun(10)
    if len(day) == 1:
        drawNum(3,3,0)
        penRun(10)
        drawNum(3,3,day[0])
        penRun(10)
    else:
        for i in range(len(day)):
            num_day = day[i]
            drawNum(3,3,num_day)
            penRun(10)

def drawTime(tm_hour,tm_min,tm_sec):
    turtle.goto(-300,0)
    hour = numReturn(tm_hour)
    min = numReturn(tm_min)
    sec = numReturn(tm_sec)
    if len(hour) == 1:
        drawNum(5,5,0)
        penRun(20)
        drawNum(5,5,hour[0])
        penRun(20)
    else:
        for i in range(len(hour)):
            num_hour = hour[i]
            drawNum(5,5,num_hour)
            penRun(20)
    turtle.fd(40)
    penRun(20)
    if len(min) == 1:
        drawNum(5,5,0)
        penRun(20)
        drawNum(5,5,min[0])
        penRun(20)
    else:
        for i in range(len(min)):
            num_min = min[i]
            drawNum(5,5,num_min)
            penRun(20)
    turtle.fd(40)
    penRun(20)
    if len(sec) == 1:
        drawNum(5,5,0)
        penRun(20)
        drawNum(5,5,sec[0])
        penRun(20)
    else:
        for i in range(len(sec)):
            num_sec = sec[i]
            drawNum(5,5,num_sec)
            penRun(20)

def draw():
    now = time.localtime()
    turtle.hideturtle()  # 隐藏画笔
    turtle.speed(0)  # 最
    turtle.tracer(0) #追踪速度
    turtle.pu()
    turtle.fd(-300)
    turtle.pencolor('#f3f3f3')
    drawData(8888,88,88)
    turtle.pu()
    drawTime(88,88,88)
    turtle.pu()
    turtle.pencolor("red")
    drawTime(now.tm_hour,now.tm_min, now.tm_sec)
    turtle.pu()
    turtle.pencolor("blue")
    drawData(now.tm_year,now.tm_mon, now.tm_mday)
    timer = threading.Timer(0.1, draw)  # 利用多线程库定时刷新
    timer.start()
    turtle.done()

if __name__ == "__main__":
    draw()