import numpy as np
import matplotlib.pyplot as plt
import math

# Constants
rho_ice = 1000  # Density of ice in kg/m3
r0 = 1e-6       # Initial radius in meter
crevasse_length = {"Enceladus": 1000, "Europa": 20000}  # in meter
T_bottom = 273  # Kelvin
T_top = {"Enceladus": 70, "Europa": 120}    # Kelvin
kb = 1.38e-23
m_h2o = 18.01e-3 / 6.022e23
dm = 1

def temp_height_enceladus():
    h1 = 0
    T1 = 273
    h2 = 1000
    T2 = 70

    m = (T2 - T1) / (h2 - h1) # Slope of the function
    b = T1 - m * h1

    return m, b

def thermal_velocity(crevasse_length):
    """Calculate the Temperature Values for the Entire Trip"""
    heights = np.arange(0, int(crevasse_length["Enceladus"]), dm)
    m, b = temp_height_enceladus()
    temperatures = m * heights + b
    """Calculate the thermal velocity at temperature T."""
    return np.sqrt(8 * kb * temperatures / (np.pi * m_h2o))

def calculate_icy_grain_mass(crevasse_length, T_top):
    V_th = thermal_velocity(crevasse_length)    # Vth is working properly

    heights = np.arange(0, int(crevasse_length["Enceladus"]), dm)
    total_mass = np.zeros_like(heights)
    total_mass[0] = (4 * np.pi * rho_ice * r0**3) / (3)     # Initial Mass
    print("Initial masses:", total_mass[0])
    sigma = np.pi * (r0)**2

    for i in range(0, len(heights)):
        if i > 0:
            dt = dm / V_th[i]
            mass_flow = rho_ice * V_th[i]
            accretion = mass_flow * sigma * dt

            total_mass[i] = total_mass[i-1] + accretion

            new_r = ((3*total_mass[i])/(4 * np.pi * rho_ice))**(1/3)

            sigma = np.pi * new_r**2
        if i == 0:
            None
    print("Masses")
    print(total_mass)
    return total_mass

def graph_mass_height():
    total_mass = calculate_icy_grain_mass(crevasse_length, T_top)
    heights = np.arange(0, int(crevasse_length["Enceladus"]), dm)

    # Make the plot
    plt.plot(heights, total_mass)

    # Label and Title
    plt.xlabel("Height, m")
    plt.ylabel("Mass, kg")
    plt.title("Enceladus Ice Grain Relationship Between Mass and Height")

    # Show Plot
    plt.show()

if __name__ == "__main__":
    graph_mass_height()