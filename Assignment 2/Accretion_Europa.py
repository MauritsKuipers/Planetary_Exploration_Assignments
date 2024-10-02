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

def temp_height_europa():
    h1 = 0
    T1 = 273
    h2 = 20000
    T2 = 120

    m = (T2 - T1) / (h2 - h1) # Slope of the function
    b = T1 - m * h1

    return m, b

def thermal_velocity(crevasse_length):
    """Calculate the Temperature Values for the Entire Trip"""
    heights = np.arange(0, int(crevasse_length["Europa"]), dm)
    m, b = temp_height_europa()
    temperatures = m * heights + b
    """Calculate the thermal velocity at temperature T."""
    return np.sqrt(8 * kb * temperatures / (np.pi * m_h2o))

def calculate_icy_grain_mass(crevasse_length, T_top):
    V_th = thermal_velocity(crevasse_length)  # Vth is working properly

    heights = np.arange(0, int(crevasse_length["Europa"]), dm)
    total_mass = []  # Use a list to store mass values
    initial_mass_mg = ((4 * np.pi * rho_ice * r0**3) / (3))
    total_mass.append(initial_mass_mg)  # Append initial mass
    print("Initial mass:", total_mass[0])
    sigma = np.pi * (r0)**2

    for i in range(1, len(heights)):
        print("Sigma:", sigma)
        dt = dm / V_th[i]
        mass_flow = 4.85*10**(-3) * V_th[i]    # or rho_ice * V_th[i]
        print("Mass Flow:", mass_flow)
        accretion = mass_flow * 4 * sigma * dt
        print("Accretion:", accretion)
        total_mass.append(total_mass[i - 1] + accretion)  # Append the new total mass
        print("Previous Mass:", total_mass[i - 1])
        print("Current Mass:", total_mass[i])
        new_r = ((3 * total_mass[i]) / (4 * np.pi * rho_ice))**(1/3)

        sigma = np.pi * new_r**2
    print("total_mass: ", total_mass)
    return total_mass


def graph_mass_height():
    total_mass = calculate_icy_grain_mass(crevasse_length, T_top)  #back to grams
    heights = np.arange(0, int(crevasse_length["Europa"]), dm)

    # Make the plot
    plt.plot(heights, total_mass)

    # Label and Title
    plt.xlabel("Height, m")
    plt.ylabel("Mass, kg")
    plt.title("Europa Ice Grain Relationship Between Mass and Height")

    # Show Plot
    plt.show()

if __name__ == "__main__":
    graph_mass_height()