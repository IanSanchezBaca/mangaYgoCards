### This file should maybe handle all of the image editing

from PIL import Image #This is used to open images
from PIL import ImageDraw # this is used to draw to images



def main():
    print("Inside imagetalker, running test")

    mage = Image.new('RGB', (100,100), (255,255,255))

    drw = ImageDraw.Draw(mage)

    drw.text((10,10), "owo", fill=(0,0,0))

    mage.show()

    mage.save("tempimg.png", "PNG")


if __name__ == "__main__":
    main()

