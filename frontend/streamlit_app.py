import streamlit as st
import requests
import datetime

BACKEND_URL = "http://backend:8000"

st.set_page_config(page_title="Travel Agent Guide", layout="centered")
st.title("🧳 Travel Agent Guide")
st.write("Personalized activity suggestions based on your travel destination and weather.")

city = st.text_input("Enter destination city")

# Calculate max allowed date (today + 14 days)
today = datetime.date.today()
max_forecast_date = today + datetime.timedelta(days=14)

# Add date input with restriction
travel_date = st.date_input(
    "Select travel date",
    min_value=today,
    max_value=max_forecast_date,
    value=today
)

if st.button("Get Recommendations"):
    if not city:
        st.warning("Please enter a city.")
    else:
        with st.spinner("Calling backend services..."):
            res = requests.get(f"{BACKEND_URL}/weather", params={"city": city, "day": travel_date.isoformat()})

            if res.status_code != 200:
                st.error("Failed to fetch weather.")
            else:
                weather = res.json()
                if "error" in weather:
                    st.error(f"Weather error: {weather['error']}")
                else:
                    res2 = requests.post(f"{BACKEND_URL}/suggest", params={
                        "city": city,
                        "temperature": weather["temperature"],
                        "conditions": weather["conditions"],
                        "lat": weather["geo"]["lat"],
                        "lon": weather["geo"]["lon"],
                        "day": weather["date"]
                    })

                    if res2.status_code != 200:
                        st.error("Failed to get suggestions.")
                    else:
                        st.subheader("Suggested Activities")
                        st.markdown(res2.json()["suggestions"])
                        st.caption(f"Lat: {weather['geo']['lat']}, Lon: {weather['geo']['lon']}")
