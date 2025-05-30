####################################
### This file handles the file stuff
####################################

def openFile(filename):
    
    try:
        file = open(filename, 'r')
    except FileNotFoundError:
        print(f"Error: the file '{filename}' does not exist.")
        exit(-1)

    deck = []

    for line in file:
        card = line.strip()
        if card and card[0].isdigit():
            found = False
            for entry in deck:
                if entry[0] == card:
                    entry[1] += 1
                    found = True
                    break
            if not found:
                deck.append([card, 1])
    

    return deck


if __name__ == "__main__":
    openFile("../template/Goblins.ydk")

    