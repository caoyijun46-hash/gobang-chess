import pygame
import time
black_name = '黑方'
white_name = '白方'
pygame.init()
class cell:
    cell_dict = {
        (0, 0):
        {
            'status' : 2,
            'if_pointed' : False
        }
    }
    black_name = '黑方'
    white_name = '白方'
    def __init__(self, black_name, white_name):
        self.black_name = black_name
        self.white_name = white_name
        for i in range(0, 22):
            for j in range(0, 22):
                self.cell_dict[(i, j)] = {
                    'status': 2
                }
    def put(self, x, y, time):
        if(self.cell_dict[(x, y)]['status'] == 2):
            self.cell_dict[(x, y)]['status'] = time % 2
            return True
        else:
            return False
    def win_vertical(self, x, y, time, count):
        if(self.cell_dict[(x, y)]['status'] == time % 2):
            count += 1
            if(count == 5):
                count = 0 
                return True
            return self.win_vertical(x, y + 1, time, count)
        else: 
            count = 0
            return False
    def win_horizontal(self, x, y, time, count):
        if(self.cell_dict[(x, y)]['status'] == time % 2):
            count += 1
            if(count == 5):
                count = 0
                return True
            return self.win_horizontal(x + 1, y, time, count)
        else:
            count = 0
            return False
    def win_left(self, x, y, time, count):
        if(self.cell_dict[(x, y)]['status'] == time % 2):
            count += 1
            if(count == 5):
                count = 0
                return True
            return self.win_left(x - 1, y + 1, time, count)
        else:
            count = 0
            return False
    def win_right(self, x, y, time, count):
        if(self.cell_dict[(x, y)]['status'] == time % 2):
            count += 1
            if(count == 5):
                count = 0
                return True
            return self.win_right(x + 1, y + 1, time, count)
        else:
            count = 0
            return False
    def check(self, time, count):
        for i in range(1, 21):
            for j in range(1, 21):
                if(self.win_vertical(i, j, time, count) or self.win_horizontal(i, j, time, count) or self.win_left(i, j ,time, count) or self.win_right(i, j, time, count)):
                    return True
        return False
screen = pygame.display.set_mode((600 , 700))
pygame.display.set_caption('五子棋')
icon = pygame.image.load("原神.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
running = True
time = 0
x = 0
y = 0
c = cell(black_name , white_name)
black_image = pygame.image.load('黑子.png')
white_image = pygame.image.load('白子.png')
black_image = pygame.transform.scale(black_image , (30, 30))
white_image = pygame.transform.scale(white_image , (30, 30))
while running:
    count = 0
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False
        if(event.type == pygame.MOUSEBUTTONDOWN):
            if(event.button == 1):
                x, y = pygame.mouse.get_pos()
                x = x // 30
                y = y // 30
                if(x>19 or y>19):
                    continue
                if(c.put(x, y, time)):
                    if(c.check(time, count)):
                        pygame.quit()
                    time += 1    
        if(event.type == pygame.MOUSEMOTION):
            pass
    screen.fill((218 , 165 , 32))
    points = [(0, 0), (600, 0), (600, 30), (0, 30), (0, 60), (600, 60), (600, 90), (0, 90), (0, 120), (600, 120), (600, 150), (0, 150), (0, 180), (600, 180), (600, 210), (0, 210), (0, 240), (600, 240), (600, 270), (0, 270), (0, 300), (600, 300), (600, 330), (0, 330), (0, 360), (600, 360), (600, 390), (0, 390), (0, 420), (600, 420), (600, 450), (0, 450), (0, 480), (600, 480), (600, 510), (0, 510), (0, 540), (600, 540), (600, 570), (0, 570), (0, 600), (600, 600), (600, 0), (570, 0), (570, 600), (540, 600), (540, 0), (510, 0), (510, 600), (480, 600), (480, 0), (450, 0), (450, 600), (420, 600), (420, 0), (390, 0), (390, 600), (360, 600), (360, 0), (330, 0), (330, 600), (300, 600), (300, 0), (270, 0), (270, 600), (240, 600), (240, 0), (210, 0), (210, 600), (180, 600), (180, 0), (150, 0), (150, 600), (120, 600), (120, 0), (90, 0), (90, 600), (60, 600), (60, 0), (30, 0), (30, 600), (0, 600)]    
    pygame.draw.lines(screen , (0 , 0 , 0) , True , points , 3)
    for i in range(0 , 21):
        for j in range(0 , 21):
            if(c.cell_dict[(i , j)]['status'] == 0):
                screen.blit(black_image , (i*30 , j*30))
            if(c.cell_dict[(i , j)]['status'] == 1):
                screen.blit(white_image , (i*30 , j*30))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()