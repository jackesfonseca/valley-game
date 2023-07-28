from pygame.math import Vector2

SCREEN_WIDTH = 1290
SCREEN_HEIGHT = 700
TILE_SIZE = 64

OVERLAY_POSITIONS = {
    'tool' : (40, SCREEN_HEIGHT - 35),
    'seed' : (45, SCREEN_HEIGHT - 5)
}

PLAYER_TOOL_OFSET = {
    'left' : Vector2(-50,40),
    'right' : Vector2(50, 40),
    'up' : Vector2(0,10),
    'down' : Vector2(0,50)
}

LAYERS = {
    'water' : 0,
    'ground' : 1,
    'soil' : 2,
    'soil water' : 3,
    'rain floor' : 4,
    'house bottom' : 5,
    'ground plant' : 6,
    'main' : 7,
    'house top' : 8,
    'fruit' : 9,
    'rain drops' : 10
}