import streamlit as st
from database import fetch_one, fetch_all

# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="Smart Uttarakhand Travel Assistant",
    page_icon="🏔️",
    layout="wide"
)

st.title("🏔️ Smart Uttarakhand Travel Assistant")

# ==========================
# SIDEBAR
# ==========================

with st.sidebar:

    st.title("🏔️ UK Travel Assistant")

    st.markdown("""
### 🚀 Explore Uttarakhand

• Tourist Places

• Trekking Destinations

• Hill Stations

• Religious Places

• Lakes

• Wildlife Parks

• Adventure Activities

• Budget Trips

• Family Trips

• Snow Destinations
""")

    st.info(
        "Example:\n\n"
        "• Tell me about Mussoorie\n"
        "• Kedarkantha Trek\n"
        "• Hill Stations\n"
        "• Religious Places\n"
        "• Budget Places"
    )

# ==========================
# SESSION STATE
# ==========================

if "messages" not in st.session_state:
    st.session_state.messages = []

# ==========================
# SHOW OLD CHAT
# ==========================

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ==========================
# USER INPUT
# ==========================

prompt = st.chat_input(
    "Ask about places, treks, budget, seasons..."
)

if prompt:

    # -----------------------
    # USER MESSAGE
    # -----------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    user_input = prompt.lower().strip()

    # ==========================
    # GREETINGS
    # ==========================

    greetings = [
        "hi",
        "hello",
        "hey",
        "hii",
        "good morning",
        "good evening",
        "good afternoon"
    ]

    if user_input in greetings:

        response = """
        # 👋 Hello!
        Welcome to the **Smart Uttarakhand Travel Assistant**.
        I can help you with:
        🏔️ Tourist Places🥾 Trekking Destinations
        💰 Budget Planning
        🌤️ Best Seasons
        ⚠️ Safety Information
        🗺️ Trip Suggestions
        Try asking:
        • Tell me about Mussoorie
        • Kedarnath
        • Kedarkantha Trek
        • Hill Stations
        • Religious Places
        """

    else:

        place = None
        trek = None
        places = None

        # ==========================
        # REMOVE COMMON WORDS
        # ==========================

        stop_words = [
            "tell",
            "me",
            "about",
            "show",
            "give",
            "information",
            "of",
            "the",
            "is",
            "please",
            "what",
            "where",
            "trip",
            "travel",
            "visit",
            "tour",
            "place"
        ]

        words = [
            w
            for w in user_input.split()
            if w not in stop_words
        ]

        # ==========================
        # SEARCH COMPLETE PLACE NAME
        # ==========================

        place = fetch_one(
            """
            SELECT *
            FROM destinations
            WHERE LOWER(name) LIKE ?
            """,
            ("%" + user_input + "%",)
        )

        # ==========================
        # SEARCH WORD BY WORD
        # ==========================

        if not place:

            for word in words:

                place = fetch_one(
                    """
                    SELECT *
                    FROM destinations
                    WHERE LOWER(name) LIKE ?
                    """,
                    ("%" + word + "%",)
                )

                if place:
                    break

        # ==========================
        # SEARCH TREK
        # ==========================

        if not place:

            trek = fetch_one(
                """
                SELECT *
                FROM treks
                WHERE LOWER(trek_name) LIKE ?
                """,
                ("%" + user_input + "%",)
            )

        if not trek:

            for word in words:

                trek = fetch_one(
                    """
                    SELECT *
                    FROM treks
                    WHERE LOWER(trek_name) LIKE ?
                    """,
                    ("%" + word + "%",)
                )

                if trek:
                    break

        # ==========================
        # CATEGORY SEARCH
        # ==========================

        if not place and not trek:

            category_map = {
                "hill station":"Hill Station",
                "hill stations":"Hill Station",

                "religious place":"Religious Site",
                "religious places":"Religious Site",

                "lake":"Lake",
                "lakes":"Lake",

                "wildlife":"Wildlife Park",
                "wildlife park":"Wildlife Park",

                "adventure":"Adventure Spot",
                "adventure spot":"Adventure Spot"
            }

            for key,value in category_map.items():

                if key in user_input:

                    places = fetch_all(
                        """
                        SELECT *
                        FROM destinations
                        WHERE category=?
                        """,
                        (value,)
                    )

                    break
                        # ==========================================================
        # PLACE RESPONSE
        # ==========================================================

        if place:

            activities = [
                activity.strip()
                for activity in place["popular_activities"].split(",")
                if activity.strip()
            ]

            activities_text = "\n".join(
                f"- {activity}" for activity in activities
            )

            response = f"""# 🏔️ {place['name']}

📍 **District:** {place['district']}

🗺️ **State:** {place['state']}

🏷️ **Category:** {place['category']}

🌤️ **Best Season:** {place['best_season']}

💰 **Approx Budget:** ₹{place['approx_budget']}

⏳ **Ideal Duration:** {place['ideal_duration']} Day(s)

⚡ **Difficulty Level:** {place['difficulty_level']}

⚠️ **Risk Level:** {place['risk_level']}

## 🎯 Popular Activities

{activities_text}

## 📝 Description

{place['short_description']}

✨ Have a safe and enjoyable journey!
"""

        # ==========================================================
        # CATEGORY RESPONSE
        # ==========================================================

        elif places:

            response = "# 📍 Recommended Destinations\n\n"

            for p in places:

                response += f"""## 🏔️ {p['name']}

📍 **District:** {p['district']}

🏷️ **Category:** {p['category']}

🌤️ **Best Season:** {p['best_season']}

💰 **Budget:** ₹{p['approx_budget']}

⚡ **Difficulty:** {p['difficulty_level']}

📝 {p['short_description']}

---

"""

        # ==========================================================
        # TREK RESPONSE
        # ==========================================================

        elif trek:

            gear = trek["essential_gear"]

            permits = trek["permits"]

            fitness = trek["physical_requirement"]

            hospital = trek["nearest_hospital"]

            safety = trek["safety_note"]

            response = f"""# 🥾 {trek['trek_name']}

📍 **Region:** {trek['region']}

🏔️ **District:** {trek['district']}

⛰️ **Maximum Altitude:** {trek['max_altitude']}

⚡ **Difficulty:** {trek['difficulty']}

⏳ **Duration:** {trek['duration']}

🌤️ **Best Season:** {trek['best_season']}

💰 **Estimated Budget:** {trek['budget']}

## 📄 Permits Required

{permits}

## 🏃 Fitness Required

{fitness}

## 🎒 Essential Gear

{gear}

## 🏥 Nearest Hospital

{hospital}

## ⚠️ Safety Tips

{safety}

🏕️ Happy Trekking!
"""
    # ==========================
    # SHOW ONLY ONE RESPONSE
    # ==========================

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )