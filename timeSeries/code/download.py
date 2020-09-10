import requests
import os
from datetime import datetime


DOWNLOAD_SAVE_DIR = os.getenv("DOWNLOAD_SAVE_DIR")

if __name__ == "__main__":

    url = "https://www.mizuhobank.co.jp/market/csv/"
    response = requests.get(url)

    contentType = response.headers['Content-Type']
    contentDisposition = response.headers['Content-Disposition']
    ATTRIBUTE = 'filename='
    filename = contentDisposition[contentDisposition.find(ATTRIBUTE) + len(ATTRIBUTE):]

    saveFileName = datetime.now().strftime("%Y%m%d_%H%M%S_") + filename

    with open(saveFileName, 'wb') as saveFile:
        saveFile.write(response.content)
