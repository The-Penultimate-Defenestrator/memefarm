import json
import os
import random
import requests

from io import BytesIO
from PIL import Image


# GLOBALS

class APIRateLimitError(Exception):
    pass


endpoint = "https://www.googleapis.com/customsearch/v1"
searchid = "013060195084513904668:z7-hxk7q35k"

# Retrieve my API key from a secret file
with open(os.path.join(os.path.dirname(__file__), "API_KEY.txt"), "r") as f:
    API_KEY = f.read()


# API

def getImageUrl(search, silent=False, attempt=0):
    """ Get a ramdom image URL from the first 10 google images results for a
    given search term """
    r = requests.get(endpoint, params={
        "key": API_KEY,
        "cx": searchid,

        "searchType": "image",

        "q": search,
    })

    data = json.loads(r.text)        # Load JSON responses
    try:
        results = data["items"]      # Find the images returned
    except KeyError:                 # If we fail...

        if attempt > 3:
            raise APIRateLimitError("Looks like you ran out of API calls")

        elif not silent:
            print("Search failed. Retrying...")

        return getImageUrl(search, attempt=attempt + 1)  # Try again (recur)

    result = random.choice(results)  # Pick a random one
    return result["link"]            # Return its link


def getImage(search):
    """ Get a PIL image for a given search term """
    url = getImageUrl(search)  # Get an image URL
    req = requests.get(url)    # Download image
    b = BytesIO(req.content)   # Load into file-like object
    try:
        out = Image.open(b)    # Open and return
    except IOError:
        print("Reading retrieved image failed. Retrying...")
        return getImage(search)
    out.searchterm = search    # Store the search term used

    return out


if __name__ == "__main__":
    # Tests
    i = getImage("cow")  # Search for an image
    i.show()             # Show it
    print(i.searchterm)  # Test custom attribute
