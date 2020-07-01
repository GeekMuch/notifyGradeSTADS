import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tqdm import tqdm

# Configure to your needs
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
url = 'https://sb.aau.dk/sb-ad/sb/index.jsp'
resLink = 'https://sb.aau.dk/sb-ad/sb/resultater/studresultater.jsp'
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
        driver.get('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
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
    
def loginSite(url):
    driver.get(url)
    
    u = driver.find_element_by_name('brugernavn')
    u.send_keys('USERNAME_HERE') # your STADS username 
    
    p = driver.find_element_by_name('adgangskode')
    p.send_keys(encoder()) # your STADS password
    p.send_keys(Keys.RETURN)
    
    oldCount(url)
    studResultater(url)



def studResultater(url):
    global refreshCounter
    global counter
    counter = 0
    kk = driver.get(resLink) # place
    a =  driver.find_elements_by_xpath('//*[@id="resultTable"]/tbody/tr[*]')
    
    countGrades(a)

    refreshCounter += 1
    checker(counter, driver, refreshCounter)

if __name__ == "__main__":
    loginSite(url)