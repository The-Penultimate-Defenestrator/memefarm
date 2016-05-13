""" Helpers for making some things in PIL easier """
from PIL import ImageFont


def drawTextWithBorder(draw, text, coords,
                       fontname="Impact", fontsize=80, strokewidth=3,
                       color="#fff", strokecolor="#000"):
    """ Draw text with a border. Although PIL doesn't support this, it can be
    faked by drawing the text in the border color, with offsets, and then
    drawing the text in the center on top.

    See http://stackoverflow.com/a/8050556/4414003 """

    font = ImageFont.truetype(fontname, fontsize)
    x, y = coords
    # Draw background
    for c in ((x - strokewidth, y - strokewidth),
              (x + strokewidth, y - strokewidth),
              (x - strokewidth, y + strokewidth),
              (x + strokewidth, y + strokewidth)):
        draw.text(c, text, font=font, fill=strokecolor)

    draw.text(coords, text, font=font, fill=color)


def proportionalResize(im, width):
    """ Resize an image to be a specified width while keeping aspect ratio """
    w, h = im.size
    aspect = float(h) / float(w)

    out = im.resize((width, int(width * aspect)))  # Resize to fit width

    return out

if __name__ == "__main__":
    from PIL import Image, ImageDraw
    i = Image.new("RGB", (1024, 768), "#abcdef")
    d = ImageDraw.Draw(i)
    drawTextWithBorder(d, "SUCH FONT", (10, 10))
    proportionalResize(i, 400).show()
