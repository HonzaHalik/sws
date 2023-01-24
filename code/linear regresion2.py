import sqlite3
import pandas
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

#TODO



db_file = fr"C:\Users\halik\OneDrive\Dokumenty\GitHub\sws\code\parametry4.db"
def linear_regresion(x):
    return slope * x + intercept
def csv():
    conn = sqlite3.connect(db_file, isolation_level=None, detect_types=sqlite3.PARSE_COLNAMES)
    db_df = pd.read_sql_query("SELECT * FROM tabulka", conn)
    db_df.to_csv('parametrycsv.csv', index=False)

#csv()
df = pandas.read_csv(fr"C:\Users\halik\OneDrive\Dokumenty\GitHub\sws\parametrycsv.csv")
print(df)
x = df['cena']
y = df['Užitná']
plt.scatter(x, y) 
slope, intercept, r, p, std_err = stats.linregress(x, y) 
mymodel = list(map(linear_regresion, x))
plt.plot(x, mymodel)
print(f"r*r je {r*r}")
plt.show()


