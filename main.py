##################################################
### The main page this will prob not handle much
##################################################
import sys ### using this for argv
import ast
from talkers import filetalker, webtalker, imagetalker, databasetalker

def main():
    if len(sys.argv) < 2:
        print("Usage: ./main.py <path to ydk file> <path to folder of images>")
        exit(-1)
    
    ### loads the database
    database = databasetalker.loadDataBase()
    
    ### grabs the ydk path and makes a deck of the codes
    ydk = sys.argv[1] ### grab the ydk file path
    ydkdeck = filetalker.openFile(ydk)


    ### this checks if they added the path to the images
    if len(sys.argv) >= 3:
        imagetalker.changePath(sys.argv[2])

    # ydkdeck = filetalker.openFile("template/3cards.ydk")
    # ydkdeck = filetalker.openFile("template/Goblins.ydk")
    # ydkdeck = filetalker.openFile("template/link.ydk")
    # ydkdeck = filetalker.openFile("template/altart.ydk")
    # deck = testing()
    
    new = []
    deck = []
    for card in ydkdeck:
        check = databasetalker.check(database, card[0])
        # databasetalker.check(database, card[0])
        if check:
            # print(check)
            deck.append(check)
        else:
            temp = webtalker.searchCard(card[0])
            if temp:
                deck.append(temp)
                new.append(temp)


    for card in deck:
        imagetalker.makeCard(card)
        # print(card)
        
    
    if len(new):
        print("saving new cards!")
        databasetalker.saveDataBase(new)
    # else:
    #     print("no new cards")
        


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