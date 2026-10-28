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
    plt.figure(figsize=(12,12))
    plt.plot(x,y,color="blue", label= f"velocity={v0} m/s,angle={angle_deg} degrees")
    peak=np.argmax(y)
    plt.scatter(x[peak],y[peak],color="red",zorder=5,label="Max height")
    plt.title("Projectile Motion Trajectory")
    plt.axhline(0,color="black",linewidth=0.9)
    plt.xlabel("Horizontal distance(m)")
    plt.ylabel("Vertical height(m)")
    plt.legend(loc="upper right")
    plt.tight_layout()
    plt.savefig("graph.png")
    plt.show()
    



print("=== Projectile Motion Tracker ===")
v0 = float(input("Enter initial velocity (m/s): "))
angle_deg = float(input("Enter launch angle (degrees): "))

result = projectile_motion(v0, angle_deg)

print(f"\nTime of Flight : {result['time_of_flight']:.2f} s")
print(f"Max Height     : {result['max_height']:.2f} m")
print(f"Range          : {result['range']:.2f} m")

plot_trajectory(result["x"], result["y"], v0, angle_deg)
    