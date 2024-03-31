from pygame import *
window = display.set_mode((800, 400))
display.set_caption('Ping Pong')
color1 = (222,184,135)
window.fill(color1)
clock = time.Clock()
FPS = 60
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)
