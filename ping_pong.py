from pygame import *
window = display.set_mode((700, 500))
display.set_caption('Ping Pong')
color1 = (90, 90, 90)
window.fill(color1)
clock = time.Clock()
FPS = 60
game = True

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Players(GameSprite):
    def updatel(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < 320:
            self.rect.y += self.speed
    def updater(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < 320:
            self.rect.y += self.speed
racket1 = Players('platform.png', 10, 200, 5, 95, 176)
racket2 = Players('platform.png', 590, 200, 5, 95, 176)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill(color1)
    racket1.reset()
    racket1.updatel()
    racket2.reset()
    racket2.updater()
    display.update()
    clock.tick(FPS)

