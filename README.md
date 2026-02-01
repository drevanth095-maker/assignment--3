# assignment--3
📌Titanic Dataset – Linear Regression Analysis:-
The Assignment covers:
  1.Exploratory Data Analysis (EDA)
  2.Feature relationship analysis
  3.Train–test data split
  4.Linear Regression modeling
  5.Model evaluation
  6.Interpretation of regression coefficients
📂DATA CLEANING:-
  1.Missing values are checked and corrected it.
  2.Removed duplicates from the data set
📌Target Variable:
   Fare (continuous)
📌Input Features:
   Age
   Pclass
📌Exploratory Data Analysis (EDA):-
   1.Fare is strongly influenced by Pclass
   2.Passengers in 1st class paid significantly higher fares
   3.Age shows a weak relationship with Fare
   4.Correlation analysis revealed negative correlation between Pclass and Fare
📌Data Splitting:-
   1.Training set is divide  75%
   2.Testing set is divide 25%
📈 Linear Regression Model is trained by using the input features and the target variables and these solved by using Scikit-learn in python library
📊 Model Evaluation:-
The model was evaluated by using two Standard merices 
     1.Mean Squared Error (MSE) 
      Measures average squared difference between actual and predicted values
      Lower MSE indicates better model fit
     2.R² Score
      Represents proportion of variance explained by the model
      Value closer to 1 indicates better performance and it also explains the variance 
📌Interpretation:-
    Moderate MSE due to high variance in fare values
    R² score indicates the model explains a reasonable portion of fare variability
✅ Final Conclusion:-
    EDA revealed meaningful patterns in the dataset
    Linear Regression successfully captured the relationship between passenger class and fare
    Pclass is the strongest predictor of Fare
    Model performance is acceptable for linear assumptions
    More advanced models may further improve prediction accuracy
    📄 This project demonstrates fundamental ML concepts of  the Exploratory Data Analysis (EDA), regression modeling, coefficient interpretation, and evaluation metrics.
     
