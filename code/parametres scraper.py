from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
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

def start_sequence(db, url):
    #connect to the database
    conn = None
    cursor = None
    try:
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        print(sqlite3.version)
        cursor.execute('''CREATE TABLE IF NOT EXISTS test14 ("Celková cena:", "Poznámka k ceně:", "ID zakázky:", "Aktualizace:", "Stavba:", "Stav objektu:", "Vlasnictví:", "Podlaží:", "Užitná plocha:", "Plocha podlahová:", "Plocha zahrady:", "Balkón:", "Terasa:", "Sklep:", "Parkování:", "Garáž:", "Datum nastěhování:", "Voda:", "Topení:", "Plyn:", "Telekomunikace:", "Doprava:", "Komunikace:", "Energetická náročnost budovy:", "Bezbariérový:","Vybavení:", "Výtah:")''')
    except Error as e:        #                              1                      2               3             4                 5            6             7              8                  9             10                    11               12        13       14         15             16     17                     18        19        20           21             22              23                    24                         25           26        27 
        print(e)
        quit()
    
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
    
    return driver, conn, cursor

def get_data(driver, url):
    for i in range(5):
        if driver.find_elements(By.XPATH,'//*[@id="page-layout"]/div[2]/div[3]/div[3]/div/div/div[1]/form/div[2]/div/div/button'):    
            button = driver.find_element(By.XPATH,'//*[@id="page-layout"]/div[2]/div[3]/div[3]/div/div/div[1]/form/div[2]/div/div/button')
            button.click()
            time.sleep(sleep)
            print("page loading")
    byty_xpaths = []
    for byt in range(1, 61):
        button = driver.find_element(By.XPATH, f'//*[@id="page-layout"]/div[2]/div[3]/div[3]/div/div/div/div/div[3]/div/div[{byt}]/div/div/span/h2/a/span')
        button.click()
        time.sleep(sleep)
        
        tabulka = driver.find_element(By.XPATH, '//*[@id="page-layout"]/div[2]/div[3]/div[3]/div/div/div/div/div[7]').text
        
        tabulka_list = tabulka.splitlines()
        
        parametry = ["Celková cena:", "Poznámka k ceně:", "ID zakázky:", "Aktualizace:", "Stavba:", "Stav objektu:", "Vlasnictví:", "Podlaží:", "Užitná plocha:", "Plocha podlahová:", "Plocha zahrady:", "Balkón:", "Terasa:", "Sklep:", "Parkování:", "Garáž:", "Datum nastěhování:", "Voda:", "Topení:", "Plyn:", "Telekomunikace:", "Doprava:", "Komunikace:", "Energetická náročnost budovy:", "Bezbariérový:","Vybavení:", "Výtah:"]
        hodnoty = []
        i = 0
        for parametr in parametry:
            i = 0
            for i in range(len(tabulka_list)):    #loops over lines in the table until it finds the correct parametr or loops over the entire table
                row = tabulka_list[i]
                print(f"v {row} hledam {parametr}")
                if parametr in row: #checks if the desired parametr is in the line of the table then extracts the value and breaks the loop
                    hodnota = row[len(parametr) : ]
                    break
                else:
                    hodnota = None
                    print("looping over table")
                    
            print(f'{parametr} je {hodnota}')
            hodnoty.append(hodnota)
            print(hodnoty)
            print(len(hodnoty))
        time.sleep(sleep*2)
        driver.back()           
        
        return hodnoty
        
def write(conn, cursor, hodnoty):
        "Celková cena:", "Poznámka k ceně:", "ID zakázky:", "Aktualizace:", "Stavba:", "Stav objektu:", "Vlasnictví:", "Podlaží:", "Užitná plocha:", "Plocha podlahová:", "Plocha zahrady:", "Balkón:", "Terasa:", "Sklep:", "Parkování:", "Garáž:", "Datum nastěhování:", "Voda:", "Topení:", "Plyn:", "Telekomunikace:", "Doprava:", "Komunikace:", "Energetická náročnost budovy:", "Bezbariérový:","Vybavení:", "Výtah:"
        celkova_cena, poznamka, id_zakazky, aktualizace, stavba, stav, vlasnictvi, podlazi, uzitna_plocha, plocha_podlahova, plocha_zahrady, balkon, terasa, sklep, parkovani, garaz, datum_nastehovani, voda, topeni, plyn, telekomunikace, doprava, komunikace, energeticka_narocnost, Bezbariérový, vybaveni, vytah = hodnoty
        
        cursor.executemany("INSERT INTO test14 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (hodnoty,))
        conn.commit()#                                 1 2  3  4 5   6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
        print("database updated")
def main():
    driver, conn, cursor = start_sequence(db_file, url_byty)
    hodnoty = get_data(driver, url_byty)
    write(conn, cursor, hodnoty)
    conn.close()
    driver.quit()

if __name__ == "__main__":
    main()









