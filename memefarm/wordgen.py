''' Build a word list of the 1000 most common words. I'm
using the word list that was used in Randall Munroe's
"Thing Explainer," and pulling it off xkcd.com '''

import os

import requests

localdir = os.path.dirname(__file__)


def getWords():
    """ If the word list has not been downloaded, download
    it. Then return the word list. """

    wordspath = os.path.join(localdir, "words.txt")

    # Word list has not been downloaded. Download, save, and return words.
    if not os.path.exists(wordspath):
        r = requests.get("http://xkcd.com/simplewriter/words.js")
        words = r.text.split('"')[1].split("|")
        with open(wordspath, "wb") as f:
            f.write("\n".join(words).encode("utf-8"))
        return words

    # Words list is saved, read and return.
    with open(wordspath, "r") as f:
        return [l.strip() for l in f.readlines()]


if __name__ == "__main__":
    getWords()
