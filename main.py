import jokes
from fastapi import FastAPI

app = FastAPI()

@app.get("/jokes")
def get_jokes():
    return {"jokes": jokes.tech_jokes}







