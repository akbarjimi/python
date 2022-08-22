import matplotlib.pyplot as plt

plt.style.available
range = range(1, 11)
sqrt = [n % 9 for n in range]
print(sqrt)
# This function can generate one or more plots in the same fig­ure
# The variable fig represents the entire figure or collection of plots that are generated
# The variable ax represents a single plot in the figure and is the variable we’ll use most of the time
fix, ax = plt.subplots()

plt.style.use('ggplot')
ax.plot(range, sqrt, linewidth=3)
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.tick_params(axis='both', labelsize=14)
plt.show()
