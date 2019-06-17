import pygame
import time
import random
from pygame.locals import *
#独立显卡，是专门的一个显卡，卡里有什么就会在电脑上显示什么
#集成显卡是在内存中分配出一块空间，内存有什么就会显示什么，
# 这当内存不够大的时候就会是显示效果差得很远
class Lufei(object):
    def __init__(self,screen_temp):
        self.x=300
        self.y=730
        self.screen=screen_temp
        self.image=pygame.image.load("./image/ACE.gif")
        self.bullet_list=[]
        # self.dama=[]
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))


        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
    def move_left(self):
        self.x-=5
    def move_right(self):
        self.x+=5
    def move_up(self):
        self.y-= 5
    def move_down(self):
        self.y+= 5
    def fire(self):
        self.bullet_list.append(Bullet(self.screen,self.x,self.y))
    # def dama(self):
    #     self.dama.append(Bigmamo(self.screen,self.x,self.y))



class Bullet(object):
    def __init__(self,screen_temp,x,y):
        self.x=x
        self.y=y
        self.screen=screen_temp
        self.image=pygame.image.load("./image/fire.gif")
    def display(self):
        self.screen.blit(self.image,(self.x+200,self.y-100))
    def move(self):
        self.y-=100
class Bigmamo(object):
    def __init__(self,screen_temp):
        self.x=random.randint(0,1024)
        self.y=0
        self.screen=screen_temp
        self.image=pygame.image.load("./image/bigmom.gif")
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
    def move(self):
        self.y-=5
def key(lufei_temp):
    ########对鼠标和键盘的控制此代码块是不会改变的在任意地方均可使用
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("exit()")
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                print('left')
                lufei_temp.move_left()
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                print('right')
                lufei_temp.move_right()
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                print('up')
                lufei_temp.move_up()
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                print('down')
                lufei_temp.move_down()
            elif event.key == pygame.K_TAB:
                print('space')
                lufei_temp.fire()
    ###########

def main():
    # 创建窗口
    screen = pygame.display.set_mode((800, 900), 0, 32)
    #创建背景图片
    background=pygame.image.load("./image/bg.jpeg")
    #bigmamo=pygame.image.load("./image/dama.jpg")
    lufei = Lufei(screen)
    #lufeiImage=lufei.lufeiimage()
    while True:
        screen.blit(background,(0,0))#（0，0）表示从那里开始贴图
        lufei.display()
        pygame.display.update()  #更新需要显示的内容,当没有此行代码的时候就不能进行显示贴的海贼图
        key(lufei)
        #time.sleep(0.01)#提供延时，这样可以降低cpu的利用率，根据电脑的配置
if __name__=="__main__":
    main()