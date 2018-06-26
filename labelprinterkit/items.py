"""
Objects that can be placed in a label template
"""

from PIL import Image, ImageDraw, ImageFont
import segno

class Text:
    """A simple text item"""
    def __init__(self, font: ImageFont = None) -> None:
        if font:
            self.font = font
        else:
            # fallback to default font
            self.font = ImageFont.load_default()

    def render(self, text):
        image = Image.new("1", self.font.getsize(text), "white")
        draw = ImageDraw.Draw(image)
        draw.text((0, 0), text, "black", self.font)
        return image

class MultiLineText:
    """A simple text item"""
    def __init__(self, font: ImageFont = None) -> None:
        if font:
            self.font = font
        else:
            # fallback to default font
            self.font = ImageFont.load_default()

    def render(self, text):
        lines = text.split('\n')
        images = []
        for l in lines:
            image = Image.new("1", self.font.getsize(l), "white")
            draw = ImageDraw.Draw(image)
            draw.text((0, 0), l, "black", self.font)
            images.append(image)

        width = max([i.size[0] for i in images])
        height = max([i.size[1] for i in images])

        img = Image.new("1", (width, height * len(lines)), "white")
        for n, i in enumerate(images):
            img.paste(i, box=(0, n * height, i.size[0], n * height + i.size[1]))

        return img


class MicroQR:
    """A simple QR item"""
    def __init__(self, width=32, height=32):
        self.size = (width, height)

    def render(self, text):
        qr = segno.make_micro(text)
        image = qr.to_pil(background=None, border=0)
        image = image.resize(self.size)
        return image
