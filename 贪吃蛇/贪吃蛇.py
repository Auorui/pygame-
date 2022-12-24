import pygame
import random

# 设置大小长度
W = 800
H = 600
size = (W, H)
# 设定游戏行列数
COL = 40
ROW = 30
# 定义要使用的类(用来记录点坐标)
class Point:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def copy(self):
        return Point(row=self.row, col=self.col)

# 定义绘画的函数
def rect(point, color):
    cell_width = W / COL
    cell_height = H / ROW
    left = point.col * cell_width
    top = point.row * cell_height
    pygame.draw.rect(screen, color, (left, top, int(cell_width), int(cell_height)))

# 随机生成食物
def genfood():
    while True:
        food_x = Point(row=random.randint(0, ROW - 1), col=random.randint(0, COL - 1))
        if food_x.row != head.row and food_x.col != head.col and food_x not in snakebody:
            return food_x

# pygame初始化框架
pygame.init()

screen = pygame.display.set_mode(size)
pygame.display.set_caption('贪吃蛇')
clock = pygame.time.Clock()
# 定义蛇身
snakebody = []
snakebody_color = (200, 200, 200)
# 定义蛇头
head = Point(row=0, col=0)
head_color = (0, 128, 200)
# 定义食物
food = genfood()
food_color = (255, 255, 0)
# 计分
score = 0
# 方向
direct = 'right'
# 循环
quit = True
while quit:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = False
        elif event.type == pygame.KEYDOWN:
            if event.key == 1073741906 or event.key == 119:
                if direct == 'right' or direct == 'left':
                    direct = 'up'
            elif event.key == 1073741905 or event.key == 115:
                if direct == 'right' or direct == 'left':
                    direct = 'down'
            elif event.key == 1073741904 or event.key == 97:
                if direct == 'up' or direct == 'down':
                    direct = 'left'
            elif event.key == 1073741903 or event.key == 100:
                if direct == 'up' or direct == 'down':
                    direct = 'right'
    # 处理蛇身
    snakebody.insert(0, head.copy())
    # 处理吃到食物
    eat = (head.row == food.row and head.col == food.col)
    if eat:
        food = genfood()
        score += 1
    else:
        if len(snakebody) != 0:
            snakebody.pop()
    # 移动
    if direct == 'up':
        head.row -= 1
    elif direct == 'down':
        head.row += 1
    elif direct == 'left':
        head.col -= 1
    elif direct == 'right':
        head.col += 1
    # 设定死亡
    dead = False
    if head.row < 0 or head.col < 0 or head.row >= ROW or head.col >= COL:
        dead = True
    for snake in snakebody:
        if snake.row == head.row and snake.col == head.col:
            dead = True
    if dead:
        quit = False
    # 渲染画面
    # pygame.draw.rect(screen, (255, 255, 255), (0, 0, W, H))
    screen.fill(pygame.Color('White'))
    # 画蛇头,蛇身,食物
    rect(head, head_color)
    for snake in snakebody:
        rect(snake, snakebody_color)
    rect(food, food_color)

    # 计算机处理
    pygame.display.flip()
    # 设置帧率
    clock.tick(10)
else:
    # 打印分数
    print(f"你的得分是:{score},你好像有点菜啊QAQ，小老弟！！")