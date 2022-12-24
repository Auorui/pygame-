import pygame as pg
import sys
from random import randint
import time


pg.init()         #对pygame内部各功能模块进行初始化创建及变量设置，默认调用


game_window = pg.display.set_mode((600, 500))   #初始化显示窗口，第一个size是一个二值元组，分别表示窗口的宽度和高度
pg.display.set_caption("接弹珠游戏")  #显示窗口的标题内容
score = 0
font = pg.font.Font(None, 60)
window_color = (0, 0, 0)  # 设置窗口颜色——黑色
ball_color = (0, 255, 0)  # 设置球的颜色-——绿色
rect_color = (255, 0, 0)  # 设置挡板颜色——红色
move_x = 1
move_y = 1
ball_x = randint(20, 580) #球的初始位置随机
ball_y = randint(20, 480)
points = 1
count = 0


while True:
    game_window.fill(window_color)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
    mouse_x, mouse_y = pg.mouse.get_pos()
    pg.draw.circle(game_window, ball_color, (ball_x, ball_y), 20)   #在窗口内画球
    pg.draw.rect(game_window, rect_color, (mouse_x, 490, 100, 10))  #在窗口内画矩形接拍
    ball_x += move_x
    ball_y += move_y
    my_score = font.render(str(score), False, (255, 255, 0))    #设置分数显示，黄色
    game_window.blit(my_score, (500, 30))


    ball_x += move_x
    ball_y += move_y
    if ball_x <= 20 or ball_x >= 580:          #左右两侧墙壁
        move_x = -move_x                       #碰到左右两侧墙壁时，X坐标变为反方向
    if ball_y <= 20:                           #碰到上方墙壁时，Y坐标改变方向
        move_y = -move_y
    elif ball_x >(mouse_x - 20) and ball_x <(mouse_x + 120) and ball_y >= 470:
        move_y = -move_y                      #下方接到球，改变Y坐标方向，并加分
        score += points
        count += 1                            #接球次数加1
        if count == 5:
            count = 0
            points += points                  #分数翻倍
            if move_x > 0:
                move_x += 1
            else:
                move_x -= 1
            move_y -= 1


    elif ball_y > 480 and (ball_x <= mouse_x - 20 or ball_x >= mouse_x + 120):
        ball_y = 490                         #没有接到球，退出程序
        break
    pg.display.update()                     #更新窗口，保证窗口始终打开
    time.sleep(0.03)