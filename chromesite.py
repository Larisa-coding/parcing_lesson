from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time
import random

browser = webdriver.Chrome()

browser.get("https://en.wikipedia.org/wiki/Document_Object_Model")
time.sleep(5)
browser.save_screenshot("dom.png")
time.sleep(3)

browser.get("https://ru.wikipedia.org/wiki/Selenium")
time.sleep(5)
browser.save_screenshot("selenium.png")
time.sleep(3)

browser.refresh()
time.sleep(5)

browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
assert "Википедия" in browser.title
time.sleep(5)

search_box = browser.find_element(By.ID, "searchInput")
search_box.send_keys("Солнечная система")
search_box.send_keys(Keys.RETURN)
time.sleep(5)

a = browser.find_element(By.LINK_TEXT, "Солнечная система")
a.click()
time.sleep(5)

paragraphs = browser.find_elements(By.TAG_NAME, "p")
for paragraph in paragraphs:
    print(paragraph.text)
    input("Нажмите Enter для следующего параграфа...")

hatnotes = []
for element in browser.find_elements(By.TAG_NAME, "div"):
    cl = element.get_attribute("class")
    if cl == "hatnote navigation-not-searchable":
        hatnotes.append(element)

if hatnotes:
    hatnote = random.choice(hatnotes)
    link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
    browser.get(link)
    time.sleep(5)

browser.quit()
