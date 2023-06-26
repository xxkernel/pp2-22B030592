import pygame

pygame.init()
W = 400
H = 300
sc = pygame.display.set_mode((W,H))
pygame.display.set_caption("Music")
spange_bob = pygame.image.load('image/spange_bob.webp')
spirited_away = pygame.image.load('image/spirited_away.webp')
mono = pygame.image.load('image/mono.jpg')

SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)

music = ['monogatari.mp3', 'Spange_bob.mp3', 'spirited_away.mp3']
for i in range(len(music)):
    k = i
    pygame.mixer.music.load(music[k])
    pygame.mixer.music.play(0)

def images():
    if k==0:
        sc.blit(mono,(0,0))
    elif k==1:
        sc.blit(spange_bob, (0,0))
    elif k==2:
        sc.blit(spirited_away,(0,0))

run = True
while run:
    images()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == SONG_END:
            print('The song ended!')
            k+=1
            if 0<=k and k<=2:
                pygame.mixer.music.load(music[k])
                pygame.mixer.music.play(0)
            elif k>2:
                k = 0
                pygame.mixer.music.load(music[k])
                pygame.mixer.music.play(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN or event.key == pygame.K_LEFT:
                k -=1
                if 0<=k and k<=2:
                    pygame.mixer.music.load(music[k])
                    pygame.mixer.music.play(0)
                elif k<0:
                    k = 2
                    pygame.mixer.music.load(music[k])
                    pygame.mixer.music.play(0)
            if event.key == pygame.K_UP or event.key == pygame.K_RIGHT:
                k+=1
                if 0<=k and k<=2:
                    pygame.mixer.music.load(music[k])
                    pygame.mixer.music.play(0)
                elif k>2:
                    k = 0
                    pygame.mixer.music.load(music[k])
                    pygame.mixer.music.play(0)               
            if event.key == pygame.K_SPACE:
                pygame.mixer.music.pause()
            if event.key == pygame.K_RCTRL:
                pygame.mixer.music.unpause()

    pygame.display.update()