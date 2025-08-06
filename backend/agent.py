from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

def init_conversational_agent():
    memory = ConversationBufferMemory(return_messages=True)
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)
    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=True
    )
    return conversation

def llm_generate_response(conversation, city: str, temp: float, conditions: str, activities: list, geo: dict, travel_date: str) -> str:
    lat, lon = geo.get("lat"), geo.get("lon")

    prompt = (
        f"You are a knowledgeable travel assistant.\n"
        f"The user is visiting **{city}** (latitude: {lat}, longitude: {lon}) on {travel_date}.\n"
        f"The forecast is: **{conditions}**, **{temp}°C**.\n\n"

        f"Based on this weather and location, suggest 3–5 activities that are:\n"
        f"- Suitable for these weather conditions\n"
        f"- Realistic for this specific city and its geography (no lakes = no boat tours, no mountains = no skiing)\n"
        f"- A mix of outdoor and indoor if the weather is poor\n\n"

        f"Use the list below as inspiration, but remove irrelevant ones and add better ones based on the city and weather:\n"
        f"{activities}\n\n"

        f"Return your answer in this format:\n"
        f"**Weather summary**: <your own sentence describing the weather with date selected>\n"
        f"**Recommended activities**:\n"
        f"1. ...\n"
        f"2. ...\n"
        f"..."
    )

    return conversation.predict(input=prompt)
