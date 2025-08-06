# GenAI Travel Assistant

An AI-powered travel guide that:
- Fetches weather for any city and date (up to 14 days ahead)
- Recommends suitable activities based on location and forecast
- Uses LangChain, Open-Meteo, and optionally GPT 4 mini

---

## Project Structure

```
.
├── backend/
│   ├── api.py                 # FastAPI endpoints
│   ├── agent.py               # LangChain LLM setup
│   └── tools/
│       ├── weather.py         # Weather fetching via Open-Meteo
│       └── activities.py      # Activity recommender
├── frontend/
│   └── streamlit_app.py       # Streamlit UI
├── docker-compose.yml         # Run full stack
├── requirements.txt           # Python dependencies
└── .env                       # API keys
```

---

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/maxpostolatii/travel_guide_ai_agent.git
cd genai-travel-assistant
```

### 2. Create `.env` file in root

```
OPENAI_API_KEY=your_openai_key_here
```

### 3. Run with Docker Compose

```bash
docker compose up --build
```

- Backend: http://localhost:8000
- Frontend: http://localhost:8501

---

## Features

- LangChain + GPT-4o-mini
- Weather-based activity suggestions
- Location-aware prompt filtering (no boat tours for non-water cities, etc.)
- Streamlit UI with city + date selection
- Handles weather API errors and invalid input
- Weather limited to 14 days from today (because of weather API requirements)


