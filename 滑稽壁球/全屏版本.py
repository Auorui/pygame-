import pygame,sys

pygame.init()
vInfo=pygame.display.Info()
size=width,height=vInfo.current_w,vInfo.current_h


# size=width,height=600,400
speed=[1,1]
BLACK=0,0,0
# screen=pygame.display.set_mode(size)
# screen=pygame.display.set_mode(size,pygame.RESIZABLE)  #窗口大小可调
# screen=pygame.display.set_mode(size,pygame.NOFRAME)   #无边框
screen=pygame.display.set_mode(size,pygame.FULLSCREEN)  #全屏
pygame.display.set_caption("pygame壁球")
ball = pygame.image.load("E:\pycharm\picture\滑稽.gif")
ballrect=ball.get_rect()

fps=300
fclock = pygame.time.Clock()   #创建一个clock对象，用于操作时间


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
    ballrect=ballrect.move(speed[0],speed[1])
    if ballrect.left<0 or ballrect.right>width:
        speed[0]=-speed[0]
    if ballrect.top<0 or ballrect.bottom>height:
        speed[1]=-speed[1]
    screen.fill(BLACK)
    screen.blit(ball,ballrect)  #将一个图像绘制在另一个图像上，即将src绘制到dest位置上。通过Rect对象引导对壁球的绘制
    pygame.display.update()
    fclock.tick(fps)       #控制帧速率，即窗口刷新率，其表示每秒钟300次帧刷新
