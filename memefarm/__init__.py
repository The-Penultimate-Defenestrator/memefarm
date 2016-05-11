"""
memefarm - generate an effectively unlimited number of memes by blindly
combining random images and words.
"""

from PIL import Image
import random

import wordgen


# Load words
commonwords = wordgen.getWords()


class memefarm(object):
    """ A 'meme farm' capabale of generating memes. """
    def __init__(self, words=commonwords):
        self.words = words

    def getRandomWord(self):
        """ Get a random word from the words with which the """
        return random.choice(self.words)

    def getSentence(self, length=(3, 6)):
        """ Create a random sentence, given an acceptable range for numbers of
        number of words"""
        wordcount = random.randint(*length)
        return ' '.join([self.getRandomWord() for _ in range(wordcount)])

if __name__ == "__main__":
    mf = memefarm()
    print('\n\n'.join([mf.getSentence() for _ in range(10)]))
