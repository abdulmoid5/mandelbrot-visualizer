import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter=100):
    """
    Computes the Mandelbrot set iteration count for a given complex number c.
    
    Parameters:
    c (complex): The complex number to test for Mandelbrot set inclusion.
    max_iter (int): The maximum number of iterations to check for divergence.
    
    Returns:
    int: The number of iterations before divergence, or max_iter if bounded.
    """
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def generate_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter=100):
    """
    Generates a Mandelbrot set image in the given coordinate range.
    
    Parameters:
    xmin, xmax (float): The range of real values to compute.
    ymin, ymax (float): The range of imaginary values to compute.
    width, height (int): The resolution of the output image.
    max_iter (int): The maximum number of iterations for Mandelbrot calculations.
    
    Returns:
    numpy.ndarray: A 2D array representing the Mandelbrot set, where values indicate escape time.
    """
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
