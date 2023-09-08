import pgzrun
from random import randint

#   screen height and width
WIDTH = 800
HEIGHT = 600

# title
title = "My First Game"
boxlist = []
for i in range (100):
    rx = randint(0, WIDTH)
    ry = randint(0, HEIGHT)
    sx = randint(10,100)
    sy = randint(10,100)
    boxlist.append(
        Rect((rx,ry) , (sx,sy))  # random position and size
    )

# display content on game screen
def draw():
    screen.fill("black")
    screen.draw.text(title, topleft=(10,10), fontsize = 60)
    for i in range(len(boxlist)):
        screen.draw.filled_rect(boxlist[i], "white")


# update content on game screen
def update(dt):
    print(f'update {dt}')

    # drop the box down
    for box in boxlist:
        box.y += 1              # y axis +1

pgzrun.go()