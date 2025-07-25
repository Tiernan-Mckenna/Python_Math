import numpy as np

#constants
G = 6.67e-11
Mass_Sun = 1.989e30

def acc(x,y):
    r = np.sqrt(x**2 + y**2)
    ax = -G * Mass_Sun * x/r**3
    ay = -G * Mass_Sun * y/r**3
    return ax, ay

def rk4_method(x,y,vx,vy, dt):
    #k1
    ax1, ay1 = acc(x,y)
    k1_vx = ax1 * dt
    k1_vy = ay1 * dt
    k1_x = vx * dt
    k1_y = vy * dt

    #k2
    ax2, ay2 = acc(x+0.5*k1_x, y + 0.5 * k1_y)
    k2_vx = ax2 * dt
    k2_vy = ay2 * dt
    k2_x = (vx+0.5*k1_vx) * dt
    k2_y = (vy+0.5*k1_vy) * dt

    #k3
    ax3, ay3 = acc(x + 0.5 * k2_x, y + 0.5 * k2_y)
    k3_vx = ax3 * dt
    k3_vy = ay3 * dt
    k3_x = (vx + 0.5 * k2_vx) * dt
    k3_y = (vy + 0.5 * k2_vy) * dt
    
    #k4
    ax4, ay4 = acc(x + 0.5 * k3_x, y + 0.5 * k3_y)
    k4_vx = ax4 * dt
    k4_vy = ay4 * dt
    k4_x = (vx + 0.5 * k3_vx) * dt
    k4_y = (vy + 0.5 * k3_vy) * dt

    #New Vals
    x_new = x + (k1_x + 2*k2_x + 2*k3_x + k4_x) / 6
    y_new = x + (k1_y + 2*k2_y + 2*k3_y + k4_y) / 6
    vx_new = x + (k1_vx + 2*k2_vx + 2*k3_vx + k4_vx) / 6
    vy_new = x + (k1_vy + 2*k2_vy + 2*k3_vy + k4_vy) / 6

    return x_new, y_new, vx_new, vy_new

def orbit_sim(dt=3600, total_years=76):
    x = 5.27e12
    y = 0.0

    vx = 0.0
    vy = 912.0

    total_time = total_years * 365.25 * 24 * 3600
    steps = int(total_time/dt)

    x_list, y_list = [],[]

    for _ in range(steps):
        x_list.append(x)
        y_list.append(y)
        x,y,vx,vy=rk4_method(x,y,vx,vy,dt)
    return x_list, y_list
