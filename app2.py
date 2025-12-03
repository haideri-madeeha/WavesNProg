import numpy as np
import matplotlib.pyplot as plt

def plot_sound_graph(filename):
    data = np.loadtxt(filename, delimiter = ",", skiprows = 1)
    lengths = data[:, 0]
    trials  = data[:, 1:]

    inv_length = 1 / lengths
    averages = np.mean(trials, axis = 1)
    st_dev = np.std(trials, axis = 1)

    weights = 1 / st_dev ** 2

    m, b = np.polyfit(inv_length, averages, deg = 1, w = weights)
    x_fit = np.linspace(min(inv_length), max(inv_length), 5)
    y_fit = m * x_fit + b
    
    plt.plot(x_fit, y_fit, color = "orange", linewidth = 2, label = "Weighted LS fit:") 

    plt.errorbar(inv_length, averages, yerr = st_dev, fmt = "o", capsize = 4)

    plt.title("Average vs 1/L (with outliers, weighted LS)")
    plt.xlabel("1/L (1/m)")
    plt.ylabel("Average frequency (Hz)")

    plt.tight_layout()
    plt.show()

plot_sound_graph("sound_data.csv")