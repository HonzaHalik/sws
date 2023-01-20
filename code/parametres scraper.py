from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import re
from selenium.webdriver.common.keys import Keys
import sqlite3
from sqlite3 import Error
import time


#TODO
    # replace all time.sleep with selenium code to wait for the page to load



db_file = fr"C:\Users\halik\OneDrive\Dokumenty\GitHub\sws\code\test.db"
url_byty = "https://www.sreality.cz/hledani/byty"
url_domy = "https://www.sreality.cz/hledani/domy"

test_mode = True
sleep = 5

def start_sequence(url):
    # Set up the webdriver
    driver = webdriver.Chrome()
    # create a new Chrome browser instance in headless mode
    options = webdriver.ChromeOptions()
    if not test_mode:
        options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=options)
    # Navigate to the URL
    driver.get(url)
    # Wait for the page to load
    time.sleep(sleep)
    # Find the button with the specified CSS class and click it
    button = driver.find_element(By.CSS_SELECTOR, ".praha .tspan")
    button.click()
    #click show ... flats button
    button = driver.find_element(By.CSS_SELECTOR, "#page-layout > div.content-cover > div.content-inner > div.transcluded-content.ng-scope > div > div > div.filter.ng-scope > form > div.buttons.ng-scope > div > div > button")
    button.click()
    
    return driver

def get_data(driver, url):
    byty_xpaths = []
    for byt in range(1, 21):
        load(driver, f'//*[@id="page-layout"]/div[2]/div[3]/div[3]/div/div/div/div/div[3]/div/div[{byt}]/div/div/span/h2/a/span', 5)
        button = driver.find_element(By.XPATH,f'//*[@id="page-layout"]/div[2]/div[3]/div[3]/div/div/div/div/div[3]/div/div[{byt}]/div/div/span/h2/a/span')
        button.click()
        load(driver, '/html/body/div[2]/div[1]/div[2]/div[3]/div[3]/div/div/div/div/div[7]', 5)
        tabulka = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[3]/div[3]/div/div/div/div/div[7]').text
        tabulka_list = tabulka.splitlines()
        parametry = ["Celková cena:", "Poznámka k ceně:", "ID zakázky:", "Aktualizace:", "Stavba:", "Stav objektu:", "Vlasnictví:", "Podlaží:", "Užitná plocha:", "Plocha podlahová:", "Plocha zahrady:", "Balkón:", "Terasa:", "Sklep:", "Parkování:", "Garáž:", "Datum nastěhování:", "Voda:", "Topení:", "Plyn:", "Telekomunikace:", "Doprava:", "Komunikace:", "Energetická náročnost budovy:", "Bezbariérový:","Vybavení:", "Výtah:"]
        hodnoty = [None]*27
        i = 0
        for parametr in parametry:
            i = 0
            for i in range(len(tabulka_list)):    #loops over lines in the table until it finds the correct parametr or loops over the entire table
                row = tabulka_list[i]
                if parametr in row: #checks if the desired parametr is in the line of the table then extracts the value and breaks the loop
                    hodnota = row[len(parametr) : ]
                    break
                else:
                    hodnota = None
                    
            hodnoty[parametry.index(parametr)] = hodnota
            print(f'{parametr} je {hodnota}')
        write(hodnoty)
        driver.back()  

        
def load(driver, xpath, tries):#waits for specified xpath to load if it doesnt in the tries specified returns False, returns True when element loads
    wait = 1
    try:
        myElem = WebDriverWait(driver, wait).until(EC.presence_of_element_located((By.XPATH, xpath)))
        print("page loaded")
    except TimeoutException:
        print("timed out")

def write(values):
    try:
        conn = sqlite3.connect(fr"C:\Users\halik\OneDrive\Dokumenty\GitHub\sws\code\test3.db")
        cursor = conn.cursor()
        print(sqlite3.version)
        cursor.execute("""CREATE TABLE IF NOT EXISTS test (cena, Poznámka, ID, Aktualizace, Stavba, Stav, Vlasnictví, Podlaží, Užitná, podlahová, zahrada, Balkón, Terasa, Sklep, Parkování, Garáž, nastěhování, Voda, Topení, Plyn, Telekomunikace, Doprava, Komunikace, Energetika, Bezbariérový, Vybavení, Výtah)""")
    except Exception as e:  # not Error as e
        print(e)
        #quit()
    cursor.executemany("""INSERT INTO test VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (values,)) #Insert tuple of values
    conn.commit()
    conn.close()
    print("dataze aktualizovana")
    
def main():
    driver = start_sequence(url_byty)
    get_data(driver, url_byty)
    driver.quit()

if __name__ == "__main__":
    main()









