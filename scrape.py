import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time

def scrape_website(website):
    print("Launching chrome browser....")

    # specify where our chrome driver is
    chrome_driver_path = "./chromedriver.exe" 
    # specify how the web driver should operate
    options = webdriver.ChromeOptions()
    # setup our actual driver
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        # use driver to get page source and return the html
        driver.get(website)
        print("Page loaded.....")
        html = driver.page_source
        time.sleep(10)

        return html
    finally:
        driver.quit()