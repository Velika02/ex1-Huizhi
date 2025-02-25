### a simple checkerboard

import numpy as np
import matplotlib.pyplot as plt

def generate_checkerboard(size=64, num_squares=8):
         """
         Generates a checkerboard pattern image of size (size x size).
         """
         block_size = size // num_squares
         image = np.zeros((size, size))

         for i in range(num_squares):
             for j in range(num_squares):
                 if (i + j) % 2 == 0:
                     image[i * block_size:(i + 1) * block_size, j * block_size:>
 + 1) * block_size] = 1

         return image


### Generate checkerboard image
checkerboard = generate_checkerboard()


### Plot checkerboard
plt.figure(figsize=(6,6))
plt.imshow(checkerboard, cmap="viridis", interpolation="nearest")
plt.axis("off")
plt.title("A Checkerboard Pattern")
plt.show()

