from typing import List, Dict
import random

class AIService:
    def __init__(self):
        self.responses = {
            "greeting": [
                "Hello! How can I assist you today?",
                "Hi there! What do you need help with?",
                "Greetings! How can I support your agricultural needs?"
            ],
            "crop_info": [
                "Here are some tips for growing {crop}: ...",
                "For {crop}, ensure you have the right soil and climate conditions.",
                "Did you know that {crop} thrives best in ...?"
            ],
            "weather_update": [
                "The current weather is {weather}. Make sure to adjust your farming activities accordingly.",
                "It's {weather} today. Don't forget to check your crops!",
                "Expect {weather} conditions today. Plan your irrigation accordingly."
            ]
        }

    def get_greeting(self) -> str:
        return random.choice(self.responses["greeting"])

    def get_crop_info(self, crop: str) -> str:
        return random.choice(self.responses["crop_info"]).format(crop=crop)

    def get_weather_update(self, weather: str) -> str:
        return random.choice(self.responses["weather_update"]).format(weather=weather)

    def process_user_input(self, user_input: str) -> str:
        # Placeholder for natural language processing logic
        if "hello" in user_input.lower():
            return self.get_greeting()
        elif "crop" in user_input.lower():
            crop = user_input.split(" ")[-1]  # Simplistic extraction of crop name
            return self.get_crop_info(crop)
        elif "weather" in user_input.lower():
            weather = "sunny"  # Placeholder for actual weather data
            return self.get_weather_update(weather)
        else:
            return "I'm sorry, I didn't understand that. Can you please rephrase?"