from playsound import playsound
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from src.bot import BestBuyBot, AmazonBot, MicrosoftBot


CVV = "957"

# This is the URL of the products
AMAZON_PRODUCT_URL = "https://www.amazon.ca/Playstation-3005721-PlayStation-Digital-Edition/dp/B08GS1N24H"

# This is the expected prices of the product. ( For avoiding resellers)
AMAZON_EXPECTED_PRICES = [499.99, 529.99, 539.99, 519.99]


def check_availability_all(bots):
    done = False
    while done is False:
        for bot in bots:
            result = bot.check_availability_and_buy()
            if result is True:
                done = True
                print("WOOOOOOOOOOOHOOOOOOOOOOOOOO!!!!!!!!!!!!!!!!")
                break
    for _ in range(100):
        playsound(r'src/beep.mp3')
    input("....")
    exit(0)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Setting up the driver
    print("Hey! I am the Automatic Order Bot! BestBuy, Amazon. Let's get started..\n")
    opts = Options()
    opts.add_argument("--remote-debugging-port=9222")
    EXEC_PATH = r"src/chromedriver"
    DRIVER = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe", options=opts)

    amazon_bot = AmazonBot(AMAZON_PRODUCT_URL, CVV, DRIVER, AMAZON_EXPECTED_PRICES)
    bots_c = [amazon_bot]
    amazon_bot.amazon_login()
    check_availability_all(bots_c)
