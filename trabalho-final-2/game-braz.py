import pygame
import random

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        #Creating player
        self.surface = pygame.Surface((64, 64))
        self.surface.fill((255, 0, 0))
        #Configuring player rect start position
        self.rect = self.surface.get_rect()
        self.rect.center = (1920 // 2, 1080 // 2)
        #Loading player sprite image
        self.image = pygame.image.load("./templates/SpaceShips/Ship_1_big.png")
        self.speed = 5  

    #Update player position
    def update(self, pressed_key):
        if pressed_key[pygame.K_w]:
            self.rect.move_ip(0, -1 * self.speed)
        if pressed_key[pygame.K_s]:
            self.rect.move_ip(0, self.speed)
        if pressed_key[pygame.K_a]:
            self.rect.move_ip(-1 * self.speed, 0)
        if pressed_key[pygame.K_d]:
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
            self.rect.x = gameResolution[1]
        
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        #Creating enemy
        self.surface = pygame.Surface((32, 32))
        self.surface.fill((255, 255, 0))
        #Setting the sprite rect to a random x position
        self.rect = self.surface.get_rect(center=(random.randint(0, 1920), 0))
        self.speed = random.randint(1, 10)
        #Load a sprite image
        image = pygame.image.load("./templates/asteroid.png")

        #Generating random size enemies
        newSize = random.randint(32, 101)
        self.image = pygame.transform.scale(image, (newSize, newSize)) #Original: 50,50 fo a 32,32 surface
        self.rect.width = newSize - 20
        self.rect.height = newSize - 20

    def update(self):
        #Moves the enemy down
        self.rect.move_ip((0, self.speed))
        #If the enemy goes away from window, kill himself
        if self.rect.y > 1080:
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

def screenGameOver(status, screen):
    #If the player is dead, show the screen
    if not status:
        #Show game over screen
        screenGameOver = pygame.Surface(screen.get_size())
        screenGameOver.fill((0,0,0))
        screen.blit(screenGameOver, (0,0))
    else:
        return


def main():
    #Initialize pygame
    pygame.init()

    #Create the screen
    resolution = (1920, 1080)     
    screen = pygame.display.set_mode(resolution)

    #Create the clock
    clock = pygame.time.Clock()

    #Creating the group sprites
    enemies_sprites = pygame.sprite.Group()
    projectiles_sprites = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()

    #Creating the sprite Player
    player = Player()
    all_sprites.add(player)
 
    #Creating a event to handle enemy creation
    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 500)
    
    #Creating Background
    background = pygame.image.load("./templates/background0.jpg")
    i = 0

    #Controling the ammount of key repeats per second (KEYDOWN event)
    pygame.key.set_repeat(350, 0)

    #Creating the score
    pygame.font.init()
    scoreValue = 0
    font = pygame.font.Font(None, 54)
    score = font.render(str(scoreValue), True, (255, 255, 255))
    
    #Screen's sentinels variables
    isAlive = True

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
            elif event.type == ADDENEMY:
                #Creates a new enemy
                new_enemy = Enemy()
                #Add the enemy to the groups
                enemies_sprites.add(new_enemy)
                all_sprites.add(new_enemy)
            elif event.type == pygame.KEYDOWN:
                #Create a shoot projectile when key is pressed
                if event.key == pygame.K_j:
                    projectile = Projectile()
                    newCenterx, newCentery = player.rect.center
                    projectile.rect.center = (newCenterx, newCentery - (player.rect.height // 2))
                    projectiles_sprites.add(projectile)
                elif event.key == pygame.K_r:
                    isAlive = True

        
        #Get the list of pressed keys
        pressed_keys = pygame.key.get_pressed()

        #Update player / enemy / projectile positions
        player.update(pressed_keys)
        for enemy in enemies_sprites:
            enemy.update()
        for projectile in projectiles_sprites:
            projectile.update()

        #Design animated background
        screen.blit(background, (0,i))
        screen.blit(background, (0,i - 1080))
        i += 3
        if i == 1080:
            i = 0

        #Design background / player / enemies / projectiles / score
        for sprite in all_sprites:
            screen.blit(sprite.image, sprite.rect)
        for projectile in projectiles_sprites:
            screen.blit(projectile.surface, projectile.rect)

        score = font.render(str(scoreValue), True, (255, 255, 255))
        screen.blit(score, (1920 - 75, 50))

        #Setting the colision detection
        #If the player hit an enemy
        if pygame.sprite.spritecollideany(player, enemies_sprites):
            player.kill()
            scoreValue = 0
            isAlive = False


        #If a projectile hit a enemy
        for enemy in enemies_sprites:
            if pygame.sprite.spritecollideany(enemy, projectiles_sprites):
                enemy.kill()
                scoreValue += 1

        #Show (or not) the game over screen
        screenGameOver(isAlive, screen)

        #Update the game projection
        pygame.display.flip()


if __name__ == "__main__":
    main()