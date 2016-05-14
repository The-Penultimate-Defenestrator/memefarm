""" Helpers for making some things in PIL easier """
from PIL import ImageDraw, ImageFont, ImageStat
from math import ceil


def drawTextWithBorder(draw, text, coords,
                       fontname="Impact", fontsize=80,
                       color="#fff", strokecolor="#000"):
    """ Draw text with a border. Although PIL doesn't support this, it can be
    faked by drawing the text in the border color, with offsets, and then
    drawing the text in the center on top.

    See http://stackoverflow.com/a/8050556/4414003 """

    # 3 looks good for 80px font. This allows for adjusting proportionally.
    strokewidth = ceil(3 * fontsize / 80.0)  # Use ceiling to prevent 0

    font = ImageFont.truetype(fontname, fontsize)
    x, y = coords
    # Draw background
    for c in ((x - strokewidth, y - strokewidth),
              (x + strokewidth, y - strokewidth),
              (x - strokewidth, y + strokewidth),
              (x + strokewidth, y + strokewidth)):
        draw.text(c, text, font=font, fill=strokecolor)

    draw.text(coords, text, font=font, fill=color)


def labelImage(im, text):
    """ Label an image with a string in the bottom left, using a text color
    that will ensure appropriate contrast. """
    d = ImageDraw.Draw(im)
    textsize = ImageFont.load_default().getsize(text)
    coords = im.size[0] - textsize[0] - 5, im.size[1] - textsize[1] - 5
    # Check color of image where the text would go
    textarea = im.crop(coords + im.size)
    textareabrightness = ImageStat.Stat(im.convert("L")).mean[0]
    color = (0, 0, 0) if textareabrightness > 128 else (255, 255, 255)
    # Draw text
    d.text(coords, text, fill=color)


def proportionalResize(im, width):
    """ Resize an image to be a specified width while keeping aspect ratio """
    w, h = im.size
    aspect = float(h) / float(w)

    out = im.resize((width, int(width * aspect)))  # Resize to fit width

    return out


def findFontSize(text, width, font="Impact", margin=10):
    """ Find the largest font size that will fit `text` onto `im`, given a
    margin (in percent) that must be left around an image border. """
    w = int(width * (1 - margin / 100.0 * 2))  # Width accounting for margin
    wAt40 = ImageFont.truetype(font, 40).getsize(text)[0]  # find size at 40px
    return 40 * w / wAt40  # Use a proportion to adjust that for image size


if __name__ == "__main__":
    from PIL import Image, ImageDraw

    # Blank test image
    i = Image.new("RGB", (1024, 768), "#abcdef")
    d = ImageDraw.Draw(i)
    # Calculate font size
    text = "OMG SUCH FONT"
    fontsize = findFontSize(text, 1024)
    # Render font onto canvas (102px is 10% margin)
    drawTextWithBorder(d, text, (102, 102), fontsize=fontsize)

    # Test proportional resizing to a larger width
    proportionalResize(i, 2000).show()
    # Test proportional resizing to a smaller widthAt40
    proportionalResize(i, 400).show()
