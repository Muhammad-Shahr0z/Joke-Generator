import random
import jokes
import streamlit as st

# Page Config
st.set_page_config(page_title="Tech Jokes API", page_icon="😂", layout="centered")

# Custom CSS Styling
st.markdown("""
    <style>
    body {
        background-color: #f4f4f4;
    }
    .title {
        font-size: 32px;
        font-weight: bold;
        color: #333;
        text-align: center;
        margin-bottom: 20px;
    }
    .joke-box {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 2px 4px 12px rgba(0,0,0,0.2);
        text-align: center;
        font-size: 20px;
        font-weight: bold;
        color: #444;
        transition: 0.3s;
    }
    .joke-box:hover {
        transform: scale(1.02);
    }
    .button {
        background-color: #4CAF50;
        color: white;
        padding: 12px 20px;
        font-size: 18px;
        border-radius: 8px;
        border: none;
        cursor: pointer;
        transition: 0.3s;
    }
    .button:hover {
        background-color: #45a049;
    }
    .footer {
        text-align: center;
        font-size: 16px;
        margin-top: 30px;
        color: #555;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.markdown('<div class="title">😂 Tech Jokes API 😂</div>', unsafe_allow_html=True)

st.write("Click the button to hear a funny tech joke!")

# Joke Logic
joke = jokes.tech_jokes
if st.button("Tell me a joke 😆", key="joke_btn"):
    selected_joke = random.choice(joke)
    st.markdown(f'<div class="joke-box">{selected_joke}</div>', unsafe_allow_html=True)

# Centered Footer with Name
st.markdown('<div class="footer">🚀 Developed with ❤️ by Muhammad Shahroz</div>', unsafe_allow_html=True)
