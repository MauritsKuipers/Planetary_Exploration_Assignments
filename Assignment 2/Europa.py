# made by MDMLK #

import matplotlib.pyplot as plt
import numpy as np

def temp_height_enceladus():
    h1 = 0
    T1 = 273
    h2 = 20000
    T2 = 120

    m = (T2 - T1) / (h2 - h1) # Slope of the function
    b = T1 - m * h1

    return m, b

def graph_temp_height():
    m, b = temp_height_enceladus()
    print("Europa m: ", m, "Europa b: ", b)
    x_values = np.arange(0, 20000, 1)
    y_values = m * x_values + b

    # Make the plot
    plt.plot(x_values, y_values)

    # Label and Title
    plt.xlabel("Height, m")
    plt.ylabel("Temperature, K")
    plt.title("Linear Relationship Between Temperature and Height")

    # Show Plot
    plt.show()

def velocity_height():
    m, b = temp_height_enceladus()
    x_values = np.arange(0, 20000, 1)
    y_values = m * x_values + b

    kb = 1.380649 * 10**(-23)
    mh2o = (18.01*10**(-3))/(6.02214*10**(23))

    Vth = np.sqrt((8 * kb * y_values) / (np.pi * mh2o))

    return Vth

def graph_velocity_height():
    x_values = np.arange(0, 20000, 1)
    Vth = velocity_height()

    # Make the plot
    plt.plot(x_values, Vth)

    # Label and Title
    plt.xlabel("Height, m")
    plt.ylabel("Velocity, m/s")
    plt.title("Relationship Between Velocity and Height")

    # Show Plot
    plt.show()
    return

def massflow():
    Vth = velocity_height()
    rho = 4.85  # kg/m3

    mass_flow = rho * Vth

    return mass_flow


def graph_massflow_height():
    x_values = np.arange(0, 20000, 1)
    mass_flow = massflow()

    # Make the plot
    plt.plot(x_values, mass_flow)

    # Label and Title
    plt.xlabel("Height, m")
    plt.ylabel("Mass Flow, kg/s")
    plt.title("Relationship Between Mass Flow and Height")

    # Show Plot
    plt.show()



if __name__ == "__main__":
    graph_temp_height()
    graph_velocity_height()
    graph_massflow_height()
#TEST