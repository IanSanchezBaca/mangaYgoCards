### This file handles the file stuff

def openFile(filename):
    
    try:
        file = open(filename, 'r')
    except FileNotFoundError:
        print(f"Error: the file '{filename}' does not exist.")
        exit(-1)

    deck = []

    for line in file:
        card = line.strip()
        if card[0].isdigit():
            if not card in deck:
                deck.append(card)

    return deck


if __name__ == "__main__":
    openFile("../template/Goblins.ydk")

    