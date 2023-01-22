import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


def linear_regresion(x):
    return slope * x + intercept

df = pd.read_csv(fr"C:\Users\halik\OneDrive\Dokumenty\GitHub\sws\code\repo.csv")

print(df)
x = df["nove"]
y = df["repo"]
print(df.corr()['repo'])
plt.scatter(x, y)
slope, intercept, r, p, std_err = stats.linregress(x, y)
mymodel = list(map(linear_regresion, x))
plt.scatter(x, y)
plt.plot(x, mymodel)
print(f"r*r je {r*r}")
plt.show()
