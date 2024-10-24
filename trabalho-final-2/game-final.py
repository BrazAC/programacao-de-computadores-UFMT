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
        self.rect.width = 50
        self.rect.height = 40
        self.rect.center = (1920/2, 600)
        self.speed = 10
        self.ship = pygame.image.load("./templates/SpaceShips/Ship_3.png")
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

        #Constraint player position inside the screen
        gameResolution = (1920, 1080)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > gameResolution[0]:
            self.rect.right = 1920
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > gameResolution[1]:
            self.rect.bottom = gameResolution[1]

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surface = pygame.Surface((32, 32))
        self.surface.fill((255, 255, 255))
        #Creating Enemy in random x position
        self.rect = self.surface.get_rect(center=(random.randint(50, 1870), -100))
        #Setting enemy speed
        self.speed = random.randint (5, 12)
        self.speedx = random.randint (-2, 2)
        #Loading enemy image
        image = pygame.image.load("./templates/asteroid.png")
        #Setting random size for enemy
        size = random.randint(32, 200)
        self.image = pygame.transform.scale(image, (size, size))
        if size > 100:
            self.rect.width = size - 45
            self.rect.height = size -35
        else:
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

class Projectile(pygame.sprite.Sprite):
    def __init__(self):
        super(Projectile, self).__init__()
        #Creating player
        self.surface = pygame.Surface((5, 10))
        self.surface.fill((255, 255, 255))
        #Setting the starter position
        self.rect = self.surface.get_rect()

        self.speed = -25

    def update(self):
        self.rect.move_ip(0, self.speed)

        if self.rect.top < 0:
            self.kill()

def gameScreen(screen):
    #Create the clock
    clock = pygame.time.Clock()

    #Loading sounds
    shootSound = pygame.mixer.Sound("./templates/sounds/shootSound-01.mp3")

    pygame.mixer.music.load("./templates/sounds/megaman-2-gamemusic.mp3")
    pygame.mixer.music.set_volume(0.7)

    #Play the sound (-1 = loop)
    pygame.mixer.music.play(-1)

    #Creating the sprite Player
    player = Player()

    #Creating Background
    background = pygame.image.load("./templates/background0.jpg") 
    i = 0

    #Creating the sprites groups
    enemies_sprites = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    projectiles_sprites = pygame.sprite.Group()

    #Creating event to enemy creation
    Addenemy = pygame.USEREVENT + 1
    pygame.time.set_timer(Addenemy, 500)

    #Creating Score
    pygame.font.init()
    scoreValue = 0
    font = pygame.font.Font(None, 64)
    score = font.render(str(scoreValue), True, (255, 255, 255))
    
    scoreValueAsteroid = 0
    font1 = pygame.font.Font(None, 64)
    scoreAsteroid = font1.render(str(scoreValueAsteroid), True, (255, 255, 255))

    #Time Counter
    counter = 0

    #Difficult controler
    controler = 0
    secondsCounter = 0
    asteroidSpawn = 500
    backgroundSpeed = 3

    #GAME LOOP
    running = True
    while running:
        #Configure clock
        clock.tick(60)

        #Updating score based on time
        counter += 1

        #Seconds counter - game is running at 60fps (or 60 while loops per second)
        if counter > 60: 
            counter = 0
            scoreValue += 1
            secondsCounter += 1
        #For each 15 seconds rises game difficult
        if secondsCounter >= 15:
            controler += 5
            secondsCounter = 0
            asteroidSpawn -= 50
            backgroundSpeed += 3
            pygame.time.set_timer(Addenemy, asteroidSpawn)

        #Checking events
        for event in pygame.event.get():
            #If the screen was closed
            if event.type == pygame.QUIT: 
                return True
            elif event.type == Addenemy:
                enemy = Enemy()
                enemy.speed += controler
                enemies_sprites.add(enemy)
                all_sprites.add(enemy)   

            elif event.type == pygame.KEYDOWN:
                #Create a shoot projectile when j key is pressed
                if event.key == pygame.K_j:
                    projectile = Projectile()
                    newCenterx, newCentery = player.rect.center
                    projectile.rect.center = (newCenterx + 8, newCentery )
                    projectiles_sprites.add(projectile)
                    #Play the sound
                    shootSound.play()

        #Update player position
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        #Update enemy position
        for enemy in enemies_sprites:
            enemy.update()
        #Update projectiles position
        for projectile in projectiles_sprites:
            projectile.update()

        #Design animated background
        screen.blit(background, (0,i))
        screen.blit(background, (0,i - 1080))
        i += backgroundSpeed
        if i >= 1080:
            i = 0
        #Design player / enemies
        for sprite in all_sprites:
            screen.blit(sprite.image, sprite.rect)
        #Design projectiles
        for projectile in projectiles_sprites:
            screen.blit(projectile.surface, projectile.rect)

        #Desing score
        score = font.render(f"TIME: {scoreValue}", True, (255, 255, 255))
        screen.blit(score, (1920 - 250, 50))

        scoreAsteroid = font1.render(f"SCORE: {scoreValueAsteroid}", True, (255, 255, 255))
        screen.blit(scoreAsteroid, (0 + 100, 50))
        
        #If enemy hits player
        if pygame.sprite.spritecollideany(player, enemies_sprites):
            player.kill()
            #Stop playing the music
            pygame.mixer.music.stop()
            running = gameOverScreen(screen, scoreValue, scoreValueAsteroid)
            scoreValue = 0
            #Analysing the gameOverScreen return to decide an action
            if running:
                #Get back to menu screen
                return False
            else:
                #Close the game
                return True
            
        #If a projectile hit a enemy
        collideds = pygame.sprite.groupcollide(enemies_sprites, projectiles_sprites, True, True)
        if collideds:
            scoreValueAsteroid += 1
        
        #Update the game projection
        pygame.display.flip()

def gameOverScreen(screen, scoreValue, scoreAsteroidValue):
    #Creating Score
    font = pygame.font.Font(None, 64)
    score = font.render(str(scoreValue), True, (255, 255, 255))

    font1 = pygame.font.Font(None, 64)
    scoreAsteroid = font1.render(str(scoreAsteroidValue), True, (255, 255, 255))

    font2 = pygame.font.Font(None, 124)
    gameOverMessage = font2.render("YOU DIED", True, (255, 0, 0))

    #Load the game over music
    pygame.mixer.music.load("./templates/sounds/ninjagaiden-gameover.mp3")
    pygame.mixer.music.set_volume(0.7)
    #Play the sound (-1 = loop)
    pygame.mixer.music.play(0, start=1)

    running = True
    while running:
        background = pygame.image.load("./templates/background0.jpg")
        
        #Desing background
        screen.blit(background, (0, 0))

        #Designing score
        score = font.render(f"TIME SURVIVED: {scoreValue}", True, (255, 255, 255))
        screen.blit(score, ((1920 // 2) - 170, (1080 // 2) - 35))

        scoreAsteroid = font1.render(f"FINAL SCORE: {scoreAsteroidValue}", True, (255, 255, 255))
        screen.blit(scoreAsteroid, ((1920 // 2) - 150, (1080 // 2) - 95))

        gameOverMessage = font2.render(f"YOU DIED", True, (255, 0, 0))
        screen.blit(gameOverMessage, ((1920 // 2) - 180, (1080 // 2) - 195))

        pygame.display.flip()
        
        #Checking events
        for event in pygame.event.get():
            #If the screen was closed
            if event.type == pygame.QUIT: 
                return False
            elif event.type == pygame.KEYDOWN:
                #If i was pressed, return to menu
                if event.key == pygame.K_RETURN:
                    #Stop playing the music
                    pygame.mixer.music.stop()
                    #Return to menu
                    return True
                     
def menuScreen():
    #Initialize pygame
    pygame.init()

    #Initialize audio mixer
    pygame.mixer.init()

    #Create the screen
    resolution = (1920, 1080)     
    screen = pygame.display.set_mode(resolution, pygame.FULLSCREEN)
    #Setting display name / icon
    pygame.display.set_caption("A New Hope")
    displayIcon = pygame.image.load("./templates/SpaceShips/Ship_3.png")
    pygame.display.set_icon(displayIcon)

    #Loading sounds
    pygame.mixer.music.load("./templates/sounds/megaman-2-theme.mp3")
    pygame.mixer.music.set_volume(0.7)
    #Loading action sound
    actionSound = pygame.mixer.Sound("./templates/sounds/undertale-sound-savepoint.mp3")

    #Play the sound (-1 = loop)
    pygame.mixer.music.play(-1)

    #Setup title
    font = pygame.font.Font(None, 104)
    title = font.render("A NEW HOPE", True, (255, 255, 255))
    
    #Setup blink subtitle
    BLINK_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(BLINK_EVENT, 500 )
    font1 = pygame.font.Font(None, 44)
    subTitle = font1.render("Press ENTER to start", True, (255, 255, 255))
    showText = True

    #Setup background
    background = pygame.Surface((1920, 1080))
    background = pygame.image.load("./templates/background0.jpg")    
    
    running = True
    while running:
        #Checking events
        for event in pygame.event.get():
            #If the screen was closed
            if event.type == pygame.QUIT: 
                running = False
            elif event.type == pygame.KEYDOWN:
                #I enter was pressed, begin the game
                if event.key == pygame.K_RETURN:
                    #Play a little sound effect
                    actionSound.play()
                    #Stop playing the music
                    pygame.mixer.music.stop()
                    #Begins the game
                    xPressed = gameScreen(screen)
                    if xPressed:    #If the game was closed inside gameScreen, close the menu
                        running = False
                    else:           #In any other case, begins playing the menu music again
                        #Load the correct music
                        pygame.mixer.music.load("./templates/sounds/megaman-2-theme.mp3")
                        pygame.mixer.music.set_volume(0.7)
                        #Play the sound (-1 = loop)
                        pygame.mixer.music.play(-1)
            elif event.type == BLINK_EVENT:
                #Alternating showText status
                showText = not showText

        #Logic to blink the subtitle
        if showText:#If true, show background/title and subTitle
            screen.blit(background, (0, 0))
            screen.blit(title, ((1920 // 2) - 225, (1080 // 2) - 100))
            screen.blit(subTitle, ((1920 // 2) - 152, (1080 // 2) - 0))
        else:       #If false, show only the background/title
            screen.blit(background, (0, 0))
            screen.blit(title, ((1920 // 2) - 225, (1080 // 2) - 100))

        #Designing menu title
        pygame.display.flip()

def main():
    menuScreen()
    
if __name__ == "__main__":
    main()