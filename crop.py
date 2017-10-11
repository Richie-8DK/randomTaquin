from PIL import Image
from os.path import isdir, join
from os import makedirs

# dissect img in number of rows and columns
def crop(img, rows, columns):
    img = Image.open(img) # load image
    w, h = img.size # width and height of th image
    w, h = w/columns, h/rows # width and height of a section

    # create folder
    dir = "out"
    create_dir(dir)

    # dissect
    # divide image in to section and save these actions named by their position
    for i in range(0, rows):
    	print(i)
    	for j in range(0, columns):
            # crop section
    		box = (w * i, h * j, w * (i + 1), h * (j + 1))
    		region = img.crop(box)
            # save section
    		region.save(join(dir, "{}-{}.jpg".format(j, i)))

    # return width an height of a section
    return w, h

# create given folder if it didn't exist
def create_dir(path):
    if not isdir(path):
        makedirs(path)
