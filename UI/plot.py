import matplotlib.pyplot as plt
import numpy as np

# Generate data
x = np.linspace(0, 10, 100)  # 100 points between 0 and 10
y = np.sin(x)                # sine values for each x

# Create the plot
plt.figure(figsize=(8, 4))   # setting the size of the figure
plt.plot(x, y, label='Sine Wave')  # plot x and y and label the line
plt.title('Example Sine Wave Plot')  # title of the plot
plt.xlabel('X axis')         # label for the x-axis
plt.ylabel('Y axis')         # label for the y-axis
plt.legend()                 # show legend with labels
plt.grid(True)               # show grid
plt.show()                   # display the plot
