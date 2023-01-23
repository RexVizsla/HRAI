import json
from collections import Counter
import os
import matplotlib.pyplot as plt

folder_path = r"C:\Users\rexvizsla\Desktop\AI\HRAI\possible_dataset\rated"

# Initialize an empty list to store the values
values = []

# Iterate through all JSON files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".json"):
        # Open the JSON file
        with open(os.path.join(folder_path, filename)) as json_file:
            data = json.load(json_file)
            # Extract the values from the JSON and add them to the list
            values.extend([int(val * 100) for val in data.values()])

# Count the frequency of each value
value_counts = Counter(values)

# Plot the values and their frequency in a bar chart
plt.bar(value_counts.keys(), value_counts.values())
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Value Frequencies")
plt.xscale('linear')
plt.show()
