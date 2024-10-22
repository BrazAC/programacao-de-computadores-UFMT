import pygame
import random
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        #Creating player
        self.surface = pygame.Surface((50, 50))
        self.surface.fill((255, 0, 0))
        self.rect = self.surface.get_rect()
        self.speed = 5  

    #Update player position
    def update(self, pressed_key):
        if pressed_key[K_w]:
            self.rect.move_ip(0, -1 * self.speed)
        if pressed_key[K_s]:
            self.rect.move_ip(0, self.speed)
        if pressed_key[K_a]:
            self.rect.move_ip(-1 * self.speed, 0)
        if pressed_key[K_d]:
            self.rect.move_ip(self.speed, 0)


def main():
    #Initialize pygame
    pygame.init()

    #Create the screen
    resolution = (1920, 1080)     
    screen = pygame.display.set_mode(resolution)

    #Create the clock
    clock = pygame.time.Clock()

    #Creating the sprite Player
    player = Player()

    #Creating Background
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0)) #Cor preta

    #Creating the sprites groups
    #all_sprites = pygame.sprite.Group()
    #all_sprites.add(player)

    #GAME LOOP
    running = True
    
    while running:
        #Configure clock
        clock.tick(60)

        #Checking events
        for event in pygame.event.get():
            #If the screen was closed
            if event.type == pygame.QUIT: 
                running = False

        #Update player position
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        
        #Design background / player
        screen.blit(background, (0,0))
        screen.blit(player.surface, player.rect)


        #Update the game projection
        pygame.display.flip()


if __name__ == "__main__":
    main()