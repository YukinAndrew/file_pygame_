#list_nums = [1, 2, 3, 4, 5]
#print(list_nums[3] == list_nums[-2])
#print(list_nums)


import pygame

pygame.init()
W = 600
H = 400
win = pygame.display.set_mode(W, H)

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]
        y -= 1
    if keys[pygame.K_DOWN]
        y += 1 # y = y + 1