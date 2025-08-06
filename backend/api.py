from datetime import date

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from backend.tools.weather import get_weather
from backend.tools.activities import recommend_activities
from backend.agent import init_conversational_agent, llm_generate_response

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

agent = init_conversational_agent()

@app.get("/weather")
def weather(
    city: str = Query(..., description="City name"),
    day: date = Query(None, description="Date of travel (optional)")
):
    return get_weather(city, day)

@app.post("/suggest")
def suggest(
    city: str,
    temperature: float,
    conditions: str,
    day: str,
    lat: float = Query(..., description="Latitude of the city"),
    lon: float = Query(..., description="Longitude of the city")
):
    geo = {"lat": lat, "lon": lon}
    activities = recommend_activities(conditions)
    message = llm_generate_response(
        conversation=agent,
        city=city,
        temp=temperature,
        conditions=conditions,
        activities=activities,
        geo=geo,
        travel_date=day
    )
    return {"suggestions": message}