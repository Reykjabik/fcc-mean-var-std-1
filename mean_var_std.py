import numpy as np

def get_stats(func, arr):
  return [func(arr, axis=0).tolist(),
          func(arr, axis=1).tolist(),
          func(arr)]

def calculate(list):
  # Check the list contains 9 elements
  if len(list) == 9:
    arr = np.array(list).reshape((3, 3))

    calculations = {'mean': get_stats(np.mean, arr),
                    'variance': get_stats(np.var, arr),
                    'standard deviation': get_stats(np.std, arr),
                    'max': get_stats(np.max, arr),
                    'min': get_stats(np.min, arr),
                    'sum': get_stats(np.sum, arr)}

  # Otherwise, raise ValueError
  else:
    raise ValueError('List must contain nine numbers.')

  return calculations