import pygame

pygame.init()
clock = pygame.time.Clock()
W = 400
H = 300
white = (255,255,255)
sc = pygame.display.set_mode((W,H))
pygame.display.set_caption("Ball")

x_circle = W/2
y_circle = H/2
speed = 20
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and y_circle>=50:
                y_circle-=speed
            elif event.key == pygame.K_DOWN and y_circle<=H-50:
                y_circle+=speed
            elif event.key == pygame.K_RIGHT and x_circle<=W-25:
                x_circle+=speed
            elif event.key == pygame.K_LEFT and x_circle>=25:
                x_circle-=speed
    sc.fill(white)
    pygame.draw.circle(sc,(255,2,255),(x_circle,y_circle), 25)
    pygame.display.update()
    clock.tick(60)