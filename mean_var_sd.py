 import numpy as np

def calculate(list):
    if len(list) == 9:

      # Convert list to numpy array
      matrix = np.array(list).reshape(3,3)

      # Calculate the mean
      mean_matrix = [np.mean(matrix, axis=0).tolist(), np.mean(matrix, axis=1).tolist(), np.mean(matrix)]

      # Calculate the variance
      var_matrix = [np.var(matrix, axis=0).tolist(), np.var(matrix, axis=1).tolist(), np.var(matrix)]

      # Calculate the standard deviation
      std_matrix = [np.std(matrix, axis=0).tolist(), np.std(matrix, axis=1).tolist(), np.std(matrix)]

      # Calculate the max
      max_matrix = [np.max(matrix, axis=0).tolist(), np.max(matrix, axis=1).tolist(), np.max(matrix)]

      # Calculate the min
      min_matrix = [np.min(matrix, axis=0).tolist(), np.min(matrix, axis=1).tolist(), np.min(matrix)]

      # Calculate the sum
      sum_matrix = [np.sum(matrix, axis=0).tolist(), np.sum(matrix, axis=1).tolist(), np.sum(matrix)]

      calculations = {
            'mean': mean_matrix,
            'variance': var_matrix,
            'standard deviation': std_matrix,
            'max': max_matrix,
            'min': min_matrix,
            'sum': sum_matrix
        }
      return calculations
    else:
        raise ValueError('List must contain nine numbers')