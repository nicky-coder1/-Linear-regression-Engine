# Linear Regression & R² Accuracy Engine

## Overview
A pure Python program that calculates the **line of best fit** (y = mx + c) and measures its statistical accuracy from scratch, without using external maths or machine learning libraries.

## How It Works
1. **Averages & Variance:** Uses `for` loops to calculate the mean, variance, and covariance of two data lists (X and Y).
2. **Line Derivation:** Computes the gradient (m) and y-intercept (c) using S statistical formulas.
3. **Accuracy Testing (R^2):** Compares the model's predictions against the actual data to calculate the Coefficient of Determination (R^2).
4. **Predictions & Logging:** Predicts new values from the derived equation and saves the output results to `execution_log.txt`.