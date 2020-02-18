import re
import selenium
import io
import requests
import bs4
import urllib.request
import urllib.parse
from selenium import webdriver
import csv
from selenium.webdriver.common.action_chains import ActionChains
import time
from _datetime import datetime
from selenium.webdriver.common.keys import Keys

options=webdriver.ChromeOptions()
options.headless=False
prefs={"profile.default_content_setting_values.notofications" :2}
options.add_experimental_option("prefs",prefs)
driver=webdriver.Chrome("/Users/jungsoopark/Desktop/Data_Analytics/Data\ Science\ Project/Air\ Quality\ Project/chromedriver")
driver.maximize_window()
time.sleep(5)
driver.get("https://www.tripadvisor.in/")
#driver.find_element_by_id("brand-quick-links-QuickLinkTileItem__link--1k5lE").click()
#driver.find_element_by_id("userId").send_keys(email)
#driver.find_element_by_id("pwd").send_keys(pswd)
time.sleep(20)
