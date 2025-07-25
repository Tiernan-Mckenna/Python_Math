import matplotlib.pyplot as plt
import numpy as np

def sim_orbit_Newton(dt=3600, total_years=76):
    #define variables/constants
    x = 5.27e12
    y = 0.0

    v_x = 0.0
    v_y = 912.0

    mass_sun = 1.989e30
    mass_halley = 2.2e14
    G = 6.6743e-11

    Total_time = total_years * 365.25 * 24 * 3600
    steps = int(Total_time/dt)

    x_list=[]
    y_list=[]

    #calculation
    for _ in range(steps):
        r = np.sqrt(x**2 + y**2)
        ax = -G * mass_sun * x/r**3
        ay = -G * mass_sun * y/r**3

        v_x += ax * dt
        v_y += ay * dt

        x += v_x * dt
        y += v_y * dt

        x_list.append(x)
        y_list.append(y)
    return x_list, y_list
