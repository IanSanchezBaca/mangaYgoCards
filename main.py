##################################################
### The main page this will prob not handle much
##################################################

import sys ### using this for argv
from talkers import filetalker, webtalker

def main():
    # if len(sys.argv) < 2:
    #     print("Usage: ./main.py <ydk file>")
    #     exit(-1)
    # ydk = sys.argv[1]
    # filetalker.openFile(ydk)


    ydkdeck = filetalker.openFile("template/Goblins.ydk")
    # ydkdeck = filetalker.openFile("template/link.ydk")
    # ydkdeck = filetalker.openFile("template/altart.ydk")


    deck = []
    for card in ydkdeck:
        deck.append(webtalker.searchCard(card))

    

    # if deck:
    #     print(deck)

    

if __name__ == "__main__":
    main()

    