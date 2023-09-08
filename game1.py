import pgzrun
from random import randint

#   screen height and width
WIDTH = 800
HEIGHT = 600

# title
title = "My First Game"
box1 = Rect((50,50),(200,200))  # box position and size

# display content on game screen
def draw():
    screen.fill("black")
    screen.draw.text(title, topleft=(10,10), fontsize = 60)
    screen.draw.filled_rect(box1,"white") # drae box1


# update content on game screen
def update(dt):
    print(f'update {dt}')
    # drop the box down
    box1.y += 1              # y axis +1

pgzrun.go()