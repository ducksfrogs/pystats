import numpy as np
import matplotlib.pyplot as plt


colors=["#348ABD","#A60628"]
prior = [1/21, 20/21]
posterior = [0.087, 1-0.087]
plt.bar([0, .7],prior, alpha=0.70, width=0.25,
        color=colors[0], label="prior distribution",
        lw="3", edgecolor="#348ABD")

plt.bar([0 + 0.25, .7 + 0.25], posterior, alpha=0.70, width=0.25,
        color=colors[1], label= "posterior distribution",
        lw="3", edgecolor="#348ABD")
plt.xticks([0.20, 0.95],["Librarian", "Farmer"])
plt.ylabel("Probability")
plt.legend(loc="upper left")
plt.title("Prior and posterior prpbability of stieve")
plt.show()
