import requests
from bs4 import BeautifulSoup
from win32com.client import Dispatch

class DownloadFitChromeDrive:
    def __init__(self):
        self.get_chrome_version()
        self.climb_chromedriver_version()
        self.arrange_version_list()
        self.downloadVersion = self.get_chromedriver_download_version()
        
    def climb_chromedriver_version(self):  #從chromedriver下載頁面上爬出所有chromedriver版本
        response = requests.get("https://chromedriver.chromium.org/downloads")
        rep = BeautifulSoup(response.text, "html.parser")
        self.versionList = []
        tmp = {}
        # print(rep.select("p[dir='ltr'] a[href][target='_blank'] span"))
        for i in rep.select("p[dir='ltr'] a[href][target='_blank'] span"):
            if i.text != "release notes":
                self.versionList.append(i.text)
        tmp = tmp.fromkeys(self.versionList)
        self.versionList = list(tmp.keys())

    def arrange_version_list(self): #整理並歸納爬下來的chromedriver版本，存出兩個串列，一是去掉最後一位的版號，另一是完整版號
        tmp = ""
        self.compareVersionList = []
        for i in range(len(self.versionList)):
            if "ChromeDriver " in self.versionList[i]:
                self.versionList[i] = self.versionList[i].replace("ChromeDriver ", "")
                tmp = self.versionList[i].split(".")
                tmp.pop()
                self.compareVersionList.append(".".join(tmp))
    def get_version_via_com(self, filename): #從目標路徑取得該機器上的Chrome當前版本
        parser = Dispatch("Scripting.FileSystemObject")
        try:
            version = parser.GetFileVersion(filename)
        except Exception:
            return None
        return version

    def get_chrome_version(self): #將機器的chrome版本最後一位去除
        self.chromeVersion = list(filter(None, [self.get_version_via_com(p) for p in [r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"]]))[0]
        tmp = self.chromeVersion.split(".")
        tmp.pop()
        self.chromeVersion = ".".join(tmp)
        return self.chromeVersion
    
    def get_chromedriver_download_version(self): #把機器上去掉最後一位的版號與chromedriver去掉一位版號的串列作搜尋，抓出對應index，並取得完整版號
        if self.chromeVersion in self.compareVersionList:
            downloadVersion = self.versionList[self.compareVersionList.index(self.chromeVersion)]
            return downloadVersion

