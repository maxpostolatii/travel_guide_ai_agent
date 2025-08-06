def recommend_activities(conditions: str) -> list:
    conditions = conditions.lower()  # normalize to lowercase
    if any(x in conditions for x in ["rain", "shower", "storm"]):
        return [
            "Visit local museums or art galleries",
            "Try traditional indoor restaurants or cafes",
            "Explore covered shopping centers or historic libraries"
        ]
    elif any(x in conditions for x in ["clear", "sun"]):
        return [
            "Take a city walking tour or rent a bike",
            "Visit parks or botanical gardens",
            "Try outdoor street food and local markets"
        ]
    elif any(x in conditions for x in ["cloud", "fog", "overcast"]):
        return [
            "Take a boat tour or riverside walk",
            "Visit observatories or viewpoint decks"
        ]
    elif any(x in conditions for x in ["snow"]):
        return [
            "Go sledding or visit a ski area (if available)",
            "Enjoy hot chocolate at a cozy café",
            "Visit a local spa or thermal bath"
        ]
    else:
        return [
            "Check out local cultural centers or exhibitions",
            "Relax in a cozy café with a book",
            "Visit indoor theme parks or aquariums"
        ]