import pygame
import os
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Name Of The game")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 64)
#main_dir = os.path.split(os.path.abspath(__file__))[0]
#data_dir = os.path.join(main_dir, "data")

background_image = pygame.image.load("./spacebackground.png")
background_image = pygame.transform.scale(background_image,(1280, 720))
lose = False
win = False
over_image = pygame.image.load("./game over.png")
over_image = pygame.transform.scale(background_image,(1280, 720))
def main():
    # pygame setup    
    
    p2 = PlayerMouse("./target.png")
    a = asteriod("./asteroid.png", 1280 / 4, 720)
    a2 = asteriod("./asteroid.png", 1280 / 2, 720)
    a3 = asteriod("./asteroid.png", 1280 / 2, 0)
    a4 = asteriod("./asteroid.png", 1280 / 4, 0)
    a5 = asteriod("./asteroid.png", 1270 / 4/3, 720)
    a6 = asteriod("./asteroid.png", 1270 / 4/3, 0)
    a7 = asteriod("./asteroid.png", 960, 0)
    a8= asteriod("./asteroid.png", 960, 0)
    allsprites = pygame.sprite.RenderPlain((p1,p2,a,a2,a3,a4,a5,a6,a7,a8))
    running = True
    
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")
        screen.blit(background_image,(0,0))
    #################################################################
        # RENDER YOUR GAME HERE
        allsprites.update()
        allsprites.draw(screen)
        if (len(allsprites.sprites()) == 2 and allsprites.has(p1)):
            writeToScreen("You Win!", 1280 / 2, 720 / 2)
            

            

    ##############################################################
        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()


class PlayerMouse(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 15
        self.image, self.rect = load_image(image,scale=.05)#adjust scale to get character sizing right
        self.target_width, self.target_height =self.image.get_size()
        self.rect.topleft = pygame.Vector2(screen.get_width() / 2, screen.get_height())#adjust arugments for disired starting position
    def update(self):
        cursor_x, cursor_y = pygame.mouse.get_pos()
        bg_x = cursor_x - (self.target_width // 2)
        bg_y = cursor_y - (self.target_height // 2)
        self.rect.topleft = (bg_x,bg_y)






class PlayerWasd(pygame.sprite.Sprite):
    
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        
        self.speed = 15
        self.image, self.rect = load_image(image,scale=.25)#adjust scale to get character sizing right
        self.target_width, self.target_height =self.image.get_size()
        self.rect.topleft = pygame.Vector2((screen.get_width() / 2) -  self.target_width // 2, (screen.get_height() / 2) -  self.target_height // 2)#adjust arugments for disired starting position
    def update(self):
        keys = pygame.key.get_pressed()
        (x,y) = self.rect.topleft
        if keys[pygame.K_w]:
            y -= self.speed
        if keys[pygame.K_s]:
          y += self.speed
        if keys[pygame.K_a]:
             x -= self.speed
        if keys[pygame.K_d]:
             x += self.speed
        self.rect.topleft = (x,y)

class asteriod(pygame.sprite.Sprite):
    
    def __init__(self,image,startingX, startingY):
        pygame.sprite.Sprite.__init__(self)
        self.direction = -1
        self.speed = 10
        self.image, self.rect = load_image(image,scale=.08)#adjust scale to get character sizing right
        self.rect.topleft = pygame.Vector2(startingX, startingY)#adjust arugments for disired starting position
    def update(self):
        
        (x,y) = self.rect.topleft
        if y < 0 or y > screen.get_height():
            self.direction = -self.direction
        y = y + (5 * self.direction)
        self.rect.topleft = (x,y)
        if pygame.mouse.get_pressed()[0]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if (x < mouse_x and mouse_x < x + self.rect.width and y < mouse_y and mouse_y < y + self.rect.height):
                print("Clicked")
                self.kill()
        if (self.rect.colliderect(p1.rect)):
            p1.kill()
            #writeToScreen("You Lose!", 1280 / 2, 720 / 2)
            global over_image
            screen.blit(over_image,(1280, 720))
            





    
         


def writeToScreen(msg, x, y):
        text = font.render(msg, True, (10, 10, 10))
        textpos = text.get_rect(centerx=x, y=y)
        screen.blit(text, textpos)


def load_image(name, colorkey=None, scale=1):
    #fullname = os.path.join(data_dir, name)
    image = pygame.image.load(name)
    size = image.get_size()
    size = (size[0] * scale, size[1] * scale)
    image = pygame.transform.scale(image, size)

    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
    return image, image.get_rect()














p1 = PlayerWasd("./shape.png")
main()