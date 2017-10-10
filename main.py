import grab, crop, game

if __name__ == '__main__':
    img = grab.get_img()
    w, h = map(int, crop.crop(img, 3, 3))
    game.start((w, h))
