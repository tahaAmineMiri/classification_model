from fastapi import FastAPI, File, UploadFile
import pandas as pd
import io
import joblib


app = FastAPI()

# laod the model
model = joblib.load('./model.pkl')

# Create an instance of the FastAPI app
@app.post("/")
async def root(file: UploadFile = File(...)):
    
    # Read the uploaded CSV file
    df = pd.read_csv(io.StringIO((await file.read()).decode('utf-8')))
    # df = pd.read_csv("./dataset/heart_10.csv")

    # Assuming 'target' is your target column
    features = df.drop('target', axis=1)
    
    # predict the target
    prediction = model.predict(features)
    
    prediction = prediction.tolist()
    
    return {"prediction": prediction}
    
    