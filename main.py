##################################################
### The main page this will prob not handle much
##################################################
import os, ast, argparse, sys
from talkers import filetalker, webtalker, imagetalker, pdfTalker

def main(ydkPath, saveImages):
    
    ydk = ydkPath
    ydkdeck = filetalker.openFile(ydk)
    uniqueCards = set(ydkdeck)
    ### grabs cards from the website
    
    deck = []
    for card in uniqueCards:
        deck.append(webtalker.searchCard(card))
    
    ### creates the image
    for card in deck:
        imagetalker.makeCard(card)
     

    ### will make pdf file here
    pdfTalker.importCards(ydkdeck)
    pdfTalker.makeCards(sys.argv[1])

    
        

def testing():
    cards = []
    with open("template/3cards.db", 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip():
                card = ast.literal_eval(line.strip())
                cards.append(card)

    return cards


def testMain():
    print("testing")

if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("Usage: python3 main.py [ydkfile] [bool wether or not you want to save the images]")
        exit(-1)

    main(sys.argv[1], sys.argv[2])


    # ### global variables for flags and stuff
    # parser = argparse.ArgumentParser(description="Manga Style YGO Proxie PDF Generator")

    # ### Required positional argument: path to YDK file
    # parser.add_argument('ydk_path', help='Path to .ydk deck file')

    # ### Optional positional argument: image folder
    # parser.add_argument('image_folder', nargs='?', help='Folder containing card images')

    # ### Optional flag: -s
    # parser.add_argument('-s', action='store_true', help='Save the jpg images created')

    # args = parser.parse_args()

    # main(args.ydk_path, args.image_folder, args.s)

### monster card format
# name, attr, types(vector), lvl, atk/def(vector), effect, ydkcode

### spell/trap card format
# name, spell/trap, type, effect, ydkcode