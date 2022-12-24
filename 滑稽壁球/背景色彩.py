import pygame,sys

pygame.init()
icon = pygame.image.load("E:\pycharm\picture\滑稽图标.gif")  #设置图标
pygame.display.set_icon(icon)
size=width,height=600,400
speed=[1,1]
BLACK=0,0,0

screen=pygame.display.set_mode(size,pygame.RESIZABLE)  #窗口大小可调

pygame.display.set_caption("pygame壁球")
ball = pygame.image.load("E:\pycharm\picture\滑稽.gif")
ballrect=ball.get_rect()

fps=300
fclock = pygame.time.Clock()   #创建一个clock对象，用于操作时间
still=False
bgcolor=pygame.Color("black")

def RGBChannel(a):
    return 0 if a <0 else (255 if a>255 else int(a))
while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                speed[0]=speed[0] if speed[0]==0 else (abs(speed[0])-1)*int(speed[0]/abs(speed[0]))  #else后面的代码解决负号问题
            elif event.key == pygame.K_RIGHT:
                speed[0]=speed[0]+1 if speed[0]>0 else speed[0]-1
            elif event.key == pygame.K_UP:
                speed[1]=speed[1]+1 if speed[1]>0 else speed[1]-1
            elif event.key == pygame.K_DOWN:
                speed[1] = speed[1] if speed[1] == 0 else (abs(speed[1]) - 1) * int(speed[1] / abs(speed[1]))
            elif event.key == pygame.K_ESCAPE:
                sys.exit()
        elif event.type == pygame.VIDEORESIZE:   #窗口大小可调信息
            size=width,height=event.size[0],event.size[1]
            screen = pygame.display.set_mode(size,pygame.RESIZABLE)
    ballrect=ballrect.move(speed[0],speed[1])
    if pygame.display.get_active():    #窗口感知
        ballrect = ballrect.move(speed[0],speed[1])
    if ballrect.left<0 or ballrect.right>width:
        speed[0]=-speed[0]
    if ballrect.top<0 or ballrect.bottom>height:
        speed[1]=-speed[1]

    bgcolor.r = RGBChannel(ballrect.left*255/width)
    bgcolor.g = RGBChannel(ballrect.top*255/height)
    bgcolor.b = RGBChannel(min(speed[0],speed[1])*255/max(speed[0],speed[1],1))
    screen.fill(bgcolor)
    screen.blit(ball,ballrect)  #将一个图像绘制在另一个图像上，即将src绘制到dest位置上。通过Rect对象引导对壁球的绘制
    pygame.display.update()
    fclock.tick(fps)       #控制帧速率，即窗口刷新率，其表示每秒钟300次帧刷新