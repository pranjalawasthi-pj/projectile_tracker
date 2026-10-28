# 🚀 Projectile Motion Tracker

### 🌌 Calculate. Visualize. Understand Physics.

An interactive web application built with **Python, Streamlit, NumPy, and Matplotlib** to calculate and visualize the trajectory of a projectile using its initial velocity and launch angle.

---

## ✨ Features

- 🎯 **Time of Flight** — Calculate how long a projectile stays in the air.
- 📏 **Maximum Height** — Find the highest point reached by the projectile.
- 🌍 **Horizontal Range** — Calculate the total horizontal distance travelled.
- 📈 **Trajectory Visualization** — View the projectile's path through an interactive web interface.
- ⚡ **Real-Time Calculations** — Enter different values and explore the results.
- 🖥️ **Simple Interface** — Easy-to-use inputs and clear numerical results.

---

## 🛠️ Built With

| Technology | Purpose |
|---|---|
| 🐍 Python | Core programming and calculations |
| 🌐 Streamlit | Interactive web application |
| 🔢 NumPy | Numerical calculations and trajectory data |
| 📊 Matplotlib | Projectile trajectory visualization |

---

## 📐 Physics Behind the Project

The application uses standard projectile motion equations, assuming ideal conditions and that the projectile lands at the same height from which it was launched.

**1. Time of Flight**

\[
T = \frac{2u\sin\theta}{g}
\]

**2. Maximum Height**

\[
H = \frac{u^2\sin^2\theta}{2g}
\]

**3. Horizontal Range**

\[
R = \frac{u^2\sin(2\theta)}{g}
\]

Where:

- `u` = Initial velocity (m/s)
- `θ` = Launch angle
- `g` = Acceleration due to gravity (9.8 m/s²)
- `T` = Time of flight (s)
- `H` = Maximum height (m)
- `R` = Horizontal range (m)

---

## 📂 Project Structure

```text
projectile-motion-tracker/
│
├── app.py              # Streamlit web interface
├── physics.py          # Physics calculations and plotting functions
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

---

## ⚙️ Run Locally

Follow these steps to run the project on your computer.

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the Project Folder

```bash
cd projectile-motion-tracker
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Launch the Application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in your terminal to use the application.

---

## 📦 Requirements

The project uses the following Python libraries:

- `streamlit`
- `numpy`
- `matplotlib`

These dependencies are listed in `requirements.txt`.

---

## 🌐 Deployment

The application can be deployed using **Streamlit Community Cloud**.

1. Push the project files to a GitHub repository.
2. Visit [Streamlit Community Cloud](https://share.streamlit.io/).
3. Connect your GitHub account and select the repository.
4. Set the main file path to `app.py`.
5. Click **Deploy**.

---

## 🎓 Learning Objectives

This project was developed to practice and explore:

- Python functions and modular programming
- Reusing code through imports
- Numerical computation with NumPy
- Data visualization with Matplotlib
- Building web apps with Streamlit
- Organizing and deploying a Python project

---

## 🔮 Future Improvements

- 🎨 Improve the user interface and visual design
- 📊 Compare trajectories for different launch angles
- 🌬️ Explore projectile motion with air resistance
- 📥 Add an option to download calculated results
- 📱 Improve the experience on mobile devices

---

## 👨‍💻 Author

**Created as a Python learning project.**

If you find this project useful, consider giving the repository a ⭐!

---

*Built with Python and curiosity. 🚀*
