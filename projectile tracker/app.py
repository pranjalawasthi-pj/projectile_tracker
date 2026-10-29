import streamlit as st
import numpy as np
from physics import projectile_motion,plot_trajectory 
st.title("projectile motion tracker")
st.info("This app calculates the trajectory of a projectile based on initial velocity and angle of projection.")
st.write("Please enter the initial velocity (in m/s) and the angle of projection (in degrees) below:")
st.write("Note: The angle should be between 0 and 90 degrees.")
v0=st.slider("Initial velocity (m/s)", min_value=0.0,max_value=100.0 ,value=30.0, step=1.0)
theta=st.slider("Angle of projection (degrees)", min_value=0.0, max_value=90.0,value=60.0,step=1.0)

    
results=projectile_motion(v0,theta,g=9.8)
st.write(f"Time of flight: {results['time_of_flight']} seconds")
st.write(f"Maximum height: {results['max_height']} meters")
st.write(f"Range: {results['range']} meters")
st.write("Generating the trajectory plot...")
    
figure=plot_trajectory(results["x"],results["y"],v0,theta)
st.pyplot(figure)

             
