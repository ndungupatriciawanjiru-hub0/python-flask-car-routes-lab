from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Models currently in the company's fleet
existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

# Default route: introduces the company
@app.route('/')
def index():
    return 'Welcome to Flatiron Cars'

# Dynamic route: accepts a car model name from the URL
@app.route('/<model>')
def car_model(model):
    # Check whether the requested model exists in our fleet
    if model in existing_models:
        return f'Flatiron {model} is in our fleet!'
    else:
        return f'No models called {model} exists in our catalog'

if __name__ == '__main__':
    app.run(port=5555, debug=True)