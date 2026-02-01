Data Split:-
from sklearn.model_selection import train_test_split

X = df[['Age', 'Pclass']]
y = df['Fare']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

Linear Regression Model:-

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("titanic.csv")

# Handle missing values
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Fare'] = df['Fare'].fillna(df['Fare'].median())

# Feature and target
X = df[['Age']]
y = df['Fare']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Regression line
y_pred = model.predict(X)

# Plot
plt.figure()
plt.scatter(df['Age'], df['Fare'])
plt.plot(df['Age'], y_pred)
plt.xlabel("Age")
plt.ylabel("Fare")
plt.title("Linear Regression: Age vs Fare")
plt.show()

Model Evaluation:-
#Predictions---
y_pred = model.predict(X_test)
#Mean Squared Error (MSE)-----
from sklearn.metrics import mean_squared_error, r2_score

mse = mean_squared_error(y_test, y_pred)
mse

OUTPUT:-
0.146

#R² Score------
r2 = r2_score(y_test, y_pred)
r2
OUTPUT:-
0.39
Interpretation of Metrics:-
Lower MSE (0.146) 
R² = 0.39- 39% of variance

Interpretation And Conclusion:-

coefficients = pd.DataFrame({
    'Feature': X.columns,
    'Coefficient': model.coef_
})
coefficients

OUTPUT:-
SI  Feature   Coefficient
0  Pclass      -0.18
1  Age         -0.04
2  Fare         0.002
3  SibSp       -0.03
4  Parch        0.01


