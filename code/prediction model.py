from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import pandas

df = pandas.read_csv(fr"C:\Users\halik\OneDrive\Dokumenty\GitHub\sws\code\data.csv")
# Prepare your data
X = df[["repo"]] # input feature
y = df['aktivni'] # output variable

# Create an instance of the PolynomialFeatures class with a degree of 2
poly = PolynomialFeatures(degree=2)

# Transform the input feature to include polynomial terms
X_poly = poly.fit_transform(X)

# Create an instance of the LinearRegression class
reg = LinearRegression()

# Fit the model to the data
reg.fit(X_poly, y)

# Make predictions
y_pred = reg.predict(X_poly)
print(y_pred)