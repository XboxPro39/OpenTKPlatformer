import pygame
import settings
import player
import backgroundObject


SetttingsObject = settings.Settings()
PlayerObject = player.Player()
ColorObject = settings.Color()

window = pygame.display.set_mode((SetttingsObject.ScreenWidth, SetttingsObject.ScreenHeight))
pygame.display.set_caption("Pygame Game")

backgroundObjects = [backgroundObject.BackgroundObject()]
pygame.init()


joysticks = []
for i in range(0, pygame.joystick.get_count() - 1):
    joysticks.append(pygame.joystick.Joystick())





def MainLoop():
    while SetttingsObject.GameRunning == True and PlayerObject.Alive == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                SetttingsObject.GameRunning = False
                # Added test comment
        PlayerObject.getInput(backgroundObjects)
        for backgroundObj in backgroundObjects:
            window.blit(pygame.image.load('house.jpg'), (backgroundObj.PositionX, backgroundObj.PositionY))
        window.fill(ColorObject.BLACK)
        pygame.draw.rect(window, ColorObject.RED, pygame.Rect((PlayerObject.PositionX, PlayerObject.PositionY), (PlayerObject.Width, PlayerObject.Height)))
        

        pygame.display.flip()




MainLoop()

