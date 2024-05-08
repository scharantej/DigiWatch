
# Import necessary modules
from flask import Flask, request, render_template
import time

# Create a Flask web application
app = Flask(__name__)

# Define the main route
@app.route('/', methods=['GET', 'POST'])
def index():
    # If the request is a POST request, update the time
    if request.method == 'POST':
        new_time = request.form['time']
        # Update the time variable with the new time
        time = new_time

    # Render the index.html file, passing the time variable
    return render_template('index.html', time=time)

# Start the Flask web application
if __name__ == '__main__':
    app.run(debug=True)
