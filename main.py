import jokes
import random
from fastapi import FastAPI
import requests
import streamlit as st

# FastAPI app initialization
app = FastAPI()

@app.get("/jokes")
def get_jokes():
    return {"jokes": jokes.tech_jokes}

# Streamlit UI Styling
st.set_page_config(page_title="Joke Generator 🤣", page_icon="🎭", layout="centered")

# Custom CSS for better contrast in both dark & light modes
st.markdown(
    """
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
        }

        /* Automatic theme handling */
        @media (prefers-color-scheme: dark) {
            body {
                background-color: #1e1e2e;
                color: white;
            }
            .joke-box {
                background-color: #333;
                color: white;
                box-shadow: 2px 2px 10px rgba(255, 255, 255, 0.2);
            }
        }

        @media (prefers-color-scheme: light) {
            body {
                background-color: white;
                color: black;
            }
            .joke-box {
                background-color: #f0f0f0;
                color: black;
                box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
            }
        }

        /* Button Styling */
        .stButton button {
            background-color: #ff5733 !important;
            color: white !important;
            border-radius: 10px;
            font-size: 18px;
            padding: 10px 20px;
            transition: 0.3s;
            font-weight: bold;
        }
        .stButton button:hover {
            background-color: #ff2e00 !important;
            color: white !important;  /* Fix: Ensures text remains visible */
        }

        .joke-box {
            padding: 20px;
            border-radius: 12px;
            font-size: 20px;
            margin-top: 20px;
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit UI
st.title("🤣 The Ultimate Tech Joke Generator 🤖")
st.subheader("Get ready to laugh with some nerdy jokes! 😆")

# Button to fetch joke
if st.button("😂 Crack a Joke!"):
    try:
        response = requests.get("http://127.0.0.1:8000/jokes")
        jokes = response.json()
        joke = random.choice(jokes["jokes"])
        
        st.markdown(f"<div class='joke-box'>{joke}</div>", unsafe_allow_html=True)
    
    except:
        st.error("😵 Something went wrong! Try again later.")

# Footer text
st.markdown("---")
st.markdown("💻 Made with ❤️ by a Tech Enthusiast!")
