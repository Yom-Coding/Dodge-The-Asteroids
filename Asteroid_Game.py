import pygame
import random
import time

pygame.init()

WIDTH = 600
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
score = 0

class Asteroids(pygame.sprite.Sprite):

    def __init__(self): 
        super().__init__()
        self.image = pygame.image.load("/Users/yompatel/Desktop/Jet Learn/Pro Game Developer/image/g-removebg-preview.png")
        self.image = pygame.transform.scale(self.image, (20,60))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - 50)
        self.rect.y = 0

    def update(self):
        self.rect.y += 2   

        if self.rect.y > HEIGHT:
            self.rect.y = 0
            self.rect.x = random.randint(0, WIDTH - 50)

        





background = pygame.image.load("/Users/yompatel/Desktop/Jet Learn/Pro Game Developer/image/space.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

rocket = pygame.image.load("/Users/yompatel/Desktop/Jet Learn/Pro Game Developer/image/rocket.jpg")
rocket = pygame.transform.scale(rocket, (70, 70))
clock = pygame.time.Clock()


rocket_x = WIDTH//2
rocket_y = 100
rocket_width = 70
rocket_height = 70


rocket_rect = pygame.Rect(rocket_x, rocket_y, rocket_width, rocket_height)
font = pygame.font.SysFont(None, 36)




start_time = time.time()

asteroid_group = pygame.sprite.Group()
for i in range(5):
    asteroid1 = Asteroids()
    asteroid_group.add(asteroid1)
    

game_over = False




run = True
while run:
    screen.blit(background, (0, 0))

    if not game_over:
        asteroid_group.update()

        mouse_x, mouse_y = pygame.mouse.get_pos()
        rocket_rect.x = mouse_x - rocket_width // 2
        rocket_rect.y = mouse_y - rocket_height // 2

    asteroid_group.draw(screen)
    screen.blit(rocket, (rocket_rect.x, rocket_rect.y))


    if not game_over:
        for asteroid in asteroid_group:
            if rocket_rect.colliderect(asteroid.rect):
                print("GAME OVER")
                game_over = True

            

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
