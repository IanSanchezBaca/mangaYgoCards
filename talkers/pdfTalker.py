##################################################
### This file will handle all of the pdf stuff
##################################################
### examples of other proxy makers
### https://dejauxvue.github.io/YGOProxyGenerator/html/index.html
### https://proxies.ygoresources.com
import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, mm

cards = []

def importCards(deck):
    global cards
    cards = deck

    image_names = []
    for name, count in cards:
        for _ in range(count):
            image_names.append(name + ".jpg")

    cards = image_names

def makeCards():
    ### Configuration 
    image_folder = "output"  # Folder where card images are stored
    output_pdf = "proxies.pdf"
    card_width = 2.31 * inch  # 59 mm
    card_height = 3.37 * inch  # 86 mm
    cards_per_row = 3
    cards_per_col = 3
    margin = .5 * mm
    padding = .5 * mm

    ### Prepare 
    # images = sorted([
    #     f for f in os.listdir(image_folder)
    #     if f.lower().endswith(('.jpg', '.jpeg', '.png'))
    # ])
    images = cards
    c = canvas.Canvas(output_pdf, pagesize=A4)
    page_width, page_height = A4
    cards_per_page = cards_per_row * cards_per_col

    ### Total Grid Size (with gaps)
    total_grid_width = cards_per_row * card_width + (cards_per_row - 1) * padding
    total_grid_height = cards_per_col * card_height + (cards_per_col - 1) * padding

    ### Centering Offsets
    margin_x = (page_width - total_grid_width) / 2
    margin_y = (page_height - total_grid_height) / 2


    ### Draw Cards 
    for i, img_name in enumerate(images):
        row = (i % cards_per_page) // cards_per_row
        col = (i % cards_per_page) % cards_per_row

        x = margin_x + col * (card_width + padding)
        y = page_height - margin_y - (row + 1) * card_height - row * padding

        img_path = os.path.join(image_folder, img_name)

        try:
            c.drawImage(img_path, x, y, width=card_width, height=card_height,
                        preserveAspectRatio=True, anchor='c')
        except Exception as e:
            print(f"Failed to draw image {img_name}: {e}")

        if (i + 1) % cards_per_page == 0:
            c.showPage()

    c.save()
    print(f"Saved: {output_pdf}")