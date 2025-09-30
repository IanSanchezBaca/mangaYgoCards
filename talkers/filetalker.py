####################################
### This file handles the file stuff
### i.e. opening and reading the ydk
####################################

def openFile(filename):
    
    try:
        file = open(filename, 'r')
    except FileNotFoundError:
        print(f"filetalker-Error: the file '{filename}' does not exist.")
        exit(-1)

    deck = []

    for line in file:
        card = line.strip()
        if card and card[0].isdigit():
            deck.append(card)

    print(deck) 

    return deck


if __name__ == "__main__":
    openFile("../onomatRyzeal.ydk")
    # openFile("bogus")

    