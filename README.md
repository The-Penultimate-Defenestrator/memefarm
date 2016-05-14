# memefarm
A simple randomized meme generator, inspired
by Mila claiming to own a "meme farm."
`memefarm` is capable of churning out an
effectively unlimited number of unique memes.

## How

`memefarm` automatically generates randomized memes by leveraging the wealth of
images on the internet, in conjunction with an english dictionary.

The english dictionary used is the list of the 1000 most common english words
(in all their forms) used to write "[Up Goer Five](https://xkcd.com/1133/),"
and eventually *[Thing Explainer](https://xkcd.com/thing-explainer/)*.

`memefarm` will generate memes by combining a random "sentence" with a random
image. `memefarm` generates random sentences by sticking words together at
random. It finds random images via a Google Images search for a random word.

Stick these two things together, and you've got a *really stupid looking meme*!

## Limitations

Because of harsh Google API limits, `memefarm` can only generate 100 memes/day.
For the same reason, users are required to register their own API keys with
Google to use this.
