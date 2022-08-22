import matplotlib.pyplot as plt

plt.style.use('ggplot')
fix, ax = plt.subplots()
# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

x_values = range(1, 1001)
y_values = [x ** 3 for x in x_values]

# Set the range for each axis.
ax.scatter(x_values, y_values, c=(0.5, 0.5, 0.5), s=10)
ax.scatter(x_values, y_values, c=x_values, cmap=plt.cm.Blues, s=10)

# plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight')
