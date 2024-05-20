import numpy as np
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor



N = int(input("Provide the total number of training data points (N) (N must be a positive integer): "))


k = int(input("Provide the number of neighbors (k) that you want to use in the kNN regression (k must be a positive integer and smaller than or equal to N): "))

# Create empty arrays for x and y, each should be length of N
x = np.zeros(N)
y = np.zeros(N)


for i in range(N):
    x[i] = float(input(f"Enter x coordinate for point {i+1}, x must be real number: "))
    y[i] = float(input(f"Enter y coordinate for point {i+1}, y must be real number: "))


x = x.reshape(-1, 1)


if k > N:
    print("k must be smaller than or equal to N, kNN regression cannot be completed, please restart the process with legitimate input.")
else:

#kNN regression model

    model = KNeighborsRegressor(n_neighbors=k)
    model.fit(x, y)

    X = float(input("Please provide the x-coordinate of your actual test data point (X): "))
    X = np.array([X]).reshape(-1, 1)


    Y = model.predict(X)

    print(f"The predicted y value (Y) for the provided data point with x-coordinate = {X[0][0]} using {k}NN regression is {Y[0]}")

#finding coefficient of determinaation for kNN regression
    y_predicted = model.predict(x)
    r2 = r2_score(y, y_predicted)
    print(f"The coefficient of determination for {k}NN regression is {r2}")


#find variance of labels in the training dataset
variance = np.var(y)
print(f"The variance of the labels in the training dataset is {variance}")
