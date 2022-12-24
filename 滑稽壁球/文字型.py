import pygame, sys
import pygame.freetype

pygame.init()
icon = pygame.image.load("E:\pycharm\picture\滑稽图标.gif")  # 设置图标
pygame.display.set_icon(icon)
size = width, height = 600, 400
speed = [1, 1]
BLACK = 0, 0, 0
GOLD = 255, 251, 0
pos = [230, 160]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("pygame文字绘制")
f1 = pygame.freetype.Font("C:/Windows/Fonts/msyh.ttc", 36)

# f1rect=f1.render_to(screen,pos,"滑稽果",fgcolor=GOLD,size=25)
f1surf, f1rect = f1.render("滑稽果", fgcolor=GOLD, size=25)

# ball = pygame.image.load("E:\pycharm\picture\滑稽.gif")
# ballrect = ball.get_rect()

fps = 300
fclock = pygame.time.Clock()  # 创建一个clock对象，用于操作时间

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if pos[0] < 0 or pos[0] + f1rect.width > width:
        speed[0] = -speed[0]
    if pos[1] < 0 or pos[1] + f1rect.height > height:
        speed[1] = -speed[1]
    pos[0] = pos[0] + speed[0]
    pos[1] = pos[1] + speed[1]
    # ballrect = ballrect.move(speed[0], speed[1])

    screen.fill(BLACK)

    # f1rect=f1.render_to(screen,pos,"世界和平",fgcolor=GOLD,size=50)
    f1surf, f1rect = f1.render("滑稽果", fgcolor=GOLD, size=25)
    screen.blit(f1surf, (pos[0], pos[1]))
    pygame.display.update()
    fclock.tick(fps)  # 控制帧速率，即窗口刷新率，其表示每秒钟300次帧刷新