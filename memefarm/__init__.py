"""
memefarm - generate an effectively unlimited number of memes by blindly
combining random images and words.
"""


# Dependencies
from PIL import Image, ImageDraw, ImageFont
import random

# Internal modules
import imagesearch
import pilutil
import wordgen


# GLOBALS
commonwords = wordgen.getWords()  # Common english words
memefont = ImageFont.truetype("Impact")


# PUBLIC API

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

    def image(self, debug=False):
        """ Get a random image by searching for a random word """
        search = self.word()
        out = imagesearch.getImage(search)
        if debug:
            pilutil.labelImage(out, out.searchterm)
        return out

    def meme(self):
        # Find an image
        i = self.image(True)
        w, h = i.size
        d = ImageDraw.Draw(i)
        # Top text
        t1 = self.phrase((3, 4))
        pilutil.drawTextWithBorder(d, t1, (w / 10, 0),
                                   fontsize=pilutil.findFontSize(t1, w)
                                   )
        return i
