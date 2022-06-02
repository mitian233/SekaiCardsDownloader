
# Sekai Cards Downloader

A sample script help you download Sekai cards and convert them to jpeg. 

## Setup

```bash
# clone this repo
git clone https://github.com/mitian233/SekaiCardsDownloader.git
cd tootbot

# install required python modules
pip3 install -r requirements.txt
```

## Usage

Change the following contents in the script:

```python
#==========================================================
#Proxy
os.environ["http_proxy"] = "http://127.0.0.1:18899"
os.environ["https_proxy"] = "http://127.0.0.1:18899"

characterNumber = 17 #Check the role number in the url
picNumber = 17 #Check the total number of cards in the url
saveNumber = 1 #Specify the naming start number
refer_url = 'minio.dnaroma.eu' #You need to change this variable if the CDN domain name changes
#==========================================================
```

And then run the script.

<details>
<summary>Sort method</summary>
Download by card order, first download normal picture of a specified card, and then download its after training picture. If there is no pafter training picture, output 404 and skip. File nuber continue numbering.
</details>

## ATTENTION
 
THIS SCRIPT REFERENCES SOME RESOURCES OF [SEKAI VIEWER](https://sekai.best/), PLEASE USE THIS SCRIPT AS PERMITTED BY LAW AND RESCOURCE LICENSE. 

## Copyright

© Sekai Viewer

© SEGA / © Colorful Palette Inc. / © Crypton Future Media, INC. www.piapro.net All rights reserved.