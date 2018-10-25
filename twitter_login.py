# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 11:39:23 2018

@author: shaival
"""

from selenium import webdriver

def login_twitter(driver, username, password):
    
    driver.get("https://twitter.com/login")

    user = driver.find_element_by_class_name("js-username-field")
    pwd = driver.find_element_by_class_name("js-password-field")

    user.send_keys(username)
    driver.implicitly_wait(1)
    
    pwd.send_keys(password)
    driver.implicitly_wait(1)

    driver.find_element_by_class_name("EdgeButtom--medium").click()
    return driver

if __name__ == "__main__":
    username = 'shaival290597@gmail.com'
    password = 'bestsrs@29'
    driver = webdriver.Chrome()
    login_twitter(driver, username, password)
    