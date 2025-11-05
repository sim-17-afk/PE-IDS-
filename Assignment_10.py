# implementation of different charts , plots in matplotlib
import matplotlib.pyplot as plt
# line chart
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(x, y, color='green', marker='o')
plt.title("Line Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# # bar chart
x = ['A', 'B', 'C', 'D']
y = [23, 17, 35, 29]

plt.bar(x, y, color='blue')
plt.title("Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

# pie chart
labels = ['Python', 'Java', 'C++', 'JavaScript']
sizes = [35, 25, 20, 20]

plt.pie(sizes, labels=labels, startangle=90)
plt.title("Programming Language Usage")
plt.show()

# scatter plot
x = [5, 7, 8, 10, 12, 15]
y = [10, 14, 13, 20, 25, 30]

plt.scatter(x, y, color='red')
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()