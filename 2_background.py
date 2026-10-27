import pygame

pygame.init() #초기화

# 화면크기
screen_width = 480 #가로
screen_height = 640 #세로
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado game") #게임이름/

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/mkh99/Documents/pygame project/background.png")

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 이벤트 리스너 역할
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False

    # screen.fill((0, 0, 255)) #화면 RGB값으로 채우기

    screen.blit(background, (0, 0)) # 배경 그리기

    pygame.display.update() # 게임화면을 다시 그리기


# pygame 종료
pygame.quit()