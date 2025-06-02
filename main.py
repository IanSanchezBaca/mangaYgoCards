##################################################
### The main page this will prob not handle much
##################################################
import sys ### using this for argv
import ast
from talkers import filetalker, webtalker, imagetalker, databasetalker, pdfTalker

def main():
    if len(sys.argv) < 2:
        print("Usage:\n ./main.py <path to ydk file> optional:<path to folder of images> ")
        exit(-1)
    
    ### loads the database
    database = databasetalker.loadDataBase()
    
    ### grabs the ydk path and makes a list of the codes
    ### The list is a 2d vector with each vector with the first element being the code and the second element being how many times it comes up
    ydk = sys.argv[1] ### grab the ydk file path
    ydkdeck = filetalker.openFile(ydk)

    ### this checks if they added the path to the images
    if len(sys.argv) >= 3:
        imagetalker.changePath(sys.argv[2])

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
    main()

### monster card format
# name, attr, types(vector), lvl, atk/def(vector), effect, ydkcode

### spell/trap card format
# name, spell/trap, type, effect, ydkcode