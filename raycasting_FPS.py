import pygame
import sys
import time
import os
import math

pygame.display.init()
pygame.font.init()
clock = pygame.time.Clock()
FPS = 60

width = 1200
height = 840
running = True
screen = pygame.display.set_mode((width, height))

tile_size = 60
game_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
def draw_map():
    for row_index, row_value in enumerate(game_map):
        for col_index , tile in enumerate(row_value):
            y = row_index * tile_size
            x = col_index * tile_size
            if tile == 1:
                pygame.draw.rect(screen, (0, 0, 0), (x, y, tile_size, tile_size))

class Player:
    def __init__(self, x, y, speed, rad):
        self.x = x
        self.y = y
        self.speed = speed
        self.radius = rad
    def move(self, keys):    # 키보드 입력(누르기)

        if keys[pygame.K_a]:
            next_x = self.x - self.speed
            check_x = next_x - self.radius
            if game_map[self.y // tile_size][check_x // tile_size] != 1:
                self.x = next_x
                
        if keys[pygame.K_d]:
            next_x = self.x + self.speed
            check_x = next_x + self.radius
            if game_map[self.y // tile_size][check_x // tile_size] != 1:
                self.x = next_x
                
        if keys[pygame.K_s]:
            next_y = self.y + self.speed
            check_y = next_y + self.radius
            if game_map[check_y // tile_size][self.x // tile_size] != 1:
                self.y = next_y

        if keys[pygame.K_w]:
            next_y = self.y - self.speed
            check_y = next_y - self.radius
            if game_map[check_y // tile_size][self.x // tile_size] != 1:
                self.y = next_y

        # 화면 밖으로 못빠져나가게 제한함.
        self.x = max(self.radius, min(self.x, width - self.radius))
        self.y = max(self.radius, min(self.y, height - self.radius))
        
    def draw_cha(self):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), 10)

def sight():
    now_pos = (player.x, player.y) # 현재 플레이어 위치
    mouse_pos = pygame.mouse.get_pos() # 마우스 위치
    dx = mouse_pos[0] - player.x
    dy = mouse_pos[1] - player.y
    lim_line = math.hypot(dx, dy)

    if lim_line > 0:
        rate = 60 / lim_line
        rate_dx = dx*rate
        rate_dy = dy*rate      
        lim_mouse_pos = (player.x + rate_dx, player.y + rate_dy)
        pygame.draw.line(screen, (0, 0, 255), now_pos, lim_mouse_pos, width=1)

        

player = Player(300, 200, 2, 10)

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False

    screen.fill((255, 255, 255))
    # 키보드 입력(누르기)
    player.move(keys = pygame.key.get_pressed())
    # 맵 그리기
    draw_map()
    # 방향 표시
    sight()

    # 플레이어 그리기(임의)
    player.draw_cha()
    pygame.display.flip()

pygame.quit()
sys.exit()
