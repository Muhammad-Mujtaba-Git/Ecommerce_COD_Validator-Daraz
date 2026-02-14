from fastapi import FastAPI, HTTPException
from model.predict import predictions, model
from schema.userInput import Userinput

app = FastAPI()


@app.get("/")
def home():
    return {"message": "API is Running"}


@app.post("/predict")
def run_pred(data: Userinput):
    try:
        data_as_dict = data.model_dump()
        result = predictions(data_as_dict)
        return {"predictions": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
