import pandas as pd
import numpy as np

data = pd.read_csv('checkout_2.CSV')

for hour in range(24):
    hour_data = data[data['time'] == f'{hour:02}h']

    today = hour_data['avg_last_week'].values[0]
    avg_last_month = hour_data['avg_last_month'].values[0]

    n = 2  # number of data points

    # calculate variance and standard deviation
    var = ((today - avg_last_month) ** 2) / (n - 1)
    std_dev = np.sqrt(var)

    print(f'{hour:02}h: variance={var:.3f}, std_dev={std_dev:.3f}')
