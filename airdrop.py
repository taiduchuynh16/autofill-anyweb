from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys

def page_is_loaded(driver):
    return driver.find_element_by_tag_name("body") != None

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

for x in range(0,7):
    location_field = driver.find_element_by_name("how_did_you_hear_about_us")
    for option in location_field.find_elements_by_tag_name('option'):
        if option.text == 'CoinMarketCap.com':
            option.click()
            break

driver.find_element_by_xpath("//input[@value='Signup Now!']").click()
