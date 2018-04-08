from selenium import webdriver 
import sys

import requests
import bs4
import re
from selenium.webdriver.support.ui import WebDriverWait

# Find Email 
# match = emailRegex.findall(soup.text)

# Doesn't use in script. Just a simple regex command to strip emails from text
def searchForEmails(string):

    emailRegex = re.compile(r'[\w\.-]+@[\w\.-]+') 
    match = emailRegex.findall(string)
    print(match)
    return(match)


def GetEmail():
    browser = webdriver.Firefox()
    # browser.get("https://www.fakemailgenerator.com")

    browser.get('https://www.fakemailgenerator.com')
    browser.wait = WebDriverWait(browser, .5)

    browser.execute_script("window.stop();")
    browser.execute_script("window.stop();")

    element = browser.find_element_by_css_selector('#cxtEmail')
    print(element.text)
    browser.close()

count = int(input("How many emails would you like?:   "))
for i in range(count):
    GetEmail()

# browser.close()









