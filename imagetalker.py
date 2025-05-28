### This file should maybe handle all of the image editing

from PIL import Image #This is used to open images
from PIL import ImageDraw # this is used to draw to images



def main():
    print("Inside imagetalker, running test")

    mage = Image.new('RGB', (100,100), color='white')
    # This is how to crate a new image

    drw = ImageDraw.Draw(mage)

    drw.text((10,10), "owo", fill=(0,0,0))

    mage.putpixel((50,50), (255,0,0))

    mage.show()

    mage.save("tempimg.png", "PNG")


def outerBorder(card, width, height): # creates the border on the outer side of the card
    ### making the outer border
    # the top border
    for y in range(25):
        for i in range(width):
            card.putpixel((i, y), (0,0,0))
    # bottom border
    for y in range(height - 25, height):
        for i in range(width):
            card.putpixel((i, y), (0,0,0))
    # left border
    for x in range(25):
        for i in range(height):
            card.putpixel((x, i), (0,0,0))
    # right border
    for x in range(width - 25, width):
        for i in range(height):
            card.putpixel((x, i), (0,0,0))

def imageBorder(card, width, height):
    ### create the image border

    ### top border
    for i in range(10): # the thickness of the border
        for j in range(640):
            card.putpixel((85 + j, 205 + i), (0,0,0))

    ### bottom border
    for i in range(10): # the thickness of the border
        for j in range(640):
            card.putpixel((85 + j, 835 + i), (0,0,0))

    ### left border
    for i in range(10): # the thickness of the border
        for j in range(640):
            card.putpixel((85 + i, 205 + j), (0,0,0))

    ### right border
    for i in range(10): # the thickness of the border
        for j in range(640):
            card.putpixel((715 + i, 205 + j), (0,0,0))
    


def createTemplate():
    width = 813
    height = 1185


    card = Image.new('RGB', (width, height), color='white')

    # brush = ImageDraw.Draw(card)

    outerBorder(card, width, height)
    imageBorder(card, width, height)



    # card.show()

    card.save("template.png")



if __name__ == "__main__":
    # main()
    createTemplate()


### border is 25px

### image border is 10px
##  border "starts" at (85, 205)
##  border "ends" at (725, 845)
#   this makes an even 640 x 640 square
