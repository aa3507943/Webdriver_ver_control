from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from EventLog.exception_handler import ExceptionHandler

class WebControl(): #python v3.11.x selenium 4.8.x
    
    def __init__(self, driver:webdriver.Chrome):
        self.driver:webdriver.Chrome = driver
        
    """呼叫此函式需可最大化當前控制的瀏覽器"""
    def maximize_window(self):
        "最大化視窗"
        self.driver.maximize_window()
        
    """呼叫此函式需可最小化當前控制的瀏覽器"""
    def minimize_window(self):
        "最小化視窗"
        self.driver.minimize_window()

    """呼叫此函式可以將視窗移到所需的位置"""
    def move_window(self, x, y):
        "移動視窗到x, y上"
        self.driver.set_window_position(x, y)

    """呼叫此函式並於參數位置放入URL，連結至目標網頁"""
    def enter_target_page(self, url):
        "進入目標網頁"
        self.driver.get(url)
        self.all_page_wait()
    
    """呼叫此函式可以關閉當前控制的瀏覽器"""
    def close_webpage(self):
        "關閉網頁"
        self.driver.close()
    
    """呼叫此函式需可重整當前控制的瀏覽器"""
    def reload_webpage(self):
        "重載網頁"
        self.driver.refresh()
        self.all_page_wait()
    
    """呼叫此函式並從參數代入元件的Path，可在當前瀏覽器
    頁面上定位到相對應的元件"""
    def get_element(self, element):
        "取得元素"
        try:
            self.element_wait(element, 3)
            return self.driver.find_element(By.XPATH, element)
        except:
            ExceptionHandler(msg= "Cannot get the target element. 無法獲取目標元件。\n", exceptionLevel= "error")
            raise
    
    """呼叫此函式並從參數代入元件的Path，可在當前瀏覽器
    頁面上定位到相對應的元件列表，並給定另一參數指定要從
    列表中取第幾個index的元件"""
    def get_elements(self, element):
        "取得元素列"
        try:
            self.elements_wait(element, 3)
            return self.driver.find_elements(By.XPATH, element)
        except:
            ExceptionHandler(msg= "Cannot get the target element. 無法獲取目標元件。\n", exceptionLevel= "error")
            raise

    
    """呼叫此函式並從參數代入定位到的元件，可以對該元件
    做點擊的動作"""
    def element_click(self, getElement: get_element or get_elements):
        "點擊元素"
        try:
            getElement.click()
        except:
            ExceptionHandler(msg= "Cannot click the element. 無法點擊該元件。\n", exceptionLevel= "error")
            raise
    
    """呼叫此函式並從參數代入定位到的元件，可以對該元件
    做輸入的動作，並給定另一參數指定可以輸入什麼"""
    def element_send_keys(self, getElement: get_element or get_elements, content):
        "傳遞值給元素"
        try:
            getElement.send_keys(content)
        except:
            ExceptionHandler(msg= "Cannot send the target key to the element. 無法傳送目標值至該元件。\n", exceptionLevel= "error")
            raise
    
    """呼叫此函式並從參數代入欲定位的元件要等待多久時間載入"""
    def element_wait(self, element, time: int):
        "等待元素"
        try:
            WebDriverWait(self.driver, time).until(EC.element_to_be_clickable((By.XPATH, element))) 
        except:
            # logging.error(msg= "Time Out! Cannot locate the eleement. 時間到！無法定位到該元件。\n", exc_info= True)
            ExceptionHandler(msg= "Time Out! Cannot locate the element. 時間到！無法定位到該元件。\n", exceptionLevel= "error")
            raise
    
    """呼叫此函式並從參數代入欲定位的元件列表要等待多久時間載入"""
    def elements_wait(self, elements, time: int):
        "等待元素列"
        try:
            WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located((By.XPATH, elements))) 
        except:
            ExceptionHandler(msg= "Time Out! Cannot locate the element. 時間到！無法定位到該元件。\n", exceptionLevel= "error")
            raise
        
    """等待整個頁面載入完畢"""
    def all_page_wait(self):
        "整個頁面載入"
        self.driver.implicitly_wait(30)

    def switch_window(self, index):
        self.driver.switch_to.window(self.driver.window_handles[index])

    """控制警告視窗"""
    def switch_alert(self):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()

    "特例"
    def subElement_get(self, subDriver: webdriver.Chrome, element):
        try:
            self.all_page_wait()
            return subDriver.find_elements(By.XPATH, element)
        except:
            raise