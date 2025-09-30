#########################################################
### This searches the website for the stuff that I need
### NOTE I might need to change the website and links
#########################################################
import os
import requests as req


def saveImage(imgurl, cardname):
    # print(imgurl)
    file_name = str(cardname) + ".jpg"
    saveDir = "../output/cropped_" + file_name

    # ### check if the file already exists
    # if os.path.exists(saveDir):
    #     return

    r = req.get(imgurl)
    if r.status_code == 200:
        with open(saveDir, 'wb') as file:
            file.write(r.content)

    
def searchCard(name: str):
    cardName = str(name)
    saveDir = "../output/cropped_" + cardName

    ### check if the file already exists
    if not os.path.exists(saveDir):
        imgurl = "https://images.ygoprodeck.com/images/cards_cropped/" + cardName + ".jpg"
        saveImage(imgurl, name) ### save the image

    ### ygoprodeck api
    url = f"https://db.ygoprodeck.com/api/v7/cardinfo.php?id={cardName}"

    data = ""

    res = req.get(url)
    if res.status_code == 200:
        data = res.json()["data"][0]

    return data


def main():
    searchCard(34909328)
   
    
if __name__ == "__main__":
    main()
