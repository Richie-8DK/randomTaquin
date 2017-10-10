from PIL import Image

im = Image.open("pics/7.jpg")
print(im.size)
w, h = im.size
tw, th = w/3, h/3
for i in range(0,3):
	print(i)
	for ii in range(0,3):
		box = (tw*i, th*ii, tw*(i+1), th*(ii+1))
		print(box)
		region = im.crop(box)
		print("out/{}.jpg".format(i))
		region.save("out/{}-{}.jpg".format(ii, i))