import numpy as np
import matplotlib.pyplot as plt
### x and y values ###

x = np.array([1,2,3,4,5,6,7,8,9,10])
y = np.array([2.2 , 2.8 , 3.6 , 4.5 , 5.1 , 6.2 , 6.8 , 8.1 , 9 , 9.9])

# fit a line y = ax+b using numpy's polyfit

a,b = np.polyfit(x,y,1) #1 is linear

#plot original scatter points 
plt.scatter(x,y,color='red',label="sample Data")

# generate y-values for the fitted line
y_fit=a*x+b

#plot best.fit line
plt.plot(x,y_fit, color='blue', label=f"best fit line:y={a:.2f}x+{b:.2f}")
plt.xlabel('x-axis"')
plt.ylabel('y-axis"')
plt.title("line fitting using least square")
plt.legend()
plt.grid()
plt.show()