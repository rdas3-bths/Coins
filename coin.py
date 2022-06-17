from pgzero.builtins import Actor
from random import randint

WIDTH = 600
HEIGHT = 600
score = 0
game_over = False

fox = Actor("fox")
fox.pos = 100, 100
coin = Actor("coin")
coin.pos = 200, 200
display_text = "Score: " + str(score)


def draw():
    screen.fill("black")
    fox.draw()
    coin.draw()
    screen.draw.text(display_text, color="white", topleft=(10, 10))

    if game_over:
        screen.fill("pink")
        screen.draw.text("Final " + display_text, topleft=(10, 10), fontsize=60)


def place_coin():
    coin_x = randint(20, (WIDTH-20))
    coin_y = randint(20, (HEIGHT-20))
    coin.pos = coin_x, coin_y


def time_up():
    global game_over
    game_over = True


def update():
    global score
    global display_text

    if keyboard.a and keyboard.w:
        fox.x = fox.x - 4
        fox.y = fox.y - 4

    elif keyboard.d and keyboard.w:
        fox.x = fox.x + 4
        fox.y = fox.y - 4

    elif keyboard.a and keyboard.s:
        fox.x = fox.x - 4
        fox.y = fox.y + 4

    elif keyboard.d and keyboard.s:
        fox.x = fox.x + 4
        fox.y = fox.y + 4

    elif keyboard.a:
        fox.x = fox.x - 4
    elif keyboard.d:
        fox.x = fox.x + 4
    elif keyboard.w:
        fox.y = fox.y - 4
    elif keyboard.s:
        fox.y = fox.y + 4

    coin_collected = fox.colliderect(coin)

    if coin_collected:
        score = score + 10
        display_text = "Score: " + str(score)
        place_coin()


clock.schedule(time_up, 15.0)
place_coin()


