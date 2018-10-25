# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 11:42:27 2018

@author: shaival
"""

from selenium import webdriver
import random
import time

def get_quote(driver, choice):
    driver.get("http://www.quoteland.com/topic.asp")

    choices={
            1:'Motivational Quotes',
            2:'Love Quotes',
            3:'Inspirational Quotes',
            4:'Determination Quotes',
            5:'Poetry Quotes',
            6:'Teamwork Quotes',
            7:'Sports Quotes'
    }
    driver.find_element_by_link_text(choices[choice]).click()
    #choices[2].click()
    time.sleep(1)
    quotes=driver.find_elements_by_xpath('//*[@face="verdana,arial,helvetica"]')
    #next_25=driver.find_elements_by_xpath('//*[contains(text(), "Next 25 >>")]')
    c=True
    l=[]
    while(c):
        #next_25=driver.find_elements_by_xpath('//*[contains(text(), "Next 25 >>")]')
        quotes=driver.find_elements_by_xpath('//*[@face="verdana,arial,helvetica"]')
        i=0
        while((i*3 + 6) < len(quotes)):
            if(quotes[i*3 + 6].text == 'Rate this Quote!'):
                l.append(quotes[i*3 + 5].text)
            i+=1
            
        #if(len(next_25)!=0):
            #next_25[0].click()
        #else:
        c = False
    
    
    c = random.randint(0,len(l))
    
    return l[c]
    


if __name__ == "__main__":
    print("Enter choice:")
    choices = ['motivational', 'love', 'inspirational', 'determination', 'poetry', 'teamwork', 'sports']
    for i, choice in enumerate(choices):
        print(str(i+1)+": Get "+choice+" quotes")
        
    choice = input("Enter choice number: ")
    driver = webdriver.Chrome()
    print(get_quote(driver, int(choice)))