from bs4 import BeautifulSoup
import requests

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

site = requests.get("https://pixabay.com/de/photos").text

soup = BeautifulSoup(site, "html.parser")
imgs = [img.get("src") for img in soup.find_all("img")]
print(imgs)
imgs = soup.find_all("img")

i = 0
for img in imgs:
    src = img.get("src")
    if (src == "/static/img/blank.gif"):
        src = img.get("data-lazy")
    print(src)
    with open("pics/" + str(i) + ".jpg", "wb") as f:
    	f.write(requests.get(src).content)
    	i += 1