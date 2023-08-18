from selenium import webdriver
from selenium.webdriver.common.keys import Keys # needed far typing special keys
import time
# needet to wait for loading page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedriver.exe" # path to chromedriver
driver = webdriver.Chrome(PATH)

driver.get("https://amazon.de")

# settings
user_name = "philipp.haus@icloud.com"
password = "Hamburg2016"

# functions
def press(content):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, content))
        )
        print("link succesfully loaded and clicked")
        element.click()
    except:
        print("fail")

def enter(content, input):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, content))
        )
        element.send_keys(input)
        element.send_keys(Keys.RETURN)
    except:
        print("fail")

# anmelden:
press("Anmelden")
enter("ap_email", user_name)
enter("ap_password", password)
time.sleep(5)
driver.get("https://www.amazon.de/hz/wishlist/ls/ref=nav_wishlist_lists_1")

# quit
wait = input("press enter to continue: ")
driver.close()
driver.quit()
