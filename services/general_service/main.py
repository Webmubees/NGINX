from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "Services" : "General Services",
        "Messages" : "Welcome to the Microservices project !"
    }