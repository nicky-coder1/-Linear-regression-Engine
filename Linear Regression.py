x_data = [1.8,2.2,2.6,3.0,3.4,3.8,4.2]                 #CPU Speed (GHz)
y_data = [120,155,180,215,240,275,305]                   #Operations per ms

mean_x = sum(x_data) / len(x_data)                      #Calculating averages of data given
mean_y = sum(y_data) / len(y_data)


covariance_sum = 0
variance_sum = 0

for i in range(len(x_data)):
    x_dev = x_data[i] - mean_x
    y_dev = y_data[i] - mean_y

    covariance_sum += x_dev * y_dev                       #Calculating Covariance and Variance
    variance_sum += x_dev ** 2


m = covariance_sum / variance_sum                          #Calculating slope (m)
c = mean_y - (m * mean_x)                                  #Calculating y-intercept (c)

print(f"Line of Best Fit: y = {m:.2f}x + {c:.2f}")          # Finding Line of best fit using the slope and y-intercept


ss_tot = 0
ss_res = 0

for i in range(len(x_data)):
    y_actual = y_data[i]
    y_predicted = m * x_data[i] + c


    ss_tot += (y_actual - mean_y) ** 2                       #Calculating Total Sum of Squares
    ss_res += (y_actual - y_predicted) ** 2                  #Calculating Residual Sum of Squares

r_squared = 1 - (ss_res / ss_tot)                          #Calculating R-squared value
print(f"R-squared: {r_squared:.4f}")                       #Printing R-squared value


test_hours = 4.5
predicted_score = (m * test_hours) + c  
print(f"Prediction for {test_hours} hours of study:{predicted_score:.1f}%")                                    #Predicting score for a given test hour of 4.5



with open("execution_log.txt",  "w" , encoding="utf-8") as log_file:                                 #Writing the results to a text file
    log_file.write(f"Line Equation: y = {m:.2f}x + {c:.2f}\n")
    log_file.write(f"Accuracy (R-squared): {r_squared:.4f}\n")
    log_file.write(f"Prediction for {test_hours} hours of study: {predicted_score:.1f}%\n")          # Saving Results to a text file



print("Saved results to execution-log.txt!")