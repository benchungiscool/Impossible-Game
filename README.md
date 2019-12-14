# Impossible Game #
### By Ben Chung ###

Written using pygame, the aim of the game is to get as many points as possible within a given time. The user is prompted with a 4 squares,
each of a different colour and the name of a colour beneath.

## The Menu ##
![Menu Daymode](https://i.imgur.com/2TgAfPW.png "The Menu in daymode")
###### Above: The Menu in day mode ######

![Menu Darkmode](https://i.imgur.com/gl87T3X.png "The Menu in darkmode")
###### Above: The Menu in darkmode ######

The Menu is a simple system with three options, begin the game, go to the leaderboard screen or quit the game. There is also a daymode darkmode
toggle which applies to all facets of the game.

## The Leaderboard ##
![Leaderboard](https://i.imgur.com/30Mqwjd.png "The Leaderboard")
###### Above: The Leaderboard ######

The leaderboard is read in from a text file, ordered and then the top 5 entries locally are displayed on this screen. In future I may make
this a sql database so I can have multiple datapoints other than just score for each game such as; Username, points per minute and the average
reaction time, which would allow me to make a richer leaderboard experience and rank on different things, other than just score.

## The Main Game ##
![Main Game](https://i.imgur.com/OD0cqkY.png "The Main Game")
###### Above: The Main Game ######

There is a timer which when runs down to zero moves to an end of game card. Your score is recorded in a local text file and your average
reaction time is displayed which will be displayed in the post game card

## The Post Game Card ##
![Post Game](https://i.imgur.com/VnEiZD3.png "The Post Game card")
###### Above: The post game card ######

The post game card displays three things; your score, the high score and the average reaction time for the previous game. The high score
is read in the same way as for the leaderboard screen, the average reaction time is calculated by dividing the sum of a list of reaction
times by the length of the list, the high score for the previous game is also appended to the end of the local text file, for use in future
games. There is also a mini menu, whereby you can either retry the game, return to the menu or quit the game.

## What I learned ##

This is the first project that I have undertaken both in python and programming generally. This firstly helped to develop my approach to
software development, my approach was first to get core functionality, and then build around that which, in this case meant first getting the important part: the main game, done first before worrying about menu and post game card done.

Also this was my first introduction to PEP-8 development standard, another goal was to ensure that the code was as readable as possible
and while it may not be perfect, as it was my first try, I'm certainly happy with how it turned out. I used it because it was going to be both submitted to my teachers, and because it was going to be uploaded to github, as well as building good habits for future projects. I overall think that the improvement to readability is well worth the extra time needed to avoid longlineitis.
