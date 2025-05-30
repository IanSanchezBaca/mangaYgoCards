import ast

def loadDataBase():
    cards = []
    with open("template/database.db", 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip():
                card = ast.literal_eval(line.strip())
                cards.append(card)

    return cards

def check(database, card):
    # print(f"looking for {card}")
    for c in database:
        if c[len(c) - 1] == card:
            return c
            # print(f"found {card}")
        
    return None


def saveDataBase(new):
    with open("template/database.db", 'a', encoding='utf-8') as file:
        file.write("\n")
        for line in new:
            file.write(str(line) + "\n")