from PIL import Image

# dissect img in number of rows and columns
def crop(img, rows, columns):
    img = Image.open(img)
    print(img.size)
    w, h = img.size # width and height of th image
    w, h = w/columns, h/rows # width and height of a piece

    # dissect
    for i in range(0, rows):
    	print(i)
    	for j in range(0, columns):
    		box = (w * i, h * j, w * (i + 1), h * (j + 1))
    		print(box)
    		region = img.crop(box)
    		print("out/{}.jpg".format(i))
    		region.save("out/{}-{}.jpg".format(j, i))

    return w, h
