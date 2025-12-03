import numpy as np
import matplotlib.pyplot as plt

def plot_sound_graph(filename):
    data = np.loadtxt(filename, delimiter = ",", skiprows = 1)
    lengths = data[:, 0]
    trials  = data[:, 1:]

    inv_length = 1 / lengths
    averages = np.mean(trials, axis = 1)
    sigma = np.std(trials, axis = 1, ddof = 1)

    x = inv_length
    y = averages
    w = 1 / sigma

    m, b = np.polyfit(x, y, 1, w = w)

    residuals = y - (m * x + b)
    chi2 = np.sum((residuals / sigma) ** 2)
    chi2_red = chi2 / (len(x) - 2)

    S   = np.sum(1 / sigma ** 2)
    Sx  = np.sum(x / sigma ** 2)
    Sxx = np.sum(x ** 2 / sigma ** 2)

    delta = S * Sxx - Sx ** 2
    dm = np.sqrt(chi2_red * (S / delta))
    db = np.sqrt(chi2_red * (Sxx / delta))

    plt.errorbar(x, y, yerr=sigma, fmt = "o", capsize = 5)

    x_fit = np.linspace(min(x), max(x), 200)
    plt.plot(x_fit, m * x_fit + b, color = 'orange', linewidth = 2)

    plt.title("Average vs 1/L (with outliers, weighted LS)")
    plt.xlabel("1/L (1/m)")
    plt.ylabel("Average frequency (Hz)")

    plt.text(
        0.05, 0.95,
        f"Weighted LS fit:\n"
        f"m = {m:.3f} ± {dm:.3f}\n"
        f"b = {b:.3f} ± {db:.3f}",
        transform = plt.gca().transAxes,
        fontsize = 11,
        va = 'top',
        bbox=dict(facecolor = 'white', alpha = 0.7)
    )

    plt.tight_layout()
    plt.show()

plot_sound_graph("sound_data.csv")