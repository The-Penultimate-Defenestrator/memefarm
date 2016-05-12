"""
memefarm - generate an effectively unlimited number of memes by blindly
combining random images and words.
"""


# Dependencies
from PIL import Image, ImageDraw, ImageFont
import random

# Internal modules
import imagesearch
import wordgen


# GLOBALS
commonwords = wordgen.getWords()  # Common english words
memefont = ImageFont.truetype("Impact")


class memefarm(object):
    """ A 'meme farm' capabale of generating memes. """
    def __init__(self, words=commonwords):
        self.words = words

    def word(self):
        """ Get a random word from the words with which the """
        return random.choice(self.words)

    def phrase(self, length=(3, 6)):
        """ Create a random sentence, given an acceptable range for numbers of
        number of words"""
        wordcount = random.randint(*length)
        return ' '.join([self.word() for _ in range(wordcount)])

    def image(self):
        """ Get a random image by searching for a random word """
        search = self.word()
        return imagesearch.getImage(search)

if __name__ == "__main__":
    # Tests
    mf = memefarm()      # Make a memefarm
    print(mf.phrase())   # Print a random sentence
    i = mf.image()       # Find a random image
    print(i.searchterm)  # Show the search term used
    i.show()             # Show the image
