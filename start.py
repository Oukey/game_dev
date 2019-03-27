import pygame

pygame.init()
# дисплей
win = pygame.display.set_mode((500, 500))

# игрок/объект
pygame.display.set_caption('Cubes Game')

# анимация
# walkRight = [pygame.image.load('right_1.png'), pygame.image.load('right_2.png'),
#              pygame.image.load('right_3.png'), pygame.image.load('right_4.png'),
#              pygame.image.load('right_5.png'), pygame.image.load('right_6.png')]
#
# walkLeft = [pygame.image.load('left_1.png'), pygame.image.load('left_2.png'),
#             pygame.image.load('left_3.png'), pygame.image.load('left_4.png'),
#             pygame.image.load('left_5.png'), pygame.image.load('left_6.png')]
#
# bg = pygame.image.load('bg.lpg')
# playStand = pygame.image.load('idle.png')

# параметры объекта
x = 50
y = 425
widht = 60
height = 71
speed = 5

# действия объекта
isJump = False
jumpCount = 10

left = False
right = False
animCount = 0

run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # усправление объектом
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
    if keys[pygame.K_RIGHT] and x < 500 - widht - 5:
        x += speed
    if not (isJump):
        # if keys[pygame.K_UP] and y > 5:
        #     y -= speed
        # if keys[pygame.K_DOWN] and y < 500 - height - 15:
        #     y += speed
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    # создание объекта
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (0, 0, 255), (x, y, widht, height))
    pygame.display.update()

pygame.quit()
