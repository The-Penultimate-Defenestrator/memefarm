import json
import os
import random
import requests

from io import BytesIO
from PIL import Image

# GLOBALS

endpoint = "https://www.googleapis.com/customsearch/v1"
searchid = "013060195084513904668:z7-hxk7q35k"

# Retrieve my API key from a secret file
with open(os.path.join(os.path.dirname(__file__), "API_KEY.txt"), "r") as f:
    API_KEY = f.read()


# API

def getImageUrl(search):
    """ Get a ramdom image URL from the first 10 google images results for a
    given search term """
    r = requests.get(endpoint, params={
        "key": API_KEY,
        "cx": searchid,
        "searchType": "image",
        "q": search,
    })

    data = json.loads(r.text)        # Load JSON responses
    results = data["items"]          # Find the images returned
    result = random.choice(results)  # Pick a random one
    return result["link"]            # Return its link


def getImage(search):
    """ Get a PIL image for a given search term """
    url = getImageUrl(search)  # Get an image URL
    req = requests.get(url)    # Download image
    b = BytesIO(req.content)   # Load into file-like object
    return Image.open(b)       # Open and return


if __name__ == "__main__":
    getImage("cow").show()
