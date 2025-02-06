from fastapi import FastAPI
import pickle
import pandas as pd
from data_model import Water

app =FastAPI(
    title="Water Potability Prediction API",
    description="API to predict water potability",
    version="0.1"
)

with open("D:\\ml_pipeline\\model.pkl","rb") as f:
    model = pickle.load(f)
 
 #first endpoint    
@app.get("/")
def index():
    return "Welcome to Water Potability Prediction API"    

@app.post("/predict")
def model_predict(water : Water):
    sample =pd.DataFrame(
        {
            "ph":[water.ph],
            "Hardness":[water.Hardness],
            "Solids":[water.Solids],
            "Chloramines":[water.Chloramines],
            "Sulfate":[water.Sulfate],
            "Conductivity":[water.Conductivity],
            "Organic_carbon":[water.Organic_carbon],
            "Trihalomethanes":[water.Trihalomethanes],
            "Turbidity":[water.Turbidity]
        }
    )
    
    prediction = model.predict(sample)
    
    if prediction ==1:
        return "Water is Consumable"
    else:
        return "Water is not Consumable"