from Chromedriver_version import DownloadFitChromeDrive
from web_control import WebControl
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#使用webdriver_manager chrome抓取我需要版本之chromedriver
#版號使用爬蟲至網頁上爬取與本地端chrome瀏覽器當前版號匹配的版本
#可避免當最新版webdriver release後，與本地電腦之chrome瀏覽器版號對不上，造成程式直接終止的狀況出現
#WebControl為整合selenium動作之Library
driver = webdriver.Chrome(ChromeDriverManager(version= DownloadFitChromeDrive().downloadVersion).install())
webControl = WebControl(driver)