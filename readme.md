# Sampling Distribution & Confidence Visualizer

A dynamic web application built with **Flask** and **Plotly.js** that provides a visual proof of the Central Limit Theorem. This tool allows users to see how the distribution of sample means changes as the sample size ($n$) increases.

## 🚀 Live Demo
https://confidenceinterval-visualizer.onrender.com

## 📊 Features
- **Dynamic Curve Reshaping**: Watch the bell curve "tighten" in real-time as you increase $n$.
- **95% Confidence Interval**: Visually highlights the area under the curve to show the margin of error.

## 🛠️ Tech Stack
- **Backend**: Python (Flask)
- **Mathematics**: NumPy, SciPy
- **Frontend**: HTML5, CSS3, JavaScript
- **Charting**: Plotly.js

## 💻 Local Setup

1. **Clone the repo:**
   ```
   git clone https://github.com/dilmilsoach/confidenceInterval_visualizer/
   ```

2. **Set up a virtual environment:**
   ```
   python -m venv venv
   \venv\Scripts\activate\
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Run the app:**
   ```
   python app.py
   ```
   Open `http://127.0.0.1:5000` in your browser.

## 📝 The Math Behind the Visuals
The app visualizes the **Standard Error (SE)** formula:
$$SE = \frac{\sigma}{\sqrt{n}}$$

As $n$ increases, the $SE$ decreases, squeezing the distribution of sample means. The shaded green area represents the **95% Confidence Interval**, calculated as:
$$\bar{x} \pm 1.96 \times SE$$

---
*Created as an educational tool for statistics and data science.*
