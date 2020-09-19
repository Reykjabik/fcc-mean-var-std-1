import numpy as np

def calculate(list):
  # Check the list contains 9 elements
  if len(list) == 9:
    arr = np.array(list).reshape((3, 3))
    
    mean_list = [np.mean(arr, axis=0).tolist(),
                np.mean(arr, axis=1).tolist(),
                np.mean(arr)
    ]

    var_list = [np.var(arr, axis=0).tolist(),
                np.var(arr, axis=1).tolist(),
                np.var(arr)
    ]

    std_list = [np.std(arr, axis=0).tolist(),
                np.std(arr, axis=1).tolist(),
                np.std(arr)
    ]
    
    max_list = [np.max(arr, axis=0).tolist(),
                np.max(arr, axis=1).tolist(),
                np.max(arr)
    ]

    min_list = [np.min(arr, axis=0).tolist(),
                np.min(arr, axis=1).tolist(),
                np.min(arr)
    ]

    sum_list = [np.sum(arr, axis=0).tolist(),
                np.sum(arr, axis=1).tolist(),
                np.sum(arr)
        ]

    calculations = {'mean': mean_list,
                    'variance': var_list,
                    'standard deviation': std_list,
                    'max': max_list,
                    'min': min_list,
                    'sum': sum_list}

  #  print(calculations)
  # Otherwise, raise ValueError
  else:
    raise ValueError('List must contain nine numbers.')

  return calculations