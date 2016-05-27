"""
memefarm - generate an effectively unlimited number of memes by blindly
combining random images and words.
"""


# Dependencies
from PIL import ImageDraw, ImageFont
import random

# Internal modules
import imagesearch
from pilutil import drawTextWithBorder, findFontSize, labelImage
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
            labelImage(out, out.searchterm)
        return out

    def meme(self, debug=False):
        # Find an image
        i = self.image(debug)
        w, h = i.size
        d = ImageDraw.Draw(i)
        # Top text
        t1 = self.phrase((3, 4)).upper()
        drawTextWithBorder(d, t1, (w / 10, 0), fontsize=findFontSize(t1, w))
        # Bottom text (50% chance)
        if random.randint(0, 1):
            t2 = self.phrase((4, 5)).upper()
            size = findFontSize(t2, w)
            fontheight = memefont.getsize(t2)[1] + h / 8  # Add some margin
            drawTextWithBorder(d, t2, (w / 10, h - fontheight), fontsize=size)
        return i

if __name__ == "__main__":
    import os
    if not os.path.exists("memes"):
        os.mkdir("memes")

    mf = memefarm()
    for x in range(35, 100):
        print(x)

        def save_meme():
            try:
                mf.meme().convert("RGBA").save("memes/{}.png".format(x))
            except ValueError:
                print("Drawing text failed. Retrying...")
                save_meme()

        save_meme()
