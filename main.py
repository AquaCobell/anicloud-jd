import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyperclip
import yaml



def getEpisodes(link, episodes, counter2, toseason):
    
    
    driver.get(link)
    driver.maximize_window()
    time.sleep(1)
    counter = 1
    counter2 = 1
    episodes += 1
    toseason += 1
    
    while counter2 < toseason:
        time.sleep(1)
        driver.find_element_by_xpath('//*[@title="Staffel ' + str(counter2) +'"]').click()
        counter = 1
        while counter < episodes:
            time.sleep(1)
            driver.switch_to.window(driver.window_handles[1])
            site = '//*[@title="Staffel ' + str(counter2) +' Episode ' + str(counter) +'"]'
            try:
                driver.find_element_by_xpath(site).click()
            except:
                print(site + "not found, skipping")
            time.sleep(1)

            pyautogui.moveTo(960,540)
            
            a = driver.window_handles[1]
            driver.switch_to.window(a)

            if driver.execute_script("return window.pageYOffset;") < 100 :
                pyautogui.scroll(-750)

        
            time.sleep(1)
            #buttonlocation = pyautogui.locateCenterOnScreen('button.png')
            #print(buttonlocation)
            #pyautogui.moveTo(buttonlocation)
            test = driver.find_element_by_xpath('//div[@id="wrapper"]/div[2]/div[2]/div[3]/div[5]/ul/li/div/a/div')
            test2 = test.find_element_by_xpath('..')
            test3 = test2.get_attribute("href")
            driver.get(str(test3))
            
            #p= driver.window_handles[1]

            #pyautogui.middleClick()

            #c = driver.window_handles[2]
            #driver.switch_to.window(c)
            time.sleep(2)
            
            
            while "anicloud" in driver.current_url:
                print("CHAPTCHA")
                time.sleep(1)
                try:
                    #pyautogui.moveTo(pyautogui.locateOnScreen('chaptcha.png')) 
                    #pyautogui.leftClick()
                    time.sleep(5)
                except:
                    print("CAPTCHA SOLVE fehlgeschlagen")

            
   
            
            pyperclip.copy(driver.current_url)
            print(driver.current_url)
            driver.execute_script("window.history.go(-2)")
            
            #pyautogui.hotkey('ctrl', 'w')
            #driver.switch_to.window(p)
            time.sleep(1)
            pyautogui.scroll(+1000)
            
            counter+=1
        counter2+=1
try:
    config = open("config.yml")
    parseddata = yaml.load(config)
except:
    print("config.yml entweder falsch oder nicht existent")
    quit()

#print(parseddata.get("chromedriver"))
CHROMEDRIVER = parseddata.get(r"chromedriver")
#print(parseddata.get("extension"))
EXTENSION = parseddata.get(r"extension")

link = str(input("Link zur Serie:"))
episodes = int(input("Wieviel Folgen hat die Serie? [Ganzzahl]"))
counter2 = int(input("Von Staffel :"))
season = int(input("Bis Staffel :"))



chrome_options = Options() 
chrome_options.add_experimental_option("detach", True)

chrome_options.add_argument('--load-extension=' + EXTENSION)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=chrome_options,executable_path=CHROMEDRIVER)
driver.delete_all_cookies()
try:
    getEpisodes(link,episodes,counter2,season)
except:
    print("Ein Fehler ist aufgetreten. Überprüfe die config.yml und deine Eingaben")

#main_window = driver.current_window_handle










