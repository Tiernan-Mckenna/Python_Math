from Orbit_sim import sim_orbit_Newton
from Plot_Utils import plot_orbit
from RK4_method import orbit_sim

#Euler method

x_vals, y_vals = sim_orbit_Newton()
plot_orbit(x_vals,y_vals, title="Halley's Orbit Using Euler's method")

#RK4 Method plot
# x_vals, y_vals = orbit_sim()
# plot_orbit(x_vals,y_vals, "Halley's Orbit using RK4 Method")