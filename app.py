from fastapi import FastAPI
from pydantic import BaseModel
import pickle

app = FastAPI(
    title="API de Predição de Diabetes",
    description="API de Machine Learning para prever a ocorrência de diabetes com base em dados clínicos.",
    version="1.0.0"
)

class PatientData(BaseModel):
    Pregnancies: int
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

with open("model_diabetes.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/", tags=["Status"])
def home():
    return {"message": "API funcionando"}

@app.post("/predict", tags=["Predição"])
def predict(data: PatientData):
    values = list(data.dict().values())
    prediction = model.predict([values])

    return {
        "prediction": int(prediction[0]),
        "descricao": "Paciente com diabetes" if prediction[0] == 1 else "Paciente sem diabetes"
    }