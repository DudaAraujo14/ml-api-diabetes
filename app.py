from fastapi import FastAPI
import pickle

app = FastAPI()

# carregar modelo
with open("model_diabetes.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def home():
    return {"message": "API funcionando"}

@app.post("/predict")
def predict(data: dict):
    values = list(data.values())
    prediction = model.predict([values])

    return {"prediction": int(prediction[0])}