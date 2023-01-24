import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy
from sklearn.metrics import r2_score
from sklearn import linear_model

df = pd.read_csv(fr"C:\Users\halik\OneDrive\Dokumenty\GitHub\sws\code\repo.csv")
def linear_regresion(x):
    return slope * x + intercept

def draw_poly_regresion(df):
    x = df["repo"]/100
    y = df["cena"]
    mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
    plt.scatter(x, y)
    myline = numpy.linspace(0, 7, 100)
    plt.scatter(x, y)
    plt.plot(myline, mymodel(myline))
    print(f"r*r pro poly regresi je {r2_score(y, mymodel(x))}")
    plt.show()

def correlation(df):
    print(df.corr()['repo'])

def draw_linear_regresion(df):
    x = df["repo"]/100
    y = df["cena"]
    plt.scatter(x, y)
    mymodel = list(map(linear_regresion, x))
    plt.plot(x, mymodel)
    print(f"r*r pro linearni regresi je {r*r}")
    plt.show()
    
def multiple_regresion(df):
    X = df[["repo", "aktivni"]]
    y = df["aktivni"]
    regr = linear_model.LinearRegression()
    regr.fit(X, y)
    aktivni_predikce = regr.predict([[700,202206]])
    print(aktivni_predikce)


def predict(df, model):
    print(df)
    x = df["repo"]/100
    y = df["cena"]
    print(f"predpovidana cena m2 je {linear_regresion(7)}")

df = pd.read_csv(fr"C:\Users\halik\OneDrive\Dokumenty\GitHub\sws\code\repo.csv")
x = df["repo"]/100
y = df["cena"]
plt.scatter(x, y)
slope, intercept, r, p, std_err = stats.linregress(x, y)

def main():
    #correlation(df)
    #predict(df)
    draw_poly_regresion(df)
    #multiple_regresion(df)
    #draw_linear_regresion(df)

main()