#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def main():
    # Generate some data
    np.random.seed(0)
    X = 2 * np.random.rand(100, 1)
    y = 4 + 3 * X + np.random.randn(100, 1)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create and train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict using the model
    y_pred = model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse:.2f}")

    # Visualize the results
    plt.scatter(X, y, color='blue', label='Data points')
    plt.plot(X_test, y_pred, color='red', linewidth=2, label='Regression line')
    plt.xlabel('X')
    plt.ylabel('y')
    plt.title('Linear Regression Example')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
