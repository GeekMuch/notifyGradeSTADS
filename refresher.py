import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tqdm import tqdm

# Configure your preferred browsers path. 
# REMEBER TO DOWNLOAD THE BROWSER DRIVER, LINK BELOW
# https://www.selenium.dev/documentation/en/webdriver/driver_requirements/
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

# Link for the login page
url = 'https://sb.aau.dk/sb-ad/sb/index.jsp'

# Link for STADS results
resLink = 'https://sb.aau.dk/sb-ad/sb/resultater/studresultater.jsp'

# YouTube link for the video 
ytVideo = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

# Login information
username = 'BRUGERNAVN_HER'
password = 'ADGANGSKODE_HER'

# Global variables 
refreshCounter = 0
oldCounter = 0
counter = 0

# Password decoder from binary to ASCII
def encoder():
    binary_int = int("101010", 2)
    byte_number = binary_int.bit_length() + 7 // 8

    binary_array = binary_int.to_bytes(byte_number, "big")
    ascii_text = binary_array.decode()

    return ascii_text

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def checker(counter, driver, refreshCounter):
    global oldCounter
    timer = 420

    if counter > oldCounter:
        driver.get(ytVideo)
        w = driver.find_element_by_xpath("//*[@class='ytp-large-play-button ytp-button']")
        w.click()
        print("\n\n[+] GRADE IS UP !\n\n")

    else:
        print("\nNumber of refresh: {0}\nNumber of courses: {1}".format(refreshCounter, counter))
        for char in tqdm(range(timer), unit='s', unit_divisor=60):
            time.sleep(1)
            #progress.set_description("Next refresh..") # 900 seconds = 15 minutes, 780s = 13 min
        driver.refresh()
        clear_screen()    
        studResultater(url)

def oldCount(url):
    global oldCounter

    res = driver.get(resLink)
    gradeList =  driver.find_elements_by_xpath('//*[@id="resultTable"]/tbody/tr[*]')
    
    oldCounter = countGrades(gradeList)

def countGrades(GradeList):
    global counter

    for x in GradeList:
        counter += 1

    return counter
    
def studResultater(url):
    global refreshCounter
    global counter
    counter = 0
    kk = driver.get(resLink) # place
    a =  driver.find_elements_by_xpath('//*[@id="resultTable"]/tbody/tr[*]')
    
    countGrades(a)

    refreshCounter += 1
    checker(counter, driver, refreshCounter)

def loginSite(url):
    driver.get(url)
    
    u = driver.find_element_by_name('brugernavn')
    u.send_keys(username) # your STADS username 
    
    p = driver.find_element_by_name('adgangskode')
    p.send_keys(password) # your STADS password
    p.send_keys(Keys.RETURN)

    error = driver.find_elements_by_class_name('ErrorText')

    if 'Forkert' in error[0].text:
        print('\n[x] Error in login \n')
        sys.exit(0) 
    else:
        oldCount(url)
        studResultater(url)

if __name__ == "__main__":
    loginSite(url)