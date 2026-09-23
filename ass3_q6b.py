import numpy as np
import matplotlib.pyplot as plt
import cv2

# Load the two images as grayscale
p1 = cv2.imread("/Users/hananw/Documents/CPBS_7620/ass3/image1.jpg", cv2.IMREAD_GRAYSCALE)
p2 = cv2.imread("/Users/hananw/Documents/CPBS_7620/ass3/image2.jpg", cv2.IMREAD_GRAYSCALE)

# Resize p2 so it has the same size as p1
p2 = cv2.resize(p2, (p1.shape[1], p1.shape[0]))

# Convert to float for the calculations
p1 = p1.astype(float)
p2 = p2.astype(float)

# Alpha values from 0 to 1 in steps of 0.2
alpha_values = np.arange(0, 1.01, 0.2)

for alpha in alpha_values:

    blended = alpha * p1 + (1 - alpha) * p2

    plt.figure()
    plt.imshow(blended, cmap="gray")
    plt.title("alpha = " + str(round(alpha, 1)))
    plt.axis("off")
    plt.show()