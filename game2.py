import pgzrun
from random import randint

# screen height and width
WIDTH = 800
HEIGHT = 600
w , h = WIDTH , HEIGHT
# player in the middle of the screen
p=Rect((w//2 , h//2),(20,30))    # player
e=Rect((0,h//2),(20,30))        # enemy
c=Rect((200,200),(10,10))     # coin
score = 0                      # score 

#music 
#music.play('background - this is file name') mp3 file

def draw():
    screen.fill("black")
    screen.draw.filled_rect(p, "white")
    screen.draw.filled_rect(e, "red")
    screen.draw.filled_rect(c, "yellow")
    screen.draw.text(f'Score:{score}', topleft=(10,10), fontsize = 30)

def update(dt):
    global score
    # player controls
    if keyboard.left: p.x += -3
    if keyboard.right: p.x += 3
    if keyboard.up: p.y += -3
    if keyboard.down: p.y += 3
    if p.x < 0: p.x = w
    if p.x > w: p.x = 0
    if p.x < 0: p.y = h
    if p.x > h: p.y = 0
    # enemy follows player
    if e.x < p.x: e.x += 2
    if e.x > p.x: e.x += -2
    if e.x < p.y: e.y += 2
    if e.x > p.y: e.y += -2
    # collision detection
    if p.colliderect(e):
        print('Game Over!')
        quit()
    if p.colliderect(c):
        score += 1
        #sounds,coin.play(file name)
        c.x = randint (0,w)
        c.y = randint (0,h)

pgzrun.go()