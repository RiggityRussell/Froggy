import pygame, sys #importing pygame to run our game, and system commands
from settings import * #importing our settings we create for the game

class Game: #the game class which holds the main information to run the game.
    def __init__(self): #defining the game class

        pygame.init() #initializing pygame
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("Froggy")
        self.clock = pygame.time.Clock()
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()