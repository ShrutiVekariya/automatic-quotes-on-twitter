# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 18:59:27 2018

@author: shaival
"""

from twitter_login import login_twitter
from selenium import webdriver
from fetch_quotes import get_quote


username = 'shaival290597@gmail.com'
password = 'bestsrs@29'

print("Enter choice:")
choices = ['motivational', 'love', 'inspirational', 'determination', 'poetry', 'teamwork', 'sports']
for i, choice in enumerate(choices):
    print(str(i+1)+": Get "+choice+" quotes")
    
choice = input("Enter choice number: ")
driver2 = webdriver.Chrome()
quote = get_quote(driver2, int(choice))
print(quote)
print("Do you like this post? y/n")
if input() == 'n':
	quote = get_quote(driver2, int(choice))
print(quote)

driver = webdriver.Chrome()
driver = login_twitter(driver, username, password)

tweet = driver.find_element_by_name('tweet')
tweet.send_keys(quote)
driver.implicitly_wait(1)
driver.find_element_by_class_name('js-tweet-btn').click()
