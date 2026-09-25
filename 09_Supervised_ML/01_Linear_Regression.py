import matplotlib.pyplot as plt
import numpy as np

hours = [1, 2, 3, 4, 5]
scores = [50, 55, 65, 75, 90]

plt.scatter(hours, scores)
plt.title("Hours Studied vs Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Scores")
plt.legend()
plt.show()