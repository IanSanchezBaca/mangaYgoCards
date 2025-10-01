#########################################################
### This searches the website for the stuff that I need
### NOTE I might need to change the website and links
#########################################################
import os
import requests as req
import json ### used for testing


def saveImage(imgurl, path):

    r = req.get(imgurl)
    if r.status_code == 200:
        with open(path, 'wb') as file:
            file.write(r.content)

    return

    
def searchCard(name):
    cardName = str(name)
    saveDir = "output/cropped_" + cardName + ".jpg"

    ### check if the file already exists
    if not os.path.exists(saveDir):
        imgurl = "https://images.ygoprodeck.com/images/cards_cropped/" + cardName + ".jpg"
        saveImage(imgurl, saveDir) ### save the image

    ### ygoprodeck api
    url = f"https://db.ygoprodeck.com/api/v7/cardinfo.php?id={cardName}"

    data = ""

    res = req.get(url)
    if res.status_code == 200:
        data = res.json()["data"][0]

    # saveCardData(data)

    return data

def saveCardData(data): ### used for testing
    with open("utopia.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def main():
    # searchCard(34909328)
    searchCard(84013237)
    # saveCardData()
   
    
if __name__ == "__main__":
    main()
