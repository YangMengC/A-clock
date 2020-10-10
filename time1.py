import time
import threading
import turtle


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

def drawData(tm_new):
    tm = numReturn(tm_new)
    if len(tm) == 1:
        turtle.pencolor('#f3f3f3')
        drawNum(3,3,8)
        turtle.pu()
        turtle.fd(-20)
        turtle.pencolor("blue")
        drawNum(3,3,0)
        penRun(10)
        turtle.pencolor('#f3f3f3')
        drawNum(3,3,8)
        turtle.pu()
        turtle.fd(-20)
        turtle.pencolor("blue")
        drawNum(3,3,tm[0])
        penRun(10)
    else:
        for i in range(len(tm)):
            turtle.pencolor('#f3f3f3')
            drawNum(3,3,8)
            turtle.pu()
            turtle.fd(-20)
            turtle.pencolor("blue")
            drawNum(3,3,tm[i])
            penRun(10)

def drawTime(tm_new):
    tm = numReturn(tm_new)
    if len(tm) == 1:
        turtle.pencolor('#f3f3f3')
        drawNum(5,5,8)
        turtle.pu()
        turtle.fd(-30)
        turtle.pencolor("red")
        drawNum(5,5,0)
        penRun(20)
        turtle.pencolor('#f3f3f3')
        drawNum(5,5,8)
        turtle.pu()
        turtle.fd(-30)
        turtle.pencolor("red")
        drawNum(5,5,tm[0])
        penRun(20)
    else:
        for i in range(len(tm)):
            turtle.pencolor('#f3f3f3')
            drawNum(5,5,8)
            turtle.pu()
            turtle.fd(-30)
            turtle.pencolor("red")
            drawNum(5,5,tm[i])
            penRun(20)

def draw(year_old,month_old,day_old,hour_old,minute_old):
    now = time.localtime()
    turtle.hideturtle()  # 隐藏画笔
    # turtle.speed(10)  # 最
    # turtle.tracer(0) #追踪速度
    turtle.pu()
    if now.tm_hour == hour_old and now.tm_min == minute_old:
        turtle.goto(60,0)
        drawTime(now.tm_sec)
        turtle.pu()
    elif now.tm_hour == hour_old and now.tm_min != minute_old:
        turtle.goto(60,0)
        drawTime(now.tm_sec)
        turtle.pu()
        turtle.goto(-120,0)
        drawTime(now.tm_min)
        turtle.pu()
    elif now.tm_hour != hour_old:
        turtle.goto(60,0)
        drawTime(now.tm_sec)
        turtle.pu()
        turtle.goto(-120,0)
        drawTime(now.tm_min)
        turtle.pu()
        turtle.goto(-300,0)
        drawTime(now.tm_hour)
        turtle.pu()
    
    if now.tm_year == year_old and now.tm_mon == month_old and now.tm_mday ==day_old:
        turtle.goto(60,0)
        turtle.pu()
    elif now.tm_year == year_old and now.tm_mon == month_old:
        turtle.goto(55,-80)
        drawData(now.tm_mday)
        turtle.pu()
    elif now.tm_year == year_old and now.tm_mon != month_old:
        turtle.goto(-65,-80)
        drawData(now.tm_mon)
        turtle.pu()
        turtle.goto(55,-80)
        drawData(now.tm_mday)
        turtle.pu()
    elif now.tm_year != year_old:
        turtle.goto(-265,-80)
        drawData(now.tm_year)
        turtle.pu()
        turtle.goto(-65,-80)
        drawData(now.tm_mon)
        turtle.pu()
        turtle.goto(55,-80)
        drawData(now.tm_mday)
        turtle.pu()
    
    hour_old = now.tm_hour
    minute_old = now.tm_min
    year_old = now.tm_year
    month_old = now.tm_mon
    day_old = now.tm_mday
    timer = threading.Timer(0.1, draw(year_old,month_old,day_old,hour_old,minute_old))  # 利用多线程库定时刷新
    timer.start()

if __name__ == "__main__":
    hour_old = 0
    minute_old = 0
    year_old = 0
    month_old = 0
    day_old = 0
    turtle.hideturtle()  # 隐藏画笔
    turtle.speed(0)  # 最kuai
    turtle.tracer(10) #追踪速度
    turtle.pu()
    turtle.goto(-190,0)
    turtle.pd()
    turtle.fd(40)
    
    turtle.pu()
    turtle.goto(-10,0)
    turtle.pd()
    turtle.fd(40)

    draw(year_old,month_old,day_old,hour_old,minute_old)
    
    turtle.done()