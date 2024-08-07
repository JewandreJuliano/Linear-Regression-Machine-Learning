# Simple Machine Learning Example: Linear Regression
    This project demonstrates a basic example of machine learning using linear regression with scikit-learn. Linear regression is a fundamental algorithm in machine learning used to model the relationship between a dependent variable and one or more independent variables.

## Overview
- The script provided performs the following steps:

   - Generate Data: Create synthetic data with a linear relationship.
   - Split Data: Divide the data into training and testing sets.
   - Train Model: Fit a linear regression model to the training data.
   - Evaluate Model: Assess the model's performance using Mean Squared Error (MSE).
   - Visualize Results: Plot the data points and the fitted regression line.

- ***numpy*** is used for generating and manipulating numerical data.
- ***matplotlib*** is used for plotting graphs.
- ***scikit-learn*** provides tools for splitting data, training models, and evaluating performance.

- ***X*** represents the feature (independent variable) and ***y*** represents the target (dependent variable).
- The data is generated with a linear relationship **y = 4 + 3 * X** plus some noise.

- Split the data into training (80%) and testing (20%) sets.
- Create a LinearRegression model and fit it to the training data.
- Use the trained model to predict values for the test set.
- Calculate and print the Mean Squared Error to evaluate model performance.
- Plot the original data points in blue and the fitted regression line in red.
- Display labels, title, and legend on the plot.
# How to Run the Script

1. Clone the Repository.(git clone <repository-url>
cd <repository-directory>
)
2. Create a Virtual Environment( ***python -m venv .venv*** )
3. Activate the Virtual Environment( ***.venv\Scripts\activate*** )
4. Install Required Packages( ***pip install -r requirements.txt*** )
5. Run the Script( ***python linear_regression.py*** )

# Side Notes:
This was my second attempt at this project, I initially wanted to create a script that is able to recognize certain fruits and vegetable. It was very confusing to me but i will continue to work on it and hopefully have it up soon.