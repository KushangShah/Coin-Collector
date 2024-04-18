import pygame
import pgzero
import pyzero
from random import randint


# pgzrun /Users/bina/Code?/Exercise/Game?/"Coin-Collector"/CoinCollector.py

# setting screen size
WIDTH = 720
HEIGHT = 480

# initiallizing score 0
score = 0

# to tell Pygame Zero if the game is over or not
game_over = False

# introducing the actor
fox = Actor('fox')
fox.pos = 100, 100
coin = Actor('coin')
coin.pos= 200, 200

# setting screen
def draw():
    screen.fill("purple")
    fox.draw()
    coin.draw()
    screen.draw.text("Score:" + str(score), color='black', topleft=(10, 10))

    if game_over:
        screen.fill('pink')
        screen.draw.text("Final score: " + str(score), topleft=(10, 10), font = 60)

# defining functions
def place_coin():
    coin.x = randint(15, (WIDTH - 15))
    coin.y = randint(15, (HEIGHT - 15))

def times_up():
    global game_over
    game_over = True

def update():
    global score
    if keyboard.left:
        fox.x -= 5
    elif keyboard.right:
        fox.x += 5
    elif keyboard.up:
        fox.y -= 5
    elif keyboard.down:
        fox.y += 5

    coin_colleceted = fox.colliderect(coin)

    if coin_colleceted:
        score += 10
        place_coin()
        
# Run the function
clock.schedule(times_up, 7.0)

place_coin()