import pygame
import random
import time

pygame.init()

WIDTH = 600
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge The Asteroid")
max_time = 60
last_spawn_time = 0
start_time = 0
time_passed = 0
class Asteroids(pygame.sprite.Sprite):

    def __init__(self): 
        super().__init__()
        self.image = pygame.image.load("/Users/yompatel/Desktop/Jet Learn/Pro Game Developer/image/g-removebg-preview.png")
        self.image = pygame.transform.scale(self.image, (20,60))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - 50)
        self.rect.y = 0
        self.wave = 0
        self.speed = 1.5   

    def increase_speed(self):
        self.speed = self.speed + 0.25               
    def update(self):
        self.rect.y += self.speed  
 
        if self.rect.y > HEIGHT:
            self.wave = self.wave + 1
            self.rect.y = 0
            self.rect.x = random.randint(0, WIDTH - 50)

        
background = pygame.image.load("/Users/yompatel/Desktop/Jet Learn/Pro Game Developer/image/space.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

rocket = pygame.image.load("/Users/yompatel/Desktop/Jet Learn/Pro Game Developer/image/rocket.jpg")
rocket = pygame.transform.scale(rocket, (70, 70))
clock = pygame.time.Clock()

start_time = time.time()
last_spawn_time = round(start_time)

rocket_x = WIDTH//2
rocket_y = 100
rocket_width = 70
rocket_height = 70


rocket_rect = pygame.Rect(rocket_x, rocket_y, rocket_width, rocket_height)
font = pygame.font.SysFont(None, 36)



asteroid_group = pygame.sprite.Group()

for i in range(5):
    asteroid1 = Asteroids()
    asteroid_group.add(asteroid1)
    

game_over = False

difficulty_up = True

run = True
while run:
    if not game_over:
        screen.blit(background, (0, 0))
        screen.blit(rocket, (rocket_rect.x, rocket_rect.y))

        current_time = time.time()
        time_passed = round(current_time - start_time)
        timer = max_time - time_passed
        time_text = font.render("Timer:" + str(timer), True, (255,255,255))
        screen.blit(time_text, (WIDTH - 120, 20))
        if timer <= 0:
            message = "You Have Won"
            game_over = True

        if round(current_time - last_spawn_time) == 10:
            asteroid2 = Asteroids()
            asteroid_group.add(asteroid2)
            for asteroid in asteroid_group:
                asteroid.increase_speed()
            print(len(asteroid_group))
            last_spawn_time = current_time

        asteroid_group.draw(screen)
        asteroid_group.update()

        mouse_x, mouse_y = pygame.mouse.get_pos()
        rocket_rect.x = mouse_x - rocket_width // 2
        rocket_rect.y = mouse_y - rocket_height // 2

        for asteroid in asteroid_group:
            if rocket_rect.colliderect(asteroid.rect):
                message = "GAME OVER"
                game_over = True


    else:
        game_over_text = font.render(message, True, (255,255,255))
        screen.blit(game_over_text, (WIDTH/2 - game_over_text.get_width()/2, HEIGHT/2))
        
            

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
