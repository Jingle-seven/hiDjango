import os
import random
import urllib.request
import win32gui
import win32con
from PIL import Image

class StealBing:

    def __init__(self):
        self.content = urllib.request.urlopen('http://cn.bing.com/').read()
        self.bgImageUrl = ''
        self.localFileName = ''
        self.localBMPFileName = ''

    def parserImageURL(self):
        tempStr = str(self.content)
        startIndex = tempStr.index('g_img={url:')+13
        endIndex = tempStr.index(',id:')-1
        tempStr = tempStr[startIndex:endIndex]
        tempStr = tempStr.replace('\\', '')
        self.bgImageUrl = tempStr
        print(tempStr)

    #仅用于生成本地文件名，在这里修改保存的路径
    def createLocalFileName(self):
        randomStr = ''.join(random.sample(['a','b','c','d','e','f','g','h','i','j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'], 6)).replace(" ","")
        self.localFileName =  'e:/desktop/background/' + randomStr + '.jpg'
        self.localBMPFileName = 'e:/desktop/background/' + randomStr + '.bmp'

    def downloadImage(self):
        if self.bgImageUrl == '':
            self.parserImageURL()
        if self.localFileName == '':
            self.createLocalFileName()
        urllib.request.urlretrieve(self.bgImageUrl, self.localFileName)
    def updataBGImage(self):
        img = Image.open(self.localFileName)
        img.save(self.localBMPFileName)
        os.remove(self.localFileName)
        win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, self.localBMPFileName, 0)

if __name__ == '__main__':
    stealBing = StealBing()
    stealBing.downloadImage()
    stealBing.updataBGImage()