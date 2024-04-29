from fastapi import FastAPI, File, UploadFile
import joblib
import pandas as pd


app = FastAPI()

# Create an instance of the FastAPI app
# @app.get("/")
# async def root():
#     return {"message": "Hello, World!"}

@app.get("/hello/{name}")
async def hello_name(name: str):
    return {"message": f"Hello, {name}!"}