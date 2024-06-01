import random
import requests

# Constants
API_KEY = "781b7e58fa5b4a818713d9c9fa431c37"  # Your Weatherbit API key
WEATHER_API_URL = "https://api.weatherbit.io/v2.0/current"

def detect_emotion(image_path):
    """
    Simulate emotion detection by randomly selecting an emotion.
    
    Args:
    image_path (str): Path to the image file.
    
    Returns:
    str: Detected emotion.
    """
    emotions = ["happy", "sad", "neutral", "angry"]
    return random.choice(emotions)

def get_motivational_phrase(emotion):
    """
    Get a motivational phrase based on the detected emotion.
    
    Args:
    emotion (str): Detected emotion.
    
    Returns:
    str: Motivational phrase.
    """
    phrases = {
        "happy": "Keep shining!",
        "sad": "It's a new day, keep pushing forward!",
        "neutral": "Today is full of possibilities!",
        "angry": "Take a deep breath and start fresh."
    }
    return phrases.get(emotion, "Have a great day!")

def fetch_weather_data(lat, lon):
    """
    Fetch weather information from the Weatherbit API based on latitude and longitude.
    
    Args:
    lat (float): Latitude of the location.
    lon (float): Longitude of the location.
    
    Returns:
    dict: Weather data if the request is successful, None otherwise.
    """
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
    """
    Get weather information formatted as a string based on latitude and longitude.
    
    Args:
    lat (float): Latitude of the location.
    lon (float): Longitude of the location.
    
    Returns:
    str: Formatted weather information or an error message.
    """
    weather_data = fetch_weather_data(lat, lon)
    if weather_data and "data" in weather_data:
        city_name = weather_data["data"][0]["city_name"]
        weather = weather_data["data"][0]["weather"]["description"]
        temperature = weather_data["data"][0]["temp"]
        return f"The current weather in {city_name} is {weather} with a temperature of {temperature}°C."
    return "Weather information not available."

# Simulated usage example
def main():
    image_path = "user_photo.jpg"  # Simulated image path
    lat, lon = 41.3851, 2.1734  # Coordinates for Barcelona

    emotion = detect_emotion(image_path)
    phrase = get_motivational_phrase(emotion)
    weather_info = get_weather(lat, lon)

    print(f"Detected emotion: {emotion}, Motivational phrase: {phrase}")
    print(weather_info)

if __name__ == "__main__":
    main()
