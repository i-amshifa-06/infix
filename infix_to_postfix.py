import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import r2_score, accuracy_score

# Load dataset (Pima Indians Diabetes dataset)
df = pd.read_csv("diabetes.csv")

# --------- Linear Regression (BMI → Glucose) ---------
X = df[['BMI']]
y = df['Glucose']

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

lr = LinearRegression()
lr.fit(x_train, y_train)
pred1 = lr.predict(x_test)

print("Linear Regression R² Score:", r2_score(y_test, pred1))

# --------- Logistic Regression (Glucose → Diabetes Outcome) ---------
X = df[['Glucose']]
y = df['Outcome']

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

logr = LogisticRegression()
logr.fit(x_train, y_train)
pred2 = logr.predict(x_test)

print("Logistic Regression Accuracy:", accuracy_score(y_test, pred2))