import jokes
from fastapi import FastAPI
import streamlit as st

app = FastAPI()

@app.get("/jokes")
def get_jokes():
    return {"jokes": jokes.tech_jokes}


st.title("Tech Jokes API")
st.write("Here are some tech jokes:")
for joke in jokes.tech_jokes:
    st.write(joke)









