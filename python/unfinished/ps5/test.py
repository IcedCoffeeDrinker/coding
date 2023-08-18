from selenium import webdriver
from selenium.webdriver.common.keys import Keys # needed far typing special keys
import time
# needet to wait for loading page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedriver.exe" # path to chromedriver
driver = webdriver.Chrome(PATH)

driver.get("http://much.epic-sushi.de") # open website

print(driver.title) # website name

# --- locating elements from HTML --- #
# https://youtu.be/b5jt2bhSeXs

# ways to locate stuff:
# -id
# -class
# -name

driver.get("https://techwithtim.net")
print(driver.title)
time.sleep(2)

search = driver.find_element_by_name("s") # locates the inputline actually named s (text, id, tag_name, class_name, ...)
search.send_keys("coding") # enters string
search.send_keys(Keys.RETURN) # return means enter

# finding search results:

articles = main.find_element_by_tag_name("article") # printing all summarys from the results
for article in articles:
    header = article.find_element_by_class_name("entry-summary") # local summary --not working? i do't care, its 1am
    print(header.text)
time.sleep(10)

spacer = ""
for i in range(20):
    spacer += "-"
print(spacer)

# --- press buttons & links --- #
link = driver.find_element_by_text("Python Programming")

# --- quit --- #
time.sleep(10)
driver.close() # close tab
driver.quit() # closes browser
