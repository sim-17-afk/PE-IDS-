# implementation of histogram in matplotlib
import matplotlib.pyplot as plt

data = [10, 20, 20, 25, 30, 35, 40, 40, 45, 50, 55, 60, 60, 65, 70]

plt.hist(data, bins=6, color='skyblue', edgecolor='black')

plt.title("Histogram of Data Values")
plt.xlabel("Value Range")
plt.ylabel("Frequency")

plt.show()