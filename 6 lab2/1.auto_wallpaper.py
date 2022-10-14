""" Problem:
    Download and change desktop wallpapers automatically
"""
import requests
import json
import PyWallpaper

api_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

# get the json
response = requests.get(api_url)
content = response.content.decode('UTF-8')


# convert string to json
dict_content = json.loads(content)

# get the image url
image_url = dict_content['url']

# download the image
res = requests.get(image_url)

# save the image
with open('apod.png', 'wb') as image:
    image.write(res.content)


# set as wallpaper
PyWallpaper.change_wallpaper('/Users/ashrafminhaj/Documents/PH/phitron-lab2/apod.png')