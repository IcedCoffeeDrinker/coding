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

def spacer():
    spacer = ""
    for i in range(200):
        spacer += "-"
    print(spacer)

# --- locating elements from HTML --- #
# https://youtu.be/b5jt2bhSeXs

# ways to locate stuff:
# -id
# -class
# -name

driver.get("https://techwithtim.net")
print(driver.title)
time.sleep(2)

search = driver.find_element(by=By.NAME, value="s") # locates the inputline actually named s (text, id, name, tag_name, class_name, ...), (elemnent, elements)!!!!!!
search.send_keys("coding") # enters string
search.send_keys(Keys.RETURN) # return means enter

# finding search results:
try:
    main = WebDriverWait(driver, 10).until( # waiting max time of 10 seconds to load
        EC.presence_of_element_located((By.ID, "main")) # wait until page loaded and locates main (possible: NAME, CLASS_NAME, TAG_NAME, ID)
    )
    print(main.text) # printing all search results
    spacer()
    articles = main.find_elements(by=By.TAG_NAME, value="article") # printing all summarys from the results
    for article in articles:
        header = article.find_element(by=By.CLASS_NAME, value="entry-summary") # local summary --not working? i do't care, its 1am
        print(header.text)
except:
    for i in range(10):
        print("FAIL")
driver.get("https://techwithtim.net")
time.sleep(5)

spacer()

# --- press buttons & links --- #
link = driver.find_element(by=By.LINK_TEXT, value="Python Programming")
link.click() # clicks link and buttons
print("link klicked")

# again like with search above waiting for element to exist before clicking
try:
    element = WebDriverWait(driver, 10).until( # waiting max time of 10 seconds to load
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials")) # wait until page loaded and locates main (possible: NAME, CLASS_NAME, TAG_NAME, ID)
    )
    print("link succesfully loaded and clicked")
    element.click()
except:
    print("fail")

#driver.back() # goes one page back (having some error)
#driver.forward() # goes one page forward
driver.refresh() # refreshes site

spacer()

# --- quit --- #
time.sleep(10)
driver.close() # close tab
driver.quit() # closes browser
