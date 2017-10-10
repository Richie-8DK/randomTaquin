import sys, pygame
from random import choice
from math import floor

black = 0, 0, 0
imgh = 113
imgw = 324

field = []

# A Tile will contain nothing or a image
class Tile(pygame.Rect):
    """docstring for Tile"""
    def __init__(self, *args):
        super(Tile, self).__init__(args)
        self.taken = False
        self.owner = None

    def take(self, img):
        self.taken = img

    def empty(self):
        self.taken = False

def create_field():
    field = []
    for row in range(0,3):
        line = []
        for column in range(0,3):
            rect = Tile(column * imgw, row * imgh, imgw, imgh)
            line.append(rect)
        field.append(line)
    return field

def start(size):
    global imgh, imgw
    imgw, imgh = size
    size = size[0]*3, size[1]*3
    # start pygame
    pygame.init()

    # create screen
    global screen
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)

    # create field out of tiles
    global field
    field = create_field()

    # load images
    for row in range(0,3):
        for column in range(0,3):
            img = pygame.image.load("out/{}-{}.jpg".format(row, column))
            field[row][column].owner = img
            chose_field().take(img)

    # free tile
    global freeTile
    freeTile = (0, 0)
    field[0][0].taken = False

    main_loop()


def main_loop():
    while True:
        # get events
        event = pygame.event.wait()
        # print(event)
        if event.type == pygame.QUIT:
            sys.exit()

        handle_events(event)

        # draw content
        draw()

def handle_events(event):
    if event.type == pygame.KEYDOWN:
        row, column = freeTile
        if event.key == pygame.K_UP:
            turn((row + 1, column), freeTile)
        elif event.key == pygame.K_DOWN:
            turn((row - 1, column), freeTile)
        elif event.key == pygame.K_LEFT:
            turn((row, column + 1), freeTile)
        elif event.key == pygame.K_RIGHT:
            turn((row, column - 1), freeTile)
    elif event.type == pygame.MOUSEBUTTONUP:
        print("clickup")
        column, row = pygame.mouse.get_pos()
        print(row, column)
        row = floor(row / imgh)
        column = floor(column / imgw)
        print(row, column)
        turn((row, column), freeTile)

def draw():
    screen.fill(black)
    for line in field:
        for tile in line:
            if tile.taken:
                screen.blit(tile.taken, tile)
    pygame.display.flip()

def turn(source, target):
    global freeTile
    if in_field(source) == False:
        return

    # check if target is next to source
    if source[0] == target[0] and abs( source[1] - target[1] ) == 1:
        pass
    elif source[1] == target[1] and abs( source[0] - target[0] ) == 1:
        pass
    else:
        return

    freeTile = source

    # shift source.taken to target
    # and emty source
    source = get(source)
    target = get(target)
    img = source.taken
    source.taken = False
    target.taken = img

    # check if img is right placed
    if img == target.owner:
        check()

def chose_field(): # schlechter name ist kein field
    # TODO: max return issue
    tile = choice(choice(field))
    return tile if not tile.taken else chose_field()

# check if pos is field
def in_field(pos):
    row, column = pos
    if 0 > row or row >= len(field):
        return False
    if 0 > column or column >= len(field[0]):
        return False
    return True

# ropes pos in field
def rope_in(pos):
    row, column = pos
    row %= len(field)
    column %= len(field[0])
    return (row, column)

def get(pos):
    row, column = rope_in(pos)
    return field[row][column]

def check():
    for row in field:
        for tile in row:
            if tile.taken != tile.owner:
                return False
    return True

def won():
    screen.fill(black)
    for line in field:
        for tile in line:
            screen.blit(tile.owner, tile)
    pygame.display.flip()
