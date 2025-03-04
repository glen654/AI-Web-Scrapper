import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
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

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    # getting rid of the style and script tags
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    # get all the text and seperated it with a new line
    cleaned_content = soup.get_text(separator="\n")
    # if \n character not seperatign anything if there's no text between it and the next thing then we're just gonna remove it
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content

# make the dom content up to 6000 batches
def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i: i + max_length] for i in range(0,len(dom_content),max_length)
    ]