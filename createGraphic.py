import math
import sys
import numpy as np
import matplotlib.pyplot as plt

# Test functions
# return (1.5 - x + x*y)**2 + (2.25 - x + x*(y**2))**2 + (2.625 - x + x*(y**3))**2 #Beale function
# return (1 + (x+y+1)**2 * (19 - 14*x +3*x**2 -14*y +6*x*y +3*y**2))*(30 +(2*x - 3*y)**2 * (18 - 32*x + 12*x**2 + 48*y - 36*x*y + 27*y**2)) #Goldstein–Price function
# return (x + 2*y - 7)**2 + (2*x + y - 5)**2 #Booth function
# return 0.26*(x**2 + y**2) - 0.48*x*y #Matyas function
# return (x*2 + y - 11)**2 + (x + y**2 -7)**2 #Himmelblau's function

def beale(x, y):
    return (1.5 - x + x * y) ** 2 + (2.25 - x + x * (y ** 2)) ** 2 + (2.625 - x + x * (y ** 3)) ** 2

def goldsteinPrice(x, y):
    return (1 + (x+y+1)**2 * (19 - 14*x +3*x**2 -14*y +6*x*y +3*y**2))*(30 +(2*x - 3*y)**2 * (18 - 32*x + 12*x**2 + 48*y - 36*x*y + 27*y**2))

def booth(x, y):
    return (x + 2 * y - 7) ** 2 + (2 * x + y - 5) ** 2

def matyas(x, y):
    return 0.26 * (x ** 2 + y ** 2) - 0.48 * x * y

def himmelblau(x, y):
    return (x*2 + y - 11)**2 + (x + y**2 -7)**2

def plot_function(func, xlim=(-5, 5), ylim=(-5, 5)):
    x = np.linspace(xlim[0], xlim[1], 400)
    y = np.linspace(ylim[0], ylim[1], 400)
    X, Y = np.meshgrid(x, y)
    Z = func(X, Y)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    plt.show()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Funkcje:")
        print("1. beale")
        print("2. goldsteinPrice")
        print("3. booth")
        print("4. matyas")
        print("5. himmelblau")
        sys.exit()

    if sys.argv[1] == "beale":
        plot_function(beale)
    elif sys.argv[1] == "goldsteinPrice":
        plot_function(goldsteinPrice)
    elif sys.argv[1] == "booth":
        plot_function(booth)
    elif sys.argv[1] == "matyas":
        plot_function(matyas)
    elif sys.argv[1] == "himmelblau":
        plot_function(himmelblau)
    else:
        print(f"Nieznana funkcja")
        print("Funkcje:")
        print("1. beale")
        print("2. goldsteinPrice")
        print("3. booth")
        print("4. matyas")
        print("5. himmelblau")


    # plot_function(beale)
    # plot_function(goldsteinPrice)
    # plot_function(matyas)
    # plot_function(booth)
    # plot_function(himmelblau)
