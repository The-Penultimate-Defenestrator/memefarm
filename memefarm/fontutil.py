""" PIL doesn't have a built-in method for drawing text with a border. This
provides that. The defaults are set to full meme power, white with black
outline. """
from PIL import ImageFont


def drawTextWithBorder(draw, text, coords,
                       fontname="Impact", fontsize=80, strokewidth=3,
                       color="#fff", strokecolor="#000"):
    """ Draw text with a border. Although PIL doesn't support this, it can be
    faked by drawing the text in the border color, with offsets, and then
    drawing the text in the center on top. See
    http://stackoverflow.com/a/8050556/4414003 """

    font = ImageFont.truetype(fontname, fontsize)
    x, y = coords
    # Draw background
    for c in ((x - strokewidth, y - strokewidth),
              (x + strokewidth, y - strokewidth),
              (x - strokewidth, y + strokewidth),
              (x + strokewidth, y + strokewidth)):
        draw.text(c, text, font=font, fill=strokecolor)

    draw.text(coords, text, font=font, fill=color)


if __name__ == "__main__":
    from PIL import Image, ImageDraw
    i = Image.new("RGB", (500, 500), "#abcdef")
    d = ImageDraw.Draw(i)
    drawTextWithBorder(d, "SUCH FONT", (10, 10))
    i.show()
