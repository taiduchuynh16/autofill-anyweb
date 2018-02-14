from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def page_is_loaded(driver):
    return driver.find_element_by_tag_name("body") != None

for e in range(3):

    chrome_options = Options()
    chrome_options.add_argument("--disable-infobars")

    driver = webdriver.Chrome()
    driver.get("https://airdrop.havven.io/?kid=KX2B4")

    wait = ui.WebDriverWait(driver, 10)
    wait.until(page_is_loaded)

    firstname = driver.find_element_by_name("first_name")
    firstname.send_keys("xxxxxxx")

    lastname = driver.find_element_by_name("last_name")
    lastname.send_keys("xxxxxxx")

    mail = driver.find_element_by_name("email")
    mail.send_keys("xxxxxxx@gmail.com")

    teleid = driver.find_element_by_name("telegram")
    teleid.send_keys("xxxxxxx@gmail.com")

    for x in range(0,20):
        location_field = driver.find_element_by_name("country_of_residence")
        for option in location_field.find_elements_by_tag_name('country_of_residence'):
            if option.text == 'Argentina':
                option.click()
                break

    wallet = driver.find_element_by_name("eth_wallet_address")
    wallet.send_keys("0xEB525E43969DE00EbfDafFc5D6a91143F5b385b0")

    teleid = driver.find_element_by_name("cryptocurrency_exchange")
    teleid.send_keys("Coinbase")

    location_field = driver.find_element_by_id("how_did_you_hear_about_us_0")
    location_field.click()