# memefarm
A simple randomized meme generator, inspired by Mila claiming to own a "meme farm." `memefarm` is capable of churning out an effectively unlimited number of unique memes (see "Possibilities").

## How

`memefarm` automatically generates randomized memes by
leveraging the wealth of images on the internet, in conjunction with an english
dictionary. `memefarm` will generate memes by picking a random image from the internet
(powered by a google search for a random word), and then picking some random
words to overlay on the image.

## Possibilities

`memefarm` can generate a *massive* number of memes.
- My dictionary file contains `354986` english words.
- For each of these, `memefarm` can pick one of 10 random images from a google image search. If we assume there are no repeats, and that the top google image results never change (which they do), this means we have roughly `3549860` possible images.
- For each of these images, we can use up to 10 words. With `354986` words, this means [we can have `87570121444401570769320794434386499351990451762305479580101` different combinations of words](http://www.wolframalpha.com/input/?i=sum+C(3549860%2Bi-1,+i),+i%3D0+to+10).
- If I did math correctly (which I probably didn't), there are `310861671310623360011181115330851258589656825092937729742217335860` possible memes to be generated.

In other words, for all effective purposes, we have unlimited memes that can come out of this.
