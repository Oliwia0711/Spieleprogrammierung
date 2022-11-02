import os
import random
import pygame

class Settings():
    SCREENRECT = pygame.rect.Rect(0, 0, 1000, 600)
    FPS = 60
    PATHFILE = os.path.dirname(os.path.abspath(__file__))
    PATHIMG = os.path.join(PATHFILE, "images")

    @staticmethod
    def get_imagepath(filename):
        return os.path.join(Settings.PATHIMG, filename)

class Mario(pygame.sprite.Sprite):
    def __init__(self, filename, colorkey = None) -> None:
        super().__init__()
        if colorkey is None:
          self.image = pygame.image.load(Settings.get_imagepath(filename)).convert_alpha()
        else:
            self.image = pygame.image.load(Settings.get_imagepath(filename)).convert()
            self.image.set_colorkey(colorkey)

        self.image = pygame.transform.scale(self.image, (100, 100))
        self.image = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image) 

class RectObstacle(pygame.sprite.Sprite):
    def __init__(self,  filename, colorkey = None) -> None:
        super().__init__()
        if colorkey is None:
          self.image = pygame.image.load(Settings.get_imagepath(filename)).convert_alpha()
        else:
            self.image = pygame.image.load(Settings.get_imagepath(filename)).convert()
            self.image.set_colorkey(colorkey)

        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()

class CircleObstacle(pygame.sprite.Sprite):
    def __init__(self,  filename, colorkey = None) -> None:
        super().__init__()
        if colorkey is None:
          self.image = pygame.image.load(Settings.get_imagepath(filename)).convert_alpha()
        else:
            self.image = pygame.image.load(Settings.get_imagepath(filename)).convert()
            self.image.set_colorkey(colorkey)

        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.radius = self.rect.width // 2

class MaskObstacle(pygame.sprite.Sprite):
    def __init__(self,  filename, colorkey = None) -> None:
        super().__init__()
        if colorkey is None:
          self.image = pygame.image.load(Settings.get_imagepath(filename)).convert_alpha()
        else:
            self.image = pygame.image.load(Settings.get_imagepath(filename)).convert()
            self.image.set_colorkey(colorkey)

        self.image = pygame.transform.scale(self.image, (100, 100))
        self.image = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
         
class Game():
    def __init__(self) -> None:
        os.environ['SDL_VIDEO_WINDOW_POS'] = "10, 50"
        pygame.init()
        self.screen = pygame.display.set_mode(Settings.SCREENRECT.size)
        self.clock = pygame.time.Clock()

        self.background = pygame.image.load(Settings.get_imagepath("background.png")).convert()
        self.background = pygame.transform.scale(self.background, Settings.SCREENRECT.size)

        self.all_obstacles = pygame.sprite.Group()
        self.all_marios = pygame.sprite.Group()

        obstacle = RectObstacle("whomp.png")
        obstacle.rect.left = 10
        obstacle.rect. bottom = Settings.SCREENRECT.height
        self.all_obstacles.add(obstacle)

        obstacle = RectObstacle("whomp1.png")
        obstacle.rect.right = Settings.SCREENRECT.width - 20
        obstacle.rect.bottom = Settings.SCREENRECT.height - 20
        self.all_obstacles.add(obstacle)

        obstacle = CircleObstacle("chainchomp.png")
        self.all_obstacles.add(obstacle)

        obstacle = CircleObstacle("chainchomp1.png")
        self.all_obstacles.add(obstacle)

        obstacle = MaskObstacle("bowser.png")
        self.all_obstacles.add(obstacle)

        obstacle = MaskObstacle("bowser1.png")
        self.all_obstacles.add(obstacle)

        self.counter = 0
        self.running = True

    def run(self):
        while self.running:
            self.clock.tick(Settings.FPS)
            self.watch_for_events()
            self.update()
            self.draw()
        pygame.quit()

    def watch_for_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False


    def update(self):
        self.counter += 1
        if self.counter >= 30:
             mario = Mario("mario.png")
             mario = pygame.transform.scale()+10
             self.all_marios.add(mario)
             self.counter = 0

        self.all_marios.update()

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.all_obstacles.draw(self.screen)
        self.all_marios.draw(self.screen)
        pygame.display.flip()

def main(): 
    game = Game()
    game.run()
    
if __name__ == "__main__":
    main()