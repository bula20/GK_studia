import pygame
import math

pygame.init()
#definiowanie okna gry
windowSize = (600, 600)
window = pygame.display.set_mode(windowSize)

#kolory
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

#wyswietlanie okna gry
background_color = WHITE
polygon_outline_color = BLACK
polygon_fill_color = YELLOW

#tworzenie wielokata
radius = 150
num_points = 3
angle = 2* math.pi / num_points
position = (windowSize[0] // 2, windowSize[1] // 2)

rotation_angle = 0
scale_factor = 1
vertical_stretch_factor = 1

pygame.display.set_caption("Moja_gra")
run = True

#petla glowna
while run :
    #obsluga zdarzen
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            position = (windowSize[0] // 2, windowSize[1] // 2)
            
            if event.key == pygame.K_1:
                rotation_angle = 0
                scale_factor = 1
                vertical_stretch_factor = 1

            elif event.key == pygame.K_2:
                rotation_angle = math.radians(45)
                scale_factor = 1.5
                vertical_stretch_factor = 1

            elif event.key == pygame.K_3:
                rotation_angle = math.radians(180)
                scale_factor = 1
                vertical_stretch_factor = 1.1
                
            elif event.key == pygame.K_4:
                rotation_angle = math.radians(25)
                scale_factor = 1
                vertical_stretch_factor = 0.5

            elif event.key == pygame.K_5:
                position = (windowSize[0] // 2, windowSize[1] - 540)
                rotation_angle = 0
                scale_factor = 1
                vertical_stretch_factor = 0.3

            elif event.key == pygame.K_6:
                rotation_angle = math.radians(25) + math.radians(90)
                scale_factor = 1
                vertical_stretch_factor = 0.5

            elif event.key == pygame.K_7:
                rotation_angle = math.radians(180)
                scale_factor = 1
                vertical_stretch_factor = 1.1

            elif event.key == pygame.K_8:
                position = (windowSize[0] // 2 - 140, windowSize[1] - 307)
                rotation_angle = math.radians(135)
                scale_factor = 0.5
                vertical_stretch_factor = 0.5

            elif event.key == pygame.K_9:
                position = (windowSize[0] // 2 + 120, windowSize[1] // 2)
                rotation_angle = math.radians(115) + math.radians(21) + math.radians(180)
                scale_factor = 0.7
                vertical_stretch_factor = 2
                
        window.fill(background_color)
        points = []
        for i in range(num_points):
            x = position[0] + radius * scale_factor * math.cos(i * angle + rotation_angle)
            y = position[1] + (radius * scale_factor * math.sin(i * angle + rotation_angle)) * vertical_stretch_factor
            points.append((x, y))
            
        pygame.draw.polygon(window, polygon_fill_color, points)
        pygame.draw.polygon(window, polygon_outline_color, points, 1)
        pygame.display.flip()

pygame.quit()
