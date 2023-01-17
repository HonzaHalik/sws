import sqlite3
values = [('19 850 000 Kč za nemovitost', 'včetně poplatků, včetně provize, včetně právního servisu', 'N6251', '29.09.2022', 'Cihlová')]
def write(values):
    try:
        conn = sqlite3.connect(fr"C:\Users\halik\OneDrive\Dokumenty\GitHub\sws\code\test2.db")
        cursor = conn.cursor()
        print(sqlite3.version)
        cursor.execute("""CREATE TABLE IF NOT EXISTS testtable (Celkova_cena, Poznamka_k_cene, ID_zakazky, Aktualizace, Stavba)""")
    except Exception as e:  # not Error as e
        print(e)
        #quit()
    print(f"values is {values}")
    print(f"len(values) is {len(values)}")
    print(f"len((values,)) is {len((values,))}")
    cursor.executemany("""INSERT INTO testtable (Celkova_cena, Poznamka_k_cene, ID_zakazky, Aktualizace, Stavba) VALUES (?, ?, ?, ?, ?)""", values) #Insert tuple of values
    conn.commit()
    conn.close()

write(values)