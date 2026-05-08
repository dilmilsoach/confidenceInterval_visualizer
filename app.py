import sys
print(f"DEBUG: Using Python at {sys.executable}")
print(f"DEBUG: Looking for libraries in {sys.path}")


from flask import Flask, render_template, request, jsonify
import numpy as np
from scipy.stats import norm

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update', methods=['POST'])
def update():
    data = request.get_json()
    n = int(data.get('n', 30))
    
    # Standard Error (SE = sigma / sqrt(n))
    se = 1.0 / np.sqrt(n)
    
    # 1. Generate full distribution curve
    x = np.linspace(-4, 4, 1000)
    y = norm.pdf(x, 0, se)
    
    # 2. Generate 95% Confidence Interval (z = 1.96)
    limit = 1.96 * se
    x_ci = np.linspace(-limit, limit, 100)
    y_ci = norm.pdf(x_ci, 0, se)
    
    # Define traces for Plotly
    traces = [
        {
            # Shaded Area: x goes forward then backward, y goes values then to zero
            'x': x_ci.tolist() + [limit, -limit],
            'y': y_ci.tolist() + [0, 0], 
            'fill': 'toself',
            'fillcolor': 'rgba(46, 204, 113, 0.3)',
            'line': {'color': 'transparent'},
            'name': '95% Confidence Interval',
            'hoverinfo': 'skip'
        },
        {
            'x': x.tolist(),
            'y': y.tolist(),
            'type': 'scatter',
            'mode': 'lines',
            'name': 'Sample Means Distribution',
            'line': {'color': '#1a73e8', 'width': 3}
        }
    ]

    return jsonify({'traces': traces, 'y_full': y.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
