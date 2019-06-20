import matplotlib.pyplot as plt

#Scatter plots read two lists for input:
##One of all the x-values, another of all the y-values.
##The two lists naturally need to be identical in length.

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.cubehelix, s=20)

plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)

plt.tick_params(axis = "both", which = "major", labelsize = 14)

plt.show()
