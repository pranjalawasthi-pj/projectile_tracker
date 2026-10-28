import numpy as np
import matplotlib.pyplot as plt

def projectile_motion(v0, angle_deg, g=9.8):
    """
    Calculates projectile motion parameters and trajectory points.

    v0        : initial velocity (m/s)
    angle_deg : launch angle in degrees
    g         : acceleration due to gravity (m/s^2), default = 9.8 (Earth)

    Returns a dictionary with range, max height, time of flight,
    and the x, y arrays for plotting the trajectory.
    """
    theta = np.radians(angle_deg)

    # Core physics formulas
    time_of_flight = (2 * v0 * np.sin(theta)) / g
    max_height = (v0 ** 2 * np.sin(theta) ** 2) / (2 * g)
    range_ = (v0 ** 2 * np.sin(2 * theta)) / g

    # Generate 200 evenly spaced time steps from 0 to time_of_flight
    t = np.linspace(0, time_of_flight, num=200)

    # Position at each time step
    x = v0 * np.cos(theta) * t
    y = v0 * np.sin(theta) * t - 0.5 * g * t ** 2

    return {
        "time_of_flight": time_of_flight,
        "max_height": max_height,
        "range": range_,
        "x": x,
        "y": y
    }


def plot_trajectory(x, y, v0, angle_deg):
    fig,ax=plt.figure(figsize=(12,12))
    ax.plot(x,y,color="blue", label= f"velocity={v0} m/s,angle={angle_deg} degrees")
    peak=np.argmax(y)
    ax.scatter(x[peak],y[peak],color="red",zorder=5,label="Max height")
    ax.title("Projectile Motion Trajectory")
    ax.axhline(0,color="black",linewidth=0.9)
    ax.xlabel("Horizontal distance(m)")
    ax.ylabel("Vertical height(m)")
    ax.legend(loc="upper right")
    fig.tight_layout()
    return fig
    






    