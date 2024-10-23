import pygame
import random
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        #Creating player
        self.surface = pygame.Surface((60, 60))
        self.surface.fill((255, 0, 0))
        self.rect = self.surface.get_rect()
        self.rect.center = (1920/2, 600)
        self.speed = 8
        self.ship = pygame.image.load("./templates/SpaceShips/Ship_2.png")
        self.image = pygame.transform.scale(self.ship, (70, 70))

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

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surface = pygame.Surface((32, 32))
        self.surface.fill((255, 255, 255))
        #Creating Enemy in random x position
        self.rect = self.surface.get_rect(center=(random.randint(-20, 1920), 0))
        #Setting enemy speed
        self.speed = random.randint (5, 12)
        self.speedx = random.randint (-2, 2)
        #Loading enemy image
        image = pygame.image.load("./templates/asteroid.png")
        #Setting random size for enemy
        size = random.randint(32, 200)
        self.image = pygame.transform.scale(image, (size, size))
        self.rect.width = size - 10
        self.rect.height = size - 10

    def update(self):
        #set enemy movement
        self.rect.move_ip((self.speedx, self.speed))
        #set enemy death if out off the screen
        if self.rect.y > 1080:
            self.kill()
        if self.rect.x > 1920:
            self.kill()

def gameScreen(screen):
    #Create the clock
    clock = pygame.time.Clock()

    #Creating the sprite Player
    player = Player()

    #Creating Background
    background = pygame.image.load("./templates/background0.jpg") 

    #Creating the sprites groups
    enemies_sprites = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    #Creating event to enemy creation
    Addenemy = pygame.USEREVENT + 1
    pygame.time.set_timer(Addenemy, 500)

    #Creating Score
    pygame.font.init()
    scoreValue = 0
    font = pygame.font.Font(None, 64)
    score = font.render(str(scoreValue), True, (255, 255, 255))

    #Time Counter
    counter = 0

    #GAME LOOP
    running = True
    while running:
        #Configure clock
        clock.tick(60)

        #Updating score based on time
        counter += 1
        if counter > 60:
            counter = 0
            scoreValue += 1
        #Checking events
        for event in pygame.event.get():
            #If the screen was closed
            if event.type == pygame.QUIT: 
                return True
            elif event.type == Addenemy:
                enemy = Enemy()
                enemies_sprites.add(enemy)
                all_sprites.add(enemy)

        #Update player position
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        #Update enemy position
        for enemy in enemies_sprites:
            enemy.update()

        #Design background / sprites
        screen.blit(background, (0,0))
        for sprite in all_sprites:
            screen.blit(sprite.image, sprite.rect)

        #Designing score
        score = font.render(f"PONTUAÇÃO: {scoreValue}", True, (255, 255, 255))
        screen.blit(score, (1920 - 450, 50))
        
        #If enemy hits player
        if pygame.sprite.spritecollideany(player, enemies_sprites):
            player.kill()
            running = gameOverScreen(screen, scoreValue)
            scoreValue = 0
            #Analysing the gameOverScreen return to decide an action
            if running:
                #Get back to menu screen
                return False
            else:
                #Close the game
                return True
            
        #Update the game projection
        pygame.display.flip()

def gameOverScreen(screen, scoreValue):
    #Creating Score
    font = pygame.font.Font(None, 64)
    score = font.render(str(scoreValue), True, (255, 255, 255))

    running = True
    while running:
        background = pygame.image.load("./templates/background0.jpg")
        
        #Desing background
        screen.blit(background, (0, 0))

        #Designing score
        score = font.render(f"PONTUAÇÃO FINAL: {scoreValue}", True, (255, 255, 255))
        screen.blit(score, ((1920 // 2) - 250, (1080 // 2) - 100))
        pygame.display.flip()
        
        #Checking events
        for event in pygame.event.get():
            #If the screen was closed
            if event.type == pygame.QUIT: 
                return False
            elif event.type == pygame.KEYDOWN:
                #If i was pressed, return to menu
                if event.key == pygame.K_RETURN:
                    return True
                     
def menuScreen():
    #Initialize pygame
    pygame.init()

    #Create the screen
    resolution = (1920, 1080)     
    screen = pygame.display.set_mode(resolution)

    #Creating Score
    font = pygame.font.Font(None, 104)
    font1 = pygame.font.Font(None, 44)
    title = font.render("A NEW HOPE", True, (255, 255, 255))
    subTitle = font1.render("Press ENTER to start", True, (255, 255, 255))

    background = pygame.Surface((1920, 1080))
    background = pygame.image.load("./templates/background0.jpg")    
    

    running = True
    while running:
        #Designing score
        screen.blit(background, (0, 0))
        screen.blit(title, ((1920 // 2) - 225, (1080 // 2) - 100))
        screen.blit(subTitle, ((1920 // 2) - 152, (1080 // 2) - 0))
        
        pygame.display.flip()

        #Checking events
        for event in pygame.event.get():
            #If the screen was closed
            if event.type == pygame.QUIT: 
                running = False
            elif event.type == pygame.KEYDOWN:
                #If i was pressed, begin the game
                if event.key == pygame.K_RETURN:
                    xPressed = gameScreen(screen)
                    #If the game was closed inside gameScreen, close the menu
                    if xPressed:
                        running = False

        

def main():
    menuScreen()
    


if __name__ == "__main__":
    main()