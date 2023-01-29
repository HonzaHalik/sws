import sqlite3
try:
    conn = sqlite3.connect(fr"C:\Users\halik\OneDrive\development\github\sws\code\parametry6.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS tabulka (cena, Poznámka, ID, Aktualizace, Stavba, Stav, Vlasnictví, Podlaží, Užitná, podlahová, zahrada, Balkón, Terasa, Sklep, Parkování, Garáž, nastěhování, Voda, Topení, Plyn, Telekomunikace, Doprava, Komunikace, Energetika, Bezbariérový, Vybavení, Výtah)""")
except Exception as e:  
    print(e)
    quit()
else:
    cursor.execute("""DELETE FROM nutneParametry WHERE rowid = 20;""")