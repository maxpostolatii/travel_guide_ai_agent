from backend.tools.weather import get_weather
from backend.tools.activities import recommend_activities
from backend.agent import init_conversational_agent, llm_generate_response

if __name__ == "__main__":
    import os
    city = input("Enter a city: ")
    api_key = os.getenv("OPENWEATHER_API_KEY")  # Set your OpenWeather API key

    weather = get_weather(city, api_key)

    if "error" in weather:
        print(f"Error: {weather['error']}")
    else:
        activities = recommend_activities(weather["conditions"], weather["temperature"])
        agent = init_conversational_agent()
        message = llm_generate_response(agent, city, weather["temperature"], weather["conditions"], activities)
        print("\nTravel Guide Recommendation:\n")
        print(message)
