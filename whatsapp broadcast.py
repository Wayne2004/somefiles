import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from os import system
from io import BytesIO
from selenium.webdriver.chrome.service import Service as ChromeService # Similar thing for firefox also!
from subprocess import CREATE_NO_WINDOW # This flag will only be available in windows
from PIL import Image
import win32clipboard
import pyperclip

def whatsapbroadcast():
    clear = lambda: system('cls')
    mobile_emulation = {
                    "deviceMetrics": {"width": 1000, "height": 620, "pixelRatio": 1.0},

                    "userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    #"Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile Safari/535.19"
    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    chrome_options.add_argument("--disable-notifications")
    chrome_service = ChromeService(r"C:\Users\wayne\AppData\Local\Programs\AutoBroadcaster\chromedriver.exe")
    chrome_service.creationflags = CREATE_NO_WINDOW
    driver = webdriver.Chrome(r"C:\Users\wayne\AppData\Local\Programs\AutoBroadcaster\chromedriver.exe", options=chrome_options, service=chrome_service)
    driver.set_window_size(1050, 810)
    driver.get("https://web.whatsapp.com/")
    input()




whatsapbroadcast()

