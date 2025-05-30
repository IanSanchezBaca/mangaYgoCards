#####################################################################
### This file should maybe probably handle all of the image editing
#####################################################################
from PIL import Image, ImageDraw, ImageFont
import textwrap

### loading this in early i uess
star = Image.open("template/black-star-icon.png")
star = star.resize((50,50), Image.Resampling.LANCZOS)

path = ""

def changePath(p):
    global path 
    # path = p ### comment this back in after tou finish
    path = "D:/Users/iansa/Documents/ProjectIgnis/pics"

def cropImage(card, template):
    # print(f"going into {path}")
    if path:
        cardImage = path + "/" + card[len(card) - 1] + ".jpg"
        sticker = Image.open(cardImage)
    
        # Coordinates: (left, top, right, bottom)
        crop_box = (96, 216, 717, 835)
        sticker = sticker.crop(crop_box)

        # Paste the cropped image onto the destination image at (0, 0)
        template.paste(sticker, (95, 215))

        # template.show()
    
    output = "output/" + card[len(card)-1] + ".jpg"
    template.save(output)

def makeMagic(card):
    name = card[0]
    magicType = card[1]
    type = card[2]
    eff = card[3]
    # code = card[4]

    print(f"Working on {name}!")

    template = Image.open("template/template.png")
    brush = ImageDraw.Draw(template)

    drawAttribute(magicType, brush)
    drawName(name, brush)
    drawLevel(brush, type)
    drawEffect(eff, brush)
    cropImage(card, template)

    # template.show()

def makeMonster(card):
    name = card[0]
    attr = card[1]
    types = card[2] # vector
    lvl = int(card[3])
    stats = card[4] # vector
    eff = card[5]
    # code = card[6] 
    
    print(f"Working on {name}!")

    template = Image.open("template/template.png")
    brush = ImageDraw.Draw(template)
    
    drawAttribute(attr, brush)
    drawName(name, brush)
    drawLevel(template, lvl)
    drawType(types, brush)
    drawEffect(eff, brush)
    drawStats(stats, brush)
    cropImage(card, template)

    # template.show()
    # template.save(f"{name}.png")

def drawStats(stats, brush):
    blood = f"ATK {stats[0]}     DEF {stats[1]}"
    # Load a bigger font (adjust the path if needed)
    font = ImageFont.truetype("arial.ttf", 32)  # Use larger size
    # center
    att_x, att_y = 406, 1120
    # Get text bounding box
    bbox = brush.textbbox((0, 0), blood, font=font)
    txt_w = bbox[2] - bbox[0]
    txt_h = bbox[3] - bbox[1]
    # Calculate top-left to center it
    text_x = att_x - txt_w // 2
    text_y = att_y - txt_h // 2
    # Draw the text
    
    brush.text((text_x, text_y), blood, font=font, fill="black")

def drawEffect(eff, brush):
    # Box coordinates
    top_left = (60, 880)
    bottom_right = (750, 1070)
    box_width = bottom_right[0] - top_left[0]
    box_height = bottom_right[1] - top_left[1]

    top_padding = 20
    bottom_padding = 20
    usable_box_height = box_height - top_padding - bottom_padding
    start_y = top_left[1] + top_padding

    
    # Load font
    font_path = "arial.ttf"  # Update if needed
    max_font_size = 60
    min_font_size = 10

    # Try decreasing font sizes until text fits
    for font_size in range(max_font_size, min_font_size - 1, -1):
        font = ImageFont.truetype(font_path, font_size)

        # Estimate characters that can fit in one line
        avg_char_width = font.getlength("A")
        max_chars_per_line = max(1, box_width // avg_char_width)

        wrapped_lines = textwrap.wrap(eff, width=int(max_chars_per_line), break_long_words=True)

        line_height = font.getbbox("A")[3] - font.getbbox("A")[1]
        total_text_height = line_height * len(wrapped_lines)

        if total_text_height <= usable_box_height:
            break

        # if total_text_height <= box_height:
        #     break  # Found a size that fits

    # Draw text centered in the box
    # y = top_left[1] + (box_height - total_text_height) // 2
    # for line in wrapped_lines:
    #     x = top_left[0]  # left align text
    #     brush.text((x, y), line, font=font, fill="black")
    #     y += line_height

    y = start_y - 20
    line_spacing = 5
    for line in wrapped_lines:
        x = top_left[0] + 100
        brush.text((x, y), line, font=font, fill="black")
        y += line_height + line_spacing

def drawType(types, brush):
    typ = "[{}]".format(" / ".join(types))

    # Load a bigger font (adjust the path if needed)
    font = ImageFont.truetype("arial.ttf", 25)  # Use larger size

    # Get text bounding box
    # bbox = brush.textbbox((0, 0), typ, font=font)
    # txt_w = bbox[2] - bbox[0]
    # txt_h = bbox[3] - bbox[1]

    # tl_x = 85
    tl_x = 60
    tl_y = 850

    # Draw the text
    brush.text((tl_x, tl_y), typ, font=font, fill="black")

def drawLevel(template, lvl):
    starx = 674
    stary = 150
    ### will make this work with spell and trap cards as well
    if isinstance(lvl, int):
        for i in range(lvl):
            blud = 55 * i
            template.paste(star, (starx - blud, stary), mask=star)
    else:
        font = ImageFont.truetype("arial.ttf", 32)  # Use larger size
        lvl = "(" + lvl + ")"
        template.text((starx - 400, stary + 10), lvl, font=font, fill="black")

def drawName(name, brush):
    left, top = 49, 52
    right, bottom = 762, 128
    box_width = right - left
    box_height = bottom - top

    # Start trying from a big font size and go down if needed
    max_font_size = 100
    min_font_size = 5
    best_font = None

    # Load a font (change path if needed)
    font_path = "arial.ttf"  # Or any .ttf you have

    for size in range(max_font_size, min_font_size - 1, -1):
        font = ImageFont.truetype(font_path, size)
        bbox = brush.textbbox((0, 0), name, font=font)
        text_w = bbox[2] - bbox[0]
        text_h = bbox[3] - bbox[1]

        if text_w <= box_width and text_h <= box_height:
            best_font = font
            break

    # If no font fits, fall back to smallest
    if best_font is None:
        best_font = ImageFont.truetype(font_path, min_font_size)

    # Get size of final text
    bbox = brush.textbbox((0, 0), name, font=best_font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]

    # Center the text in the box
    text_x = left + (box_width - text_w) // 2
    text_y = top + (box_height - text_h) // 2

    # Draw the text
    brush.text((text_x, text_y + 20), name, font=best_font, fill="black")

def drawAttribute(attr, brush): ### this should also work with spell/trap
    # Load a bigger font (adjust the path if needed)
    font = ImageFont.truetype("arial.ttf", 32)  # Use larger size
    # center
    att_x, att_y = 717, 50
    # Get text bounding box
    bbox = brush.textbbox((0, 0), attr, font=font)
    txt_w = bbox[2] - bbox[0]
    txt_h = bbox[3] - bbox[1]
    # Calculate top-left to center it
    text_x = att_x - txt_w // 2
    text_y = att_y - txt_h // 2
    # Draw the text
    brush.text((text_x, text_y), attr, font=font, fill="black")

def makeCard(card):
    if len(card) == 7:
        makeMonster(card)
    else:
        makeMagic(card)


##### Below this is only used to make the temp card #######################

def main():
    print("Inside imagetalker, running test")

    mage = Image.new('RGB', (100,100), color='white')
    # This is how to crate a new image

    drw = ImageDraw.Draw(mage)

    drw.text((10,10), "owo", fill=(0,0,0))

    mage.putpixel((50,50), (255,0,0))

    # mage.show()

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
