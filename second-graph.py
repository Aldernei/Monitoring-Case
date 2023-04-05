import matplotlib.pyplot as plt
import pandas as pd

# Load the data from the CSV file
data = pd.read_csv('checkout_2.CSV')

# Set the time column as the index
data = data.set_index('time')

# Create a line graph
plt.plot(data.index, data['avg_last_week'], label='Average Last Week')
plt.plot(data.index, data['avg_last_month'], label='Average Last Month')

# Add axis labels and a legend
plt.xlabel('Time')
plt.ylabel('Number of Sales')
plt.legend()

# Display the graph
plt.show()
