import pygame
x = pygame.init()

#Creating Game Window
gameWindow = pygame.display.set_mode((1200, 500))
pygame.display.set_caption("My First Game")

#Game Specific Variable
exit_game = False
game_over = False

#Creating a Game Loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("You have presses Right arrow Key")

pygame.quit()
quit()
