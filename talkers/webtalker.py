#########################################################
### This searches the website for the stuff that I need
#########################################################

import requests as req
from bs4 import BeautifulSoup as soup

def searchCard(name: str):
    ### getting the url ready
    url = "https://yugipedia.com/wiki/"
    url = url + name
    # cardName = ""
    
    headers = { # this is so that we dont get blocked
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/122.0.0.0 Safari/537.36'
    }
 
    try: ### error checking
        res = req.get(url, headers=headers, timeout=10)
        res.raise_for_status() ### this should raise an error if status is not 200
    except req.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")
        print("If this is an AltArt it wont work")
        return None

    s = soup(res.text, 'html.parser')
    tags = s.find_all(attrs={"title": True})
    titles = [tag['title'] for tag in tags]
    
    lore = s.find('div', class_='lore')
    lore = lore.get_text(separator=' ', strip=True)

    # print(lore)
    

    cardTypeIndex = getIndex(titles, "Card type")

    if cardTypeIndex:
        match titles[cardTypeIndex + 1]:
            case "Monster Card":
                # print("this is a Monster Card")
                card = monsterCardo(titles)
                if(card):
                    card.append(lore)
                # print(card)
            case "Spell Card":
                card = spelltrapCard(titles, "Spell")
                card.append(lore)
                # print(card)
            case "Trap Card":
                card = spelltrapCard(titles, "Trap")
                card.append(lore)
                # print(card)
    else:
        ### shouldn't be able get here as card name that doesnt exists wont work anyway
        print(f"could not find index for {name}, maybe doesnt exist.")
        exit(-1)

    if card:
        card.append(name) ### this should be the ydk code
    # print(card)

    if card:
        return card ### comment this back in
    else:
        return None

def monsterCardo(titles):
    monster = []
    cardName = titles[0]
    monster.append(cardName)

    ### get attribute
    if (Index := getIndex(titles, "Attribute")):
        # print(cardAttribute := titles[Index+1])
        cardAttribute = titles[Index+1]
        monster.append(cardAttribute)
    else:
        print(f"Could not find attribute of {cardName}")
        exit(-1)

    ### get types
    i = 1
    # numofTypes = i
    types = []
    if (Index := getIndex(titles, "Type")):

        while titles[Index + i] != "Level" and titles[Index + i] != "Rank":
            temp = titles[Index + i].split()[0]
           
            if temp == "Link":
                print(f"Links dont work: {cardName}")
                return
            
            types.append(temp)
            i = i + 1
        # numofTypes = i - 1
    
    # print(types)
    # exit(-1)

    monster.append(types)

    ### get level/rank
    cardLevel = titles[Index + i + 1].split()[1]
    monster.append(cardLevel)

    ### get atk/def
    i = 1
    stats = []
    if (Index := getIndex(titles, "DEF")):
        while titles[Index+i] != "Password":
            temp = titles[Index + i].split()[0]
            stats.append(temp)
            i = i + 1
    
    monster.append(stats)

    return monster

def spelltrapCard(titles, type):
    card = []
    ### name
    card.append(titles[0])

    ### type
    card.append(type)

    ### property?
    if (Index := getIndex(titles, "Property")):
        card.append(titles[Index+1])

    return card

def getIndex(titles, type):
    try:
        index = titles.index(type)
        # print("Index of 'Card type':", index)
        return index
    except ValueError:
        print("'Card type' not found in the list.")
        return -1

def main():
    searchCard("7084129") # magicians rod
    searchCard("Dark_Magician")
    searchCard("Monster_Reborn") 
    searchCard("Skill_Drain") 
    searchCard("Solemn_Judgment")
    searchCard("Lunalight_Tiger")
    searchCard("Divine_Arsenal_AA-ZEUS_-_Sky_Thunder")
    searchCard("34001672") # gobonga
    searchCard("Windwitch_-_Snow_Bell")
    searchCard("Hallohallo")
    
if __name__ == "__main__":
    main()
