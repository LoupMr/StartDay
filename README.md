# StartDay App

StartDay is a Flask-based web application designed to enhance your morning routine by providing motivational phrases based on detected emotions and real-time weather information.

## Features

- Detects user's emotion from a provided image.
- Generates a motivational phrase based on the detected emotion.
- Fetches current weather information for a specified location.
- Displays all information in a simple and clean web interface.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Requests

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/startday.git
    cd startday
    ```

2. Install the required Python packages:
    ```bash
    pip install Flask requests
    ```

### Running the Application

1. Start the Flask application:
    ```bash
    python app.py
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/` to see the app in action.

## Project Structure

```
startday/
│
├── app.py                  # Main application script
└── README.md               # Project README file
```

## Code Overview

### Constants

- `API_KEY`: Your Weatherbit API key.
- `WEATHER_API_URL`: URL endpoint for Weatherbit's current weather API.

### Functions

- `detect_emotion(image_path)`: Simulates emotion detection from an image.
- `get_motivational_phrase(emotion)`: Returns a motivational phrase based on the detected emotion.
- `fetch_weather_data(lat, lon)`: Fetches weather data from Weatherbit API.
- `get_weather(lat, lon)`: Retrieves and formats weather information.

### Flask Route

- `/`: Main route that displays the detected emotion, motivational phrase, and weather information.

## Example

When you run the app and visit the main page, you will see:

- The detected emotion (simulated as random for now).
- A motivational phrase corresponding to the detected emotion.
- Current weather information for Barcelona.

### Sample Output

```
Detected emotion: happy
Motivational phrase: Keep shining!
The current weather in Barcelona is Clear sky with a temperature of 25°C.
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
