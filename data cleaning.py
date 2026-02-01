DATA CLEANING:-

import pandas as pd

# Load dataset
df = pd.read_csv("titanic.csv")

# View first 5 rows
df.head()

SI   PassengerId  Survived  Pclass     Sex      Age     SibSp   Parch     Fare    Embarked
0          1         0       3         male     22.0      1      0       7.25        S
1          2         1       1        female    38.0      1      0       71.28       C
2          3         1       3        female    NaN       0      0       7.92        S
3          4         1       1        female    35.0      1      0       53.10       S
4          5         0       3        male      NaN       0      0       8.05        S

Check Missing Values:-
df.isnull().sum()

OUTPUT:-
PassengerId      0
Survived         0
Pclass           0
Sex              0
Age            177
SibSp            0
Parch            0
Fare             1
Embarked         2
dtype: int64

Handle Missing Values:-
#Fill Age with mean-------
df['Age'] = df['Age'].fillna(df['Age'].mean())

#Fill Fare with median------
df['Fare'] = df['Fare'].fillna(df['Fare'].median())

#Fill Embarked with mode (most frequent value)-------
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

Missing Values After Cleaning:-
df.isnull().sum()

OUTPUT:-
PassengerId    0
Survived       0
Pclass         0
Sex            0
Age            0
SibSp          0
Parch          0
Fare           0
Embarked       0
dtype: int64

Here all the missing values are removed succesfully

Final Cleaned Dataset:-
df.head()

OUTPUT:-
SI   PassengerId  Survived  Pclass     Sex       Age     SibSp  Parch   Fare      Embarked
0         1         0       3          male      29.7      1      0      7.25        S
1         2         1       1          female    38.0      1      0      71.28       C
2         3         1       3          female    29.7      0      0      7.92        S
3         4         1       1          female    35.0      1      0      53.10       S
4         5         0       3          male      29.7      0      0      8.05        S

Final Summary:- 
1)Identifying missing values using isnull().sum()
2)Filled numerical columns using mean / median
3)Filled categorical columns using mode
4)Hence the data set verified




