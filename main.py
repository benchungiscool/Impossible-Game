import pygame
import pygame.freetype
import random
import time
import os

# -- Colour Variables --
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 240, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
NIGHT = BLACK

# -- Calling the things necessary to get a window up and running --
pygame.init()
size = (800, 800)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
font = pygame.freetype.SysFont('Comic Sans MS', 30)
smallfont = pygame.freetype.SysFont('Comic Sans MS', 25)
title = pygame.display.set_caption("Comic Sans = Leet Font")
gamelength = 60

# -- Setting the break variables to false --
brkmenu = False
brkmain = False
brkpost = False

# -- things that will be later used within functions
subtextcolour = int
start = float
reactionlist = []
dark = False
colourstr = str
reactionstart = int
start_ticks = int
score = 0

# -- positions for the menu --
rect_start = pygame.Rect(30, 415, 250, 100)
rect_leaderboard = pygame.Rect(280, 415, 250, 100)
rect_menuquitbox = pygame.Rect(530, 415, 250, 100)
rect_titlebox = pygame.Rect(210, 175, 400, 300)
rect_scorebox = pygame.Rect(200, 100, 400, 300)
rect_quitbox = pygame.Rect(50, 50, 100, 50)

# -- positions for the main game --
rect_green = pygame.Rect(200, 300, 200, 200)
rect_red = pygame.Rect(400, 300, 200, 200)
rect_yellow = pygame.Rect(200, 100, 200, 200)
rect_blue = pygame.Rect(400, 100, 200, 200)
text_box1 = pygame.Rect(200, 425, 400, 200)
text_box2 = pygame.Rect(570, 5, 280, 100)
text_box3 = pygame.Rect(530, 50, 300, 100)
text_box4 = pygame.Rect(570, 45, 300, 100)

# -- positions for the postgame --
rect_restart = pygame.Rect(150, 50, 100, 50)
rect_smallmenu = pygame.Rect(250, 50, 100, 50)
rect_scorecard = pygame.Rect(200, 200, 400, 300)
rect_highscore = pygame.Rect(200, 250, 400, 300)
rect_avgreaction = pygame.Rect(200, 300, 400, 320)

# -- leaderboard scene positions
rect_highscoretitle = pygame.Rect(200, 100, 400, 300)
rect_highscore1 = pygame.Rect(200, 150, 400, 300)
rect_highscore2 = pygame.Rect(200, 200, 400, 300)
rect_highscore3 = pygame.Rect(200, 250, 400, 300)
rect_highscore4 = pygame.Rect(200, 300, 400, 300)
rect_highscore5 = pygame.Rect(200, 350, 400, 300)


# -- functions for features; clock, reaction time etc... --
# -- function to turn the game into darkmode --
def Darkmode():
    global BLACK, WHITE, RED, YELLOW
    global GREEN, BLUE, NIGHT, dark

    dark = True
    BLACK = (200, 200, 200)
    NIGHT = BLACK
    WHITE = (28, 28, 28)
    RED = (130, 0, 0)
    GREEN = (0, 130, 0)
    YELLOW = (130, 130, 0)
    BLUE = (0, 0, 130)


# -- function to switch the program back into lightmode --
def Lightmode():
    global BLACK, WHITE, RED, YELLOW
    global GREEN, BLUE, NIGHT, dark

    dark = False
    BLACK = (0, 0, 0)
    NIGHT = BLACK
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 0)
    BLUE = (0, 0, 255)


# -- selects a random str to be the correct colour --
def Selection():
    global colourstr, reactionstart
    colourstr = random.choice(["Red", "Green", "Blue", "Yellow"])
    reactionstart = time.time()


# -- selects the correct colour code based on the correct string --
def CorrectTuple():
    if colourstr == "Red":
        return RED
    if colourstr == "Green":
        return GREEN
    if colourstr == "Blue":
        return BLUE
    if colourstr == "Yellow":
        return YELLOW


# -- chooses the colour of the text underneath the buttons --
def RandomiseColour():
    global subtextcolour
    subtextcolour = random.choice([RED, GREEN, BLUE, YELLOW])


# -- generates a reference point for the timer --
def FetchTicks():
    global start_ticks
    start_ticks = pygame.time.get_ticks()


# -- the timer --
# -- uses a reference point and the current time to derive game time --
def CountDown():
    seconds = (pygame.time.get_ticks()-start_ticks)/1000
    timeleft = gamelength - seconds
    timeleft = int(timeleft)

    if timeleft < 1 and timeleft >= 0:
        global brkmain
        brkmain = True
        PostGame()

    return(timeleft)


# -- resets the score at the start of each game --
def ScoreReset():
    global score
    score = 0


# -- increases the score by a given amount --
def IncreaseScore(number):
    global score
    score = score + number


# -- the button and a combined test for correctness --
def DrawButton(surf, cursor_pos,
               pressed, rect, colour):
    global reactionlist
    pygame.draw.rect(surf, colour, rect)

    if rect.collidepoint(cursor_pos) and pressed:

        if colour == CorrectTuple():
            IncreaseScore(1)
            reactionlist.append(time.time()-reactionstart)
            pygame.time.delay(200)
            Selection()
            RandomiseColour()

        else:
            IncreaseScore(-1)
            Selection()
            RandomiseColour()
            pygame.time.delay(200)


# -- calculates the average reaction time for a game --
def AverageReaction():
    if len(reactionlist) == 0:
        return gamelength
    else:
        return sum(reactionlist) / len(reactionlist)


# -- button for the mainmenu --
def MenuButton(surf, cursor_pos, pressed,
               rect, colour):
    pygame.draw.rect(surf, colour, rect)

    if rect.collidepoint(cursor_pos) and pressed:
        MainGame()


# -- a button that leads to the leaderboard screen --
def LeaderboardButton(surf, cursor_pos, pressed,
                      rect, colour):
    pygame.draw.rect(surf, colour, rect)

    if rect.collidepoint(cursor_pos) and pressed:
        LeaderboardScene()


# -- a toggle between light and darkmode --
def DarkmodeButton(surf, cursor_pos, pressed,
                   rect, colour):
    global dark
    if not dark:
        text = "Night"
    if dark:
        text = "Day"

    pygame.draw.rect(surf, colour, rect)
    text_surf, text_rect = smallfont.render(text, WHITE)
    text_rect.center = rect.center
    screen.blit(text_surf, text_rect)

    if rect.collidepoint(cursor_pos) and pressed:
        pygame.time.delay(150)
        if not dark:
            dark = True
            Darkmode()
        elif dark:
            dark = False
            Lightmode()


# -- A button that restarts the game --
def Restartbutton(surf, cursor_pos, pressed,
                  rect, colour):
    pygame.draw.rect(surf, colour, rect)

    text_surf, text_rect = smallfont.render("Retry?", BLACK)
    text_rect.center = rect.center
    screen.blit(text_surf, text_rect)

    if rect.collidepoint(cursor_pos) and pressed:
        MainGame()


# -- a button that goes to the menu --
def Gotomenu(surf, cursor_pos, pressed,
             rect, colour):
    pygame.draw.rect(surf, colour, rect)

    if rect.collidepoint(cursor_pos) and pressed:
        Menu()


# -- a button that quits the game --
def QuitButton(surf, cursor_pos, pressed,
               rect, colour):
    pygame.draw.rect(surf, colour, rect)

    if rect.collidepoint(cursor_pos) and pressed:
        exit()


# -- like QuitButton, but a small version
def SmallQuitButton(surf, cursor_pos, pressed,
                    rect, colour):
    pygame.draw.rect(surf, colour, rect)

    text_surf, text_rect = smallfont.render("Quit", BLACK)
    text_rect.center = rect.center
    screen.blit(text_surf, text_rect)

    if rect.collidepoint(cursor_pos) and pressed:
        exit()


# -- a small version of menu button --
def SmallMenuButton(surf, cursor_pos, pressed,
                    rect, colour):
    pygame.draw.rect(surf, colour, rect)

    text_surf, text_rect = smallfont.render("Menu", BLACK)
    text_rect.center = rect.center
    screen.blit(text_surf, text_rect)

    if rect.collidepoint(cursor_pos) and pressed:
        Menu()


# -- creates text --
def TextGen(surf, rect, text_colour,
            text):
    text_surf, text_rect = font.render(text, text_colour)
    text_rect.center = rect.center
    screen.blit(text_surf, text_rect)


# -- checks leaderboard exists on users computer --
def CheckLeaderboard():
    # -- If leaderboard doesn't exist, creates it and appends 5 zeroes --
    if not os.path.isfile('localleaderboard.txt'):
        data = open("localleaderboard.txt", "w")
        data.write("0, 0, 0, 0, 0")


# -- reads in the data from the text file --
def ParseLeaderboard():
    # -- The main function of the ParseLeaderboard function
    # opens the leaderboard file, reads it in then converts it into a list. --
    data = open("localleaderboard.txt", "r")
    processdata = data.read()
    str(processdata)
    leaderboard = processdata.split(",")

    # -- convert elements from leaderboard text file from string to integer --
    leaderboard = [int(i) for i in leaderboard]

    # -- puts leaderboard in ascending order --
    leaderboard.sort()

    # -- return leaderboard --
    return(leaderboard)


# -- writes score to the leaderboard file --
def AppendLeaderboard(score):
    data = open("localleaderboard.txt", "a")
    data.write(", " + str(score))


# -- functions for scenes such as menu, maingame and postgame --
def Menu():
    reactionlist.clear()
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        pos = pygame.mouse.get_pos()
        leftClicked = pygame.mouse.get_pressed()[0]

        screen.fill(WHITE)
        MenuButton(screen, pos, leftClicked, rect_start, GREEN)
        LeaderboardButton(screen, pos, leftClicked, rect_leaderboard, BLUE)
        QuitButton(screen, pos, leftClicked, rect_menuquitbox, RED)
        DarkmodeButton(screen, pos, leftClicked, rect_quitbox, NIGHT)
        TextGen(screen, rect_menuquitbox, BLACK, "Quit")
        TextGen(screen, rect_titlebox, RED, "Game by Ben")
        TextGen(screen, rect_leaderboard, BLACK, "Leaderboard")
        TextGen(screen, rect_start, BLACK, "Play!")
        pygame.display.flip()
        clock.tick(60)


# -- a scene that shows high scores --
def LeaderboardScene():
    run = True
    CheckLeaderboard()
    leaderboard = ParseLeaderboard()
    RandomiseColour()

    while run:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit()

        pos = pygame.mouse.get_pos()
        leftClicked = pygame.mouse.get_pressed()[0]

        screen.fill(WHITE)
        TextGen(screen, rect_highscoretitle, subtextcolour,
                "Reaction Game Hall of Fame")
        TextGen(screen, rect_highscore1, subtextcolour,
                "1. " + str(leaderboard[-1]))
        TextGen(screen, rect_highscore2, subtextcolour,
                "2. " + str(leaderboard[-2]))
        TextGen(screen, rect_highscore3, subtextcolour,
                "3. " + str(leaderboard[-3]))
        TextGen(screen, rect_highscore4, subtextcolour,
                "4. " + str(leaderboard[-4]))
        TextGen(screen, rect_highscore5, subtextcolour,
                "5. " + str(leaderboard[-5]))

        Gotomenu(screen, pos, leftClicked,
                 rect_quitbox, GREEN)
        TextGen(screen, rect_quitbox,
                BLACK, "Menu")

        pygame.display.flip()
        clock.tick(60)


# -- the main game scene --
def MainGame():
    FetchTicks()
    Selection()
    ScoreReset()
    RandomiseColour()
    reactionlist.clear()

    pygame.time.delay(500)
    run = True
    while run:

        for event in pygame.event.get():
            if CountDown() < 1 and CountDown() >= 0:
                PostGame()
            if event.type == pygame.QUIT:
                exit()

        pos = pygame.mouse.get_pos()
        leftClicked = pygame.mouse.get_pressed()[0]

        screen.fill(WHITE)
        DrawButton(screen, pos, leftClicked,
                   rect_green, GREEN)
        DrawButton(screen, pos, leftClicked,
                   rect_red, RED)
        DrawButton(screen, pos, leftClicked,
                   rect_yellow, YELLOW)
        DrawButton(screen, pos, leftClicked,
                   rect_blue, BLUE)

        TextGen(screen, text_box1,
                subtextcolour, colourstr)
        TextGen(screen, text_box2, BLACK,
                "Score: " + str(score))
        TextGen(screen, text_box3, BLACK,
                str(CountDown() % 100).zfill(2))

        pygame.display.flip()
        clock.tick(60)


# -- the post game card
def PostGame():
    CheckLeaderboard()
    AppendLeaderboard(score)
    leaderboard = ParseLeaderboard()
    AverageReaction()

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        pos = pygame.mouse.get_pos()
        leftClicked = pygame.mouse.get_pressed()[0]

        screen.fill(WHITE)

        Restartbutton(screen, pos, leftClicked,
                      rect_restart, GREEN)
        SmallQuitButton(screen, pos, leftClicked,
                        rect_quitbox, RED)
        SmallMenuButton(screen, pos, leftClicked,
                        rect_smallmenu, BLUE)

        TextGen(screen, rect_scorecard, BLUE,
                "Your score: " + str(score))
        TextGen(screen, rect_avgreaction, BLACK, "Your Average reaction: "
                + str(round(AverageReaction(), 3)) + " seconds")
        TextGen(screen, rect_highscore, BLACK,
                "The high score was: " + str(leaderboard[-1]))

        pygame.display.flip()
        clock.tick(60)


# -- Calling the Game functions --
run = True
while run:
    Menu()
    MainGame()
    PostGame()

pygame.QUIT
exit()
