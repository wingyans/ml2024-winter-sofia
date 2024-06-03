##import libraries that will be used

import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier

### Set up Training Dataset

N = int(input("Enter the total number of (x, y) points (N) for training set TrainS (N must be a positive integer): "))

# Create empty arrays for training dataset x and y
TrainS_x = []
TrainS_y = []

#Ask users to input x and y coordinates for each point
for i in range(N):
  print(f"Enter point {i+1} (x, y) (x is input feature and can only be real number; y is class label and can only be non-negative integer:")
  train_x = float(input("x: "))
  train_y = int(input("y: "))
  TrainS_x.append(train_x)
  TrainS_y.append(train_y)

#Reshape x and y to prepare data input for sklearn

TrainS_x = np.array(TrainS_x).reshape(-1, 1)  
TrainS_y = np.array(TrainS_y)


### Set up Testing Dataset
M = int(input("Enter the total number of (x, y) points (M) for testing set TestS (M must be a positive integer): "))

# Create empty arrays for testing dataset x and y
TestS_x = []
TestS_y = []

#Ask users to input x and y coordinates for each point
for i in range(M):
  print(f"Enter point {i+1} (x, y) (x is input feature and can only be real number; y is class label and can only be non-negative integer:")
  test_x = float(input("x: "))
  test_y = int(input("y: "))
  TestS_x.append(test_x)
  TestS_y.append(test_y)

#Reshape x and y to prepare data input for sklearn

TestS_x = np.array(TestS_x).reshape(-1, 1)  
TestS_y = np.array(TestS_y)


### Create kNN Classifier
param_grid = {'n_neighbors': list(range(1, 11))}
KNN = KNeighborsClassifier()

### Perform Grid Search for Hyperparameter 
GS_KNN = GridSearchCV(KNN, param_grid, cv=5)
GS_KNN.fit(TrainS_x, TrainS_y)

### Find the best hyperparameter for kNN Classification Method
best_k = GS_KNN.best_params_['n_neighbors']
best_model = GS_KNN.best_estimator_

### Predict the value of Y in the testing dataset 
predicted_TestS_y = best_model.predict(TestS_x)

### Find test accuracy score
test_accuracy = accuracy_score(TestS_y, predicted_TestS_y)

### Print Final Results
print(f"The optimal k value (best_k) is: {best_k}")
print(f"The test accuracy score is: {test_accuracy:.2f}")








