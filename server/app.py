from flask import Flask

# Initialize the Flask application instance.
app = Flask(__name__)

# Models currently in the Flatiron Cars fleet.
# The '/<model>' route checks the requested model against this list.
existing_models = [
    'Beedle',
    'Crossroads',
    'M2',
    'Panique',
]

# Default route.
# Returns a friendly welcome message so users know the API is live.
@app.route('/')
def index():
    return 'Welcome to Flatiron Cars'

# Dynamic route for a specific car model.
# - If the model exists in `existing_models`, confirm it's in our fleet.
# - Otherwise, tell the user it isn't in our catalog.
@app.route('/<model>')
def car_model(model):
    if model in existing_models:
        return f'Flatiron {model} is in our fleet!'
    return f'No models called {model} exists in our catalog'
