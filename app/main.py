# main.py

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello World"}


@app.get("/about")
def about():
    return {"project": "My First CI/CD deployment of FastAPI App"}


# NEW ENDPOINT 1
@app.get("/health")
def health():
    return {
        "status": "ok", 
        "service": "fastapi-running"
        }


# NEW ENDPOINT 2
@app.get("/version")
def version():
    return {
        "app": "FastAPI CI/CD Demo",
        "version": "1.0.1"
    }