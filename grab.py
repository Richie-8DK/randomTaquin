from bs4 import BeautifulSoup
import requests
from random import choice
from io import BytesIO


params = {
	"min_height": None,
	"orientation": None,
	"image_type": None,
	"cat": None,
	"q": None,
	"min_width": None,
	"order": "ec",
	"colors": None,
	"pagi": None
}

def get_imgs(params=params, url="https://pixabay.com/de/photos"):
    # get page's content
    page = requests.get(url).text

    # find all imgs from page
    soup = BeautifulSoup(page, "html.parser")
    imgs = [img.get("src") for img in soup.find_all("img")]
    imgs = soup.find_all("img")
    return imgs


# not necessary but nice to have
def download_galerie(params=params, url="https://pixabay.com/de/photos"):
    imgs = get_imgs(params, url)

    # download
    i = 0
    for img in imgs:
        src = img.get("src")
        if (src == "/static/img/blank.gif"):
            src = img.get("data-lazy")
        print(src)
        with open("pics/" + str(i) + ".jpg", "wb") as f:
        	f.write(requests.get(src).content)
        	i += 1

def get_img(saveTo=False, params=params, url="https://pixabay.com/de/photos"):
    imgs = get_imgs(params, url)

    # choose random image from imgs
    img = choice(imgs)
    # get the url of the img
    src = img.get("src")
    if src == "/static/img/blank.gif": src = img.get("data-lazy")
    # get th img itself
    img = requests.get(src).content

    img = BytesIO(img)

    # save the img if path is given
    if (saveTo):
        with open(saveTo) as f:
            f.write(img)

    print(img)
    return img
