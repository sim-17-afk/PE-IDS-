# implementation of different graphs in matplotlib

import matplotlib.pyplot as plt
# line graph
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(x, y, color='blue', marker='o')
plt.title("Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# bar graph
x = ['A', 'B', 'C', 'D']
y = [10, 20, 15, 25]

plt.bar(x, y, color='orange')
plt.title("Bar Graph")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

# histogram
data = [10, 20, 20, 30, 40, 40, 40, 50, 60]

plt.hist(data, bins=5, color='purple', edgecolor='black')
plt.title("Histogram")
plt.xlabel("Value Range")
plt.ylabel("Frequency")
plt.show()