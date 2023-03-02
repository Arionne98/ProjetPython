import pygame

class Game:

    def __init__(self, title, resolution):
        self.title = title
        self.resolution = resolution 

    def charger_module(self):
        pygame.init()

    def display(self):
        pygame.display.set_caption(self.title)
        display = pygame.display.set_mode(self.resolution)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

    def decharger_module(self):
      pygame.quit()

minecraft = Game("Minecraft 1.7.10", (600, 500))

minecraft.charger_module()
minecraft.display()
minecraft.run()
minecraft.decharger_module()

