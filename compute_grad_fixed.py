import numpy as np

# Load data
X = np.loadtxt("../Addis2025_DEM/X_Abaya_DEM.txt")
Y = np.loadtxt("../Addis2025_DEM/Y_Abaya_DEM.txt")
Z = np.loadtxt("../Addis2025_DEM/Abaya_DEM.txt")  # elevation


def compute_slopes_in_percentage(X, Y, Z):
    # Compute grid spacing
    dx = np.mean(np.diff(X, axis=1))
    dy = np.mean(np.diff(Y, axis=0))

    # Cardinal direction slopes
    dZdy, dZdx = np.gradient(Z, dy, dx)

    # Diagonal spacing
    diag_dist = np.sqrt(dx**2 + dy**2)

    # Diagonal derivatives
    dZd_NE = np.zeros_like(Z)
    dZd_NW = np.zeros_like(Z)

    dZd_NE[1:-1, 1:-1] = (Z[2:, 2:] - Z[:-2, :-2]) / (2 * diag_dist)
    dZd_NW[1:-1, 1:-1] = (Z[2:, :-2] - Z[:-2, 2:]) / (2 * diag_dist)

    # Convert slope (rise/run) to 0–1 percentage
    def slope_to_percentage(s):
        return np.abs(s) / (1 + np.abs(s))

    # Convert each direction
    sx = slope_to_percentage(dZdx)
    sy = slope_to_percentage(dZdy)
    sNE = slope_to_percentage(dZd_NE)
    sNW = slope_to_percentage(dZd_NW)

    # Take maximum slope per cell
    slope = np.maximum.reduce([sx, sy, sNE, sNW])

    return slope


slope = compute_slopes_in_percentage(X, Y, Z)
