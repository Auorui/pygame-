import pygame, sys

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("pygame框架")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()


# #屏幕尺寸和模式
# pygame.display.set_mode()   #设置相关屏幕模式
# pygame.display.Info()   #生成屏幕相关信息
#
# #窗口标题和图标
# pygame.display.set_caption()   #设置标题信息
# pygame.display.set_icon()   #设置图标信息
# pygame.display.get_caption()   #获得图标
#
# #窗口感知和刷新
# pygame.display.get_caption()
# pygame.display.flip()
# pygame.display.update()

# #处理事件
# pygame.event.get()
# pygame.event.poll()  #从队列中获取一个事件
# pygame.event.clear()
#
# #操作事件队列能缓存事件类型
# pygame.event.set_blocked()  #控制哪些类型事件不允许被保存到事件队列中
# pygame.event.get_allowed()   #...允许...
# pygame.event.set_blocked()    #测试某个事件类型是否被事件队列所禁止，返回布尔值
#
# #生成事件
# pygame.event.post()  #创建一个事件，并将其放入事件队列
# pygame.event.Event()  #创建一个给定类型的事件

# #鼠标移动事件
# pygame.event.MOUSEMOTION
#     event.pos #鼠标当前坐标，相对于窗口左上角
#     event.rel #相对距离，相对于上次事件
#     event.buttoms #鼠标按键状态，对应于鼠标的三个键
#
# #鼠标键释放事件
# pygame.event.MOUSEBUTTONUP
#     event.pos
#     event.button
#
# #鼠标键释放事件
# pygame.event.MOUSEBUTTONDOWN
#     event.pos
#     event.button #鼠标按下键编号n,左键为1，右键为3


# #RGB常用颜色
# 255 255 255 白色
# 0 0 0 黑色
# 190 190 190 灰色
# 0 100 0 深绿色
# 255 215 0 金色
# 238 130 238 紫罗兰
# 160 32 240 紫色
# alpha通道表示不透明度，取值0-255 默认是255
# alpha通道值越大，不透明度越高，255表示不透明











