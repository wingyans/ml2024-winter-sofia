import numpy as np
from sklearn.metrics import precision_score, recall_score

# Ask users for the total number of data points in this calculation
N = int(input("Enter the total number of (x, y) points (N): "))

# Create empty arrays for x and y, each should be length of N
X = np.zeros(N, dtype=int)
Y = np.zeros(N, dtype=int)

#Ask users to input x and y coordinates for each point
for i in range(N):
  print(f"Enter point {i+1} (x, y), where X (ground truth class label) and Y (predicted class label) are either 0 or 1: ")
  x = int(input("x: "))
  y = int(input("y: "))

  # Validate x and y input values
  if x not in (0, 1) or y not in (0, 1):
      print("Invalid entry, value must be 0 or 1. Please start over.")
      exit(1)

# Append x and y values to the arrays
  X[i] = x
  Y[i] = y

# Calculate precision and recall scores based on inputs
precision_value = precision_score(X, Y)
recall_value = recall_score(X, Y)

# Print the results
print(f"\nPrecision for binary classification (4dp) = {precision_value:.4f}")
print(f"Recall for binary classification (4dp) = {recall_value:.4f}")
