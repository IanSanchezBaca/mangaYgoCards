##################################################
### The main page this will prob not handle much
##################################################
import os, ast, argparse
from talkers import filetalker, webtalker, imagetalker, databasetalker, pdfTalker

def main(ydkPath, imgFolder, saveImages):
    ### loads the database
    database = databasetalker.loadDataBase()
    
    ### grabs the ydk path and makes a list of the codes
    ### The list is a 2d vector with each vector with the first element being the code and the second element being how many times it comes up
    ydk = ydkPath
    ydkdeck = filetalker.openFile(ydk)

    ### this checks if they added the path to the images
    if imgFolder:
        imagetalker.changePath(imgFolder)

    ### grabs cards from either the "database" or from the website
    new = []
    deck = []
    for card in ydkdeck[:]:
        check = databasetalker.check(database, card[0])
        if check:
            deck.append(check)
        else:
            temp = webtalker.searchCard(card[0])
            if temp:
                deck.append(temp)
                new.append(temp)
            else:
                ydkdeck.remove(card)

    ### creates the image
    for card in deck:
        imagetalker.makeCard(card)
        # print(card)

    ### will make pdf file here
    pdfTalker.importCards(ydkdeck)
    pdfTalker.makeCards()

    ### cleaning up or not
    if not saveImages:
        for filename in os.listdir("output"):
            if filename.lower().endswith('.jpg'):
                file_path = os.path.join("output", filename)
                if os.path.isfile(file_path):
                    os.remove(file_path)

    ### saves new cards not already in the database
    if len(new):
        print("saving new cards!")
        databasetalker.saveDataBase(new)
        

def testing():
    cards = []
    with open("template/3cards.db", 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip():
                card = ast.literal_eval(line.strip())
                cards.append(card)

    return cards

if __name__ == "__main__":
    ### global variables for flags and stuff
    parser = argparse.ArgumentParser(description="Manga Style YGO Proxie PDF Generator")

    ### Required positional argument: path to YDK file
    parser.add_argument('ydk_path', help='Path to .ydk deck file')

    ### Optional positional argument: image folder
    parser.add_argument('image_folder', nargs='?', help='Folder containing card images')

    ### Optional flag: -s
    parser.add_argument('-s', action='store_true', help='Save the jpg images created')

    args = parser.parse_args()

    main(args.ydk_path, args.image_folder, args.s)

### monster card format
# name, attr, types(vector), lvl, atk/def(vector), effect, ydkcode

### spell/trap card format
# name, spell/trap, type, effect, ydkcode