##################################################
### The main page this will prob not handle much
##################################################

import sys ### using this for argv
import ast
from talkers import filetalker, webtalker, imagetalker

def main():
    # if len(sys.argv) < 2:
    #     print("Usage: ./main.py <ydk file>")
    #     exit(-1)
    # ydk = sys.argv[1]
    # filetalker.openFile(ydk)

    # ydkdeck = filetalker.openFile("template/3cards.ydk")
    # ydkdeck = filetalker.openFile("template/Goblins.ydk")
    # ydkdeck = filetalker.openFile("template/link.ydk")
    # ydkdeck = filetalker.openFile("template/altart.ydk")

    deck = testing()
    
    # deck = []
    # for card in ydkdeck:
    #     deck.append(webtalker.searchCard(card))


    for card in deck:
        # print(card)
        imagetalker.makeCard(card)

    # print("END")
        


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