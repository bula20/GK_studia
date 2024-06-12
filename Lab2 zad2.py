import pygame

pygame.init()
# Ustawienia okna gry
windowWidth = 600
windowHeight = 600
window = pygame.display.set_mode((windowHeight, windowHeight))
pygame.display.set_caption("Gra z kołem i kwadratem")
run = True

# Kolory
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Parametry figury
CIRCLE_RADIUS = 150
SQUARE_SIZE = 150


square_surface = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
square_surface.fill(YELLOW)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill(WHITE)
    pygame.draw.circle(window, BLACK, (windowWidth // 2, windowHeight // 2), CIRCLE_RADIUS)
    square_transformed = pygame.transform.rotate(square_surface, 0)
    square_rect = square_transformed.get_rect(center=(windowWidth // 2, windowHeight // 2))

    window.blit(square_transformed, square_rect.topleft)
    pygame.display.flip()
    
pygame.quit()