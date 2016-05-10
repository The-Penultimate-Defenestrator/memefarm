"""
memefarm - generate an effectively unlimited number of memes by blindly
combining random images and words.
"""

from PIL import Image
import random

import wordgen

commonwords = wordgen.getWords()

class memefarm(object):
    def __init__(self, words=commonwords):
        self.words = words

    def getRandomWord(self):
        """ Get a random word from the words with which the """
        return random.choice(self.words)

    def getSentence(self, length=(3,6)):
        """ Create a random sentence with a given range for numbers of words"""
        return ' '.join([self.getRandomWord() for _ in range(random.randint(3,6))])

if __name__ == "__main__":
    mf = memefarm()
    print('\n\n'.join([mf.getSentence() for _ in range(10)]))