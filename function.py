import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter=100):
    """Computes the Mandelbrot set iteration count for a given complex number c."""
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def generate_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter=100):
    """Generates a Mandelbrot set image in the given coordinate range."""
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    
    mandelbrot_set = np.empty((height, width))
    
    for i in range(height):
        for j in range(width):
            mandelbrot_set[i, j] = mandelbrot(complex(x[j], y[i]), max_iter)
    
    return mandelbrot_set

# Define the plot region and resolution
xmin, xmax, ymin, ymax = -2, 1, -1.5, 1.5
width, height = 800, 600
max_iter = 100

# Generate the Mandelbrot set
data = generate_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter)

# Plot the Mandelbrot set
plt.figure(figsize=(10, 7))
plt.imshow(data, extent=(xmin, xmax, ymin, ymax), cmap='inferno', origin='lower')
plt.colorbar(label='Iterations to escape')
plt.title('Mandelbrot Set')
plt.xlabel('Real Axis')
plt.ylabel('Imaginary Axis')
plt.show()
