#########################################################
### This searches the website for the stuff that I need
### NOTE I might need to change the website and links
#########################################################
import os
import requests as req
import json ### used for testing


def saveEdgeCases(imgurl, path):
    try:
        r = req.get(imgurl, timeout=10) ### adding a timeout
        if r.status_code == 200:
            with open(path, 'wb') as file:
                file.write(r.content)
    
    except req.exceptions.Timeout:
        print("request timed out")
    
    except req.exceptions.RequestException as e:
        print("request Failed: ", e)
        

    return

def saveImage(imgurl, path):
    try:
        r = req.get(imgurl, timeout=10) ### adding a timeout
        if r.status_code == 200:
            with open(path, 'wb') as file:
                file.write(r.content)
    
    except req.exceptions.Timeout:
        print("request timed out")
    
    except req.exceptions.RequestException as e:
        print("request Failed: ", e)
        

    return

    
def searchCard(name):
    data = ""
    cardName = str(name)

    ### ygoprodeck api
    url = f"https://db.ygoprodeck.com/api/v7/cardinfo.php?id={cardName}"
    res = req.get(url, timeout=10)
    if res.status_code == 200:
        data = res.json()["data"][0]

    ### getting and saving the image
    imgurl = data["card_images"][0]["image_url_cropped"]
    
    if (data["type"] == "Link Monster" or "Pendulum" in data["type"]):
        imgurl = data["card_images"][0]["image_url"]
        
        ### This should mean that the monster is a link or pendulum monster
        saveDir = "output/" + cardName + ".jpg"
        if not os.path.exists(saveDir):
            cardName + ".jpg"
            saveImage(imgurl, saveDir) ### save the image

    else:
        saveDir = "tempImages/cropped_" + cardName + ".jpg"

        ### check if the file already exists
        if not os.path.exists(saveDir):
            cardName + ".jpg"
            saveImage(imgurl, saveDir) ### save the image

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
