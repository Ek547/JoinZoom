from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import Options




link=""#add zoom link here
chrome_options = Options()
chrome_options.add_argument("--disable-user-media-security=true")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()) , options=chrome_options)
driver.get(link)
time.sleep(10)
driver.quit
