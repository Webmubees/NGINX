from fastapi import FastAPI
import socket

app = FastAPI()

@app.get("/users")
def users():
    return {
        "services" : "User Services",
        "container" : socket.gethostname(),
        "Users" : ["Alice" , "Bob" , "Charlie"]
        
    }