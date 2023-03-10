import pygame
import random
x = pygame.init()

#Colors
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
black = (0,0,0)

#Creating Game Window and giving Title
gameWindow = pygame.display.set_mode((1000, 600)) #To create Game Window of given size
pygame.display.set_caption("My First Snake Game") #Giving Title to the Game Window
pygame.display.update() #Update Function updates the default Game Window
clock = pygame.time.Clock()  #Clock Variable to create FPS which will appear snake in moving directions
font = pygame.font.SysFont(None, 30)     #Getting Font for the Score to be seen in Game Window

def text_screen(text, color, x, y):     #Defining Function to generate Font for Score to be displayed in Game Window
    screen_text  = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

def plot_snake(gameWindow,color,snake_list,snake_size):  #Defining Function to Plot Snake as it has to grow after eating food
    for x,y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])  #Creates Initial Snake in Game Window

#Creating a Function of Welcome Screen
def Welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(white)
        text_screen("Welcome to Snakes Game", black, 350,250)
        text_screen("Press Spacebar to Play", black, 350, 300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:  # If you press Enter after the game is over we will reenter in the game
                if event.key == pygame.K_SPACE:
                    gameLoop()

        pygame.display.update()
        clock.tick(60)

#Creating a Game Loop Function for writing whole game logic
def gameLoop():
    #Game Specific Variable
    exit_game = False  #This Variable exits the Game Window if True
    game_over = False  #This Variable choose to end the game if true
    snake_x = 45     #Position of the snake in X Axis
    snake_y = 55     #Position of the snake in Y Axis
    snake_size = 10  #Initial Size of the snake
    food_x = random.randint(0, 1000/2)     #Generate Food Position in X Axis
    food_y = random.randint(0, 600/2)      #Generate Food Position in Y Axis
    score = 0    #Store scores when Snake eats food
    fps = 50         #Declaring Frame Per Second Variable
    velocity_x = 0   #Declaring Velocity Variable which will move the snake in X Axis
    velocity_y = 0   #Declaring Velocity Variable which will move the snake in Y Axis
    init_velocity = 3     #Declaring Variable for Velocity for Levels of the game
    snake_list = []      #Creating Empty List to take X and Y coordinate for Snake
    snake_length = 1      #Defining Initial Length of Snake as 1

    with open("HighScore.txt", "r") as f:
        hscore = f.read()
    
    while not exit_game:  #Main Loop where the game will hold all the logic
        if game_over:       #Logic if Game Over Variable is True
            gameWindow.fill(white)
            text_screen("Game Over!!! Press Enter to continue", red, 350,250)

            with open("HighScore.txt", "w") as f:
                f.write(str(hscore))

            for event in pygame.event.get():  #Loop created after the game is over
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:   #If you press Enter after the game is over we will reenter in the game
                    if event.key == pygame.K_RETURN:
                        Welcome()

        else:
            for event in pygame.event.get():  #Inner loop where the game handle all the events occurred in the Game Window
                #Logic for the snake to move
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_q:   #Generating Cheat Code for our game
                        score += 5

            snake_x = snake_x + velocity_x   #This will move snake in  X axis with that velocity
            snake_y = snake_y + velocity_y   #This will move snake in  Y axis with that velocity

            #Logic to Eat Food and raise score
            if(abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6):
                score += 10
                food_x = random.randint(0, 1000/2)
                food_y = random.randint(0, 600/2)
                snake_length += 4       #Increase Snake's length by 4 everytime it eats Food/

                if score > int(hscore):
                    hscore = score

            gameWindow.fill(white)    #Colors the game Window in White
            text_screen("Score: "+str(score) + "    Hiscore: " +str(hscore), green, 5, 5)      #Finally displaying Score in Game Window
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])  # Creates Food in Game Window randomly anywhere

            #Creating Empty List because the Snake just grows in the game. So we need to cut the Head
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_length:     #Cutting the head once food is eaten by the snake
                del(snake_list[0])

            if head in snake_list[:-1]:   #If Head of the snake touches its body
                game_over = True

            if snake_x < 0 or snake_x > 1000 or snake_y < 0 or snake_y > 600:   #If snake touches all corners of the window
                game_over = True

            plot_snake(gameWindow, black, snake_list, snake_size)    #Usage of Snake Plotting Function with Snake List
        pygame.display.update()     #Updates the display with Snake in it.
        clock.tick(fps)      #Clock ticks and with it, Frames are created so that it appears that snake is moving
    pygame.quit()
    quit()

Welcome()
