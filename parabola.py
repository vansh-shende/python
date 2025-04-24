import numpy as np
import matplotlib.pyplot as plt
### x and y values ###

x = np.array([-4, -3, -2, -2, 0, 1, 2, 3, 4, 5])
y = np.array([20, 10, 6, 2, 1, 2, 5, 10, 19, 30])


# fit a line y = ax+b using numpy's polyfit

a,b,c = np.polyfit(x,y,2) #1 is linear

#plot original scatter points 
plt.scatter(x,y,color='red',label="sample Data")

# generate y-values for the fitted line
y_fit=a*x*x+b*x+c

#plot best.fit line
plt.plot(x,y_fit, color='blue', label=f"best fit line:y={a:.2f}x^2+{b:.2f}x+{c:.2f}")
plt.xlabel('x-axis"')
plt.ylabel('y-axis"')
plt.title("line fitting using least square")
plt.legend()
plt.grid()
plt.show()