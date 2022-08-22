import matplotlib.pyplot as plt
from random import choice


class RandomWalk:
    """ A class """

    def __init__(self, num_points=5000) -> None:
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walks(self):
        while len(self.x_values) < self.num_points:
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            if x_step == 0 or y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)


rw = RandomWalk(500000)
rw.fill_walks()
plt.style.use('classic')
fix, ax = plt.subplots(figsize=(15, 9))
point_numbers = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)
ax.scatter(0, 0, c='green', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.show()
