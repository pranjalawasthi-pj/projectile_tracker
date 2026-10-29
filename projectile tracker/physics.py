import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as pl

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
    fig=pl.Figure()
    fig.add_trace(pl.Scatter(x=x,y=y,mode="lines"))
    peak=np.argmax(y)
    fig.add_trace(pl.Scatter(x=[x[peak]],y=[y[peak]],mode="markers",marker=dict(color="red"),name="Max height"))
    fig.update_layout(title="Projectile Motion Trajectory",xaxis_title="Horizontal distance(m)",yaxis_title="Vertical distance(m)",legend=dict(x=1,y=1),width=900,height=600)        
    return fig
    






    
