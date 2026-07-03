from fastapi import FastAPI

app = FastAPI()

@app.get("/products")
def products():
    return {
        "Services" : "Product Services",
        "Products" : ["laptop" , "Keyboard" , "Mouse"]
    }

