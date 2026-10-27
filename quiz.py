# Quiz) 하늘에서 떨어지는 똥 피하기 게임을 만드시오

# [게임 조건]
# 1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능
# 2. 똥은 화면 가장 위에서 떨어짐. x 좌표는 매번 랜덤으로 설정
# 3. 캐릭터가똥을 피하면 다음 똥이 다시 떨어짐
# 4. 캐릭터가 똥과 충돌하면 게임 종료
# 5. FPS 는 30으로 고정

# [게임 이미지]
# 1. 배경 : 640 * 480 (세로 가로) - background.png
# 2. 캐릭터 : 70 * 70 - character.png
# 3. 똥 : 70 * 70 - enemy.png

import pygame
import random
#############################################################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init() #초기화

# 화면크기
screen_width = 480 # 가로
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("QUIZ")

# FPS
clock = pygame.time.Clock()
#############################################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
background = pygame.image.load("background.png") # 배경 로드

character = pygame.image.load("character.png") # 캐릭터 로드
character_size = character.get_rect().size # 캐릭터 사이즈 튜플값 받아옴
character_width = character_size[0] # 첫째항 width에 저장
character_height = character_size[1] # 둘째항 height에 저장
character_x_pos = (screen_width - character_width) / 2 # 화면의 가운데 x position 설정
character_y_pos = screen_height - character_height # 화면 맨 아래 y position 설정
character_speed = 0.6 # 캐릭터 스피드 설정
character_to_x = 0 # 키 이벤트 발생시 스피드 초기화를 위한 저장공간

enemy = pygame.image.load("enemy.png") # 적 로드
enemy_size = enemy.get_rect().size # 적 사이즈 튜플값 받아옴
enemy_width = enemy_size[0] # 첫째항 width에 저장
enemy_height = enemy_size[1] # 둘째항 height에 저장
enemy_x_pos = random.randint(1, (screen_width - enemy_width + 1)) # 화면의 width 중 랜덤한 위치에 x position 설정
enemy_y_pos = 0 # 화면 맨 위에 y position 설정
enemy_speed = 0.6 # 적 스피드 설정

running = True
while running:
    dt = clock.tick(30) #fps 30으로 설정

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += character_to_x * dt
    enemy_y_pos += enemy_speed * dt
    
    if enemy_y_pos > screen_height:
        enemy_x_pos = random.randint(1, (screen_width - enemy_width + 1))
        enemy_y_pos = 0
        screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        running = False

    # 5. 화면에 그리기
    
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    pygame.display.update() # 게임화면을 다시 그리기

# 잠시 대기
pygame.time.delay(2000) # 2초 대기 (ms)

# pygame 종료
pygame.quit()
