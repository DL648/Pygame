
import pygame
import  random
pygame.init()
#背包格子路径
Inventory = "../image/Inventory.png"
#获取屏幕信息
info = pygame.display.Info()
width = info.current_w
height = info.current_h
#创建窗口
size=(width,height)
screen=pygame.display.set_mode(size)
#显示图片
image =pygame.image.load(Inventory)
image_rect=image.get_rect()
image_rect.center=(size[0]/2,size[1]/2)
#设置帧率
clock=pygame.time.Clock()
fps = 60

speed = 2

#主循环
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		if event.type == pygame.MOUSEBUTTONDOWN or pygame.MOUSEMOTION:
			pass
	#屏幕更新
	pygame.display.flip()
	screen.blit(image,image_rect)
	color=(0,100,100)
	#screen.fill(color)
	clock.tick(fps)
	