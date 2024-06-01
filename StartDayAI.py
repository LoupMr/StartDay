import random
import requests
from flask import Flask, render_template_string

# Constants
API_KEY = "781b7e58fa5b4a818713d9c9fa431c37"  # Your Weatherbit API key
WEATHER_API_URL = "https://api.weatherbit.io/v2.0/current"

app = Flask(__name__)

def detect_emotion(image_path):
    emotions = ["happy", "sad", "neutral", "angry"]
    return random.choice(emotions)

def get_motivational_phrase(emotion):
    phrases = {
        "happy": "Keep shining!",
        "sad": "It's a new day, keep pushing forward!",
        "neutral": "Today is full of possibilities!",
        "angry": "Take a deep breath and start fresh."
    }
    return phrases.get(emotion, "Have a great day!")

def fetch_weather_data(lat, lon):
    params = {
        'lat': lat,
        'lon': lon,
        'key': API_KEY
    }
    try:
        response = requests.get(WEATHER_API_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def get_weather(lat, lon):
    weather_data = fetch_weather_data(lat, lon)
    if (weather_data and "data" in weather_data):
        city_name = weather_data["data"][0]["city_name"]
        weather = weather_data["data"][0]["weather"]["description"]
        temperature = weather_data["data"][0]["temp"]
        return f"The current weather in {city_name} is {weather} with a temperature of {temperature}°C."
    return "Weather information not available."

@app.route('/')
def main():
    image_path = "user_photo.jpg"  # Simulated image path
    lat, lon = 41.3851, 2.1734  # Coordinates for Barcelona

    emotion = detect_emotion(image_path)
    phrase = get_motivational_phrase(emotion)
    weather_info = get_weather(lat, lon)

    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Emotion and Weather Info</title>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: #f0f0f0;
                font-family: Arial, sans-serif;
            }
            .container {
                background-color: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                text-align: center;
            }
            h1 {
                color: #333;
            }
            p {
                font-size: 1.2em;
                color: #555;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>StartDay </h1>
            <p><strong>Detected emotion:</strong> {{ emotion }}</p>
            <p><strong>Motivational phrase:</strong> {{ phrase }}</p>
            <p>{{ weather_info }}</p>
        </div>
    </body>
    </html>
    """, emotion=emotion, phrase=phrase, weather_info=weather_info)

if __name__ == "__main__":
    app.run(debug=True)
