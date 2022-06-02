import requests
import os
from PIL import Image

#==========================================================
#Proxy
os.environ["http_proxy"] = "http://127.0.0.1:18899"
os.environ["https_proxy"] = "http://127.0.0.1:18899"

characterNumber = 17 #Check the role number in the url
picNumber = 17 #Check the total number of cards in the url
saveNumber = 1 #Specify the naming start number
refer_url = 'minio.dnaroma.eu' #You need to change this variable if the CDN domain name changes
#==========================================================

ua = {'User-Agent': 'Mozilla/5.0'}
if len(str(characterNumber)) < 2:
    character = "00" + str(characterNumber)
else:
    character = "0" + str(characterNumber)

#Define rename module
def rename(Number):
    if len(str(Number))<2:
        conv = "00" + str(Number)
    else:
        conv = "0" + str(Number)
    return conv

#Define downloader module
def downloader(url, saveNumber):
    r = requests.get(url, headers=ua)
    if r.status_code == 200:
        savename = rename(saveNumber)
        filename_png = savename + ".png"
        filename_jpg = savename + ".jpg"
        f = open(filename_png, 'wb')
        f.write(r.content)
        f.close()
        im = Image.open(filename_png)
        im = im.convert('RGB')
        im.save(filename_jpg, quality=95)
        os.remove(filename_png)
        print("\033[32m[SUCCESS]\033[0mWrite " + filename_jpg)
    else:
        print("\033[31m[ERROR]\033[0mCode:" + str(r.status_code))
    return r.status_code

#Main module
for i in range(1 , picNumber + 1):
    pic = rename(i)
    #Download normal card image
    url = "https://" + refer_url + "/sekai-assets/character/member/res" + character + "_no" + pic + "_rip/card_normal.png"
    if downloader(url, saveNumber)==200:
        saveNumber += 1
    #Download after training card image
    url = "https://" + refer_url + "/sekai-assets/character/member/res" + character + "_no" + pic + "_rip/card_after_training.png"
    if downloader(url, saveNumber)==200:
        saveNumber += 1
print("\033[32m[SUCCESS]\033[0mDownload complete!")