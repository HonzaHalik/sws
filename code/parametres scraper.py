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
    # linearni regrese model pro zavislost poctu nabidek na repo sazbe, inflaci
    # pro presnost brat pocet nabidek z katastru / https://www.cuzk.cz/Katastr-nemovitosti/Statisticke-udaje-o-transakcich/Statisticke-udaje-o-vybranych-transakcich-s-ne-(1).aspx



db_file = fr"C:\Users\halik\OneDrive\Dokumenty\GitHub\sws\code\test.db"
url_byty = "https://www.sreality.cz/hledani/byty"
url_domy = "https://www.sreality.cz/hledani/domy"

test_mode = True
sleep = 5

def start_sequence(url):
    # Set up
    driver = webdriver.Chrome()
    # pokud !test_mode tak otevre headles chrome
    options = webdriver.ChromeOptions()
    if not test_mode:
        options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=options)
    # jde na url
    driver.get(url)
    # ceka
    time.sleep(sleep)
    # klikne na prahu
    button = driver.find_element(By.CSS_SELECTOR, ".praha .tspan")
    button.click()
    #clickne ukazat ... nabidek
    button = driver.find_element(By.CSS_SELECTOR, "#page-layout > div.content-cover > div.content-inner > div.transcluded-content.ng-scope > div > div > div.filter.ng-scope > form > div.buttons.ng-scope > div > div > button")
    button.click()
    
    return driver

def get_data(driver, url):
    byty_xpaths = []
    for byt in range(1, 20):
        flag = False
        load(driver, f'//*[@id="page-layout"]/div[2]/div[3]/div[3]/div/div/div/div/div[3]/div/div[{byt}]/div/div/span/h2/a/span', 5)
        button = driver.find_element(By.XPATH,f'//*[@id="page-layout"]/div[2]/div[3]/div[3]/div/div/div/div/div[3]/div/div[{byt}]/div/div/span/h2/a/span')
        button.click()
        load(driver, '/html/body/div[2]/div[1]/div[2]/div[3]/div[3]/div/div/div/div/div[7]', 5)
        tabulka = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[3]/div[3]/div/div/div/div/div[7]').text
        tabulka_list = tabulka.splitlines()
        parametry = ["Celková cena:", "Poznámka k ceně:", "ID zakázky:", "Aktualizace:", "Stavba:", "Stav objektu:", "Vlasnictví:", "Podlaží:", "Užitná plocha:", "Plocha podlahová:", "Plocha zahrady:", "Balkón:", "Terasa:", "Sklep:", "Parkování:", "Garáž:", "Datum nastěhování:", "Voda:", "Topení:", "Plyn:", "Telekomunikace:", "Doprava:", "Komunikace:", "Energetická náročnost budovy:", "Bezbariérový:","Vybavení:", "Výtah:"]
        hodnoty = [None]*27
        parametry_cisla = ["Celková cena:", "Užitná plocha:", "Plocha podlahová:", "Plocha zahrady:", "Balkón:", "Terasa:", "Sklep:"]
        nutne_parametry = ["Celková cena:", "Užitná plocha:", "Podlaží:"]
        i = 0
        for parametr in parametry:
            i = 0
            for i in range(len(tabulka_list)): # hleda hodnotu v kazdem radku tabulky
                row = tabulka_list[i]
                if parametr in row: #pokud je hodnota v radku tak ji zaznamena a prestane ji hledat
                    hodnota = row[len(parametr) : ]
                    break
                else:
                    hodnota = None
            if parametr in parametry_cisla and hodnota != None: # meni 42m2 na 42
                hodnota = hodnota.strip()
                hodnota = hodnota.replace('m2', '')
                hodnota = re.sub(r'[^0-9]', '', hodnota)
            if parametr == "Podlaží:" and hodnota != None: #meni 2. podlazi z celkem 7 na jenom 2
                hodnota = hodnota.strip()
                hodnota_list = hodnota.split(".")
                hodnota = hodnota_list[0]
            if not (parametr in nutne_parametry and hodnota == None): #krome bytu bez ceny, plochy, nebo podlazi vsechny zapise jinak pokracuje na dalsi
                hodnoty[parametry.index(parametr)] = hodnota
                print(f'{parametr} je {hodnota}')
            else: 
                print("cena nebo plocha nebo podlazi nejsou dostupne")
                flag = True #pokud flag tak jde na dalsi byt 
        if flag:# pokud flag tak jde na dalsi byt
            print("flag")
            driver.back()
            # jde na dalsi byt protoze tenhle nema cenu
        else:
            write(hodnoty) # zapise hodnoty
            driver.back() # vrati se na nabidku bytu aby mohl jit na dalsi

def load(driver, xpath, tries): # nekolikrat zkontroluje dostupnost elementu pokud neni dostuny tak si stezuje
    wait = 5
    try:
        myElem = WebDriverWait(driver, wait).until(EC.presence_of_element_located((By.XPATH, xpath)))
        print("page loaded")
    except TimeoutException:
        print("timed out")


def write(values):
    try:
        conn = sqlite3.connect(fr"C:\Users\halik\OneDrive\Dokumenty\GitHub\sws\code\parametry4.db")
        cursor = conn.cursor()
        print(sqlite3.version)
        cursor.execute("""CREATE TABLE IF NOT EXISTS tabulka (cena, Poznámka, ID, Aktualizace, Stavba, Stav, Vlasnictví, Podlaží, Užitná, podlahová, zahrada, Balkón, Terasa, Sklep, Parkování, Garáž, nastěhování, Voda, Topení, Plyn, Telekomunikace, Doprava, Komunikace, Energetika, Bezbariérový, Vybavení, Výtah)""")
    except Exception as e:  # not Error as e
        print(e)
        #quit()
    cursor.executemany("""INSERT INTO tabulka VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (values,)) #Insert tuple of values
    conn.commit()
    conn.close()
    print("dataze aktualizovana")
    
def main():
    driver = start_sequence(url_byty)
    get_data(driver, url_byty)
    driver.quit()

if __name__ == "__main__":
    main()









