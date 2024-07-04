import matplotlib.pyplot as plt
import numpy as np
import json

def load_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data['labels'], data['sizes']

labels_01, sizes_01 = load_data('p_1.json')
labels_02, sizes_02 = load_data('p_2.json')

differences = np.array(sizes_02) - np.array(sizes_01)

plt.figure(figsize=(12, 6))

plt.subplot(131)
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
plt.pie(sizes_01, labels=labels_01, colors=colors, autopct='%1.1f%%')
plt.axis('equal')
plt.title('Price At 2020')

plt.subplot(132)
plt.pie(sizes_02, labels=labels_02, colors=colors, autopct='%1.1f%%')
plt.axis('equal')
plt.title('Price At 2024')

plt.subplot(133)
bar_colors = ['#008000' if diff >= 0 else '#ff6666' for diff in differences]
plt.bar(labels_01, differences, color=bar_colors)
plt.axhline(0, color='black', linewidth=0.8)
plt.xlabel('Labels')
plt.ylabel('Difference in Sizes')
plt.title('Difference Between Pie Charts')

plt.tight_layout()
plt.show()
