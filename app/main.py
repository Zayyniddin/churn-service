from fastapi import FastAPI
import pandas as pd
import numpy as np
from app.model_loader import model, scaler, encoder, num_cols, cat_cols
from app.schemas import ClientData

app = FastAPI(title="Churn Prediction API")

@app.get("/")
def root():
    return {"message": "Churn Prediction API is running"}

@app.post("/predict")
def predict_churn(data: ClientData):

    # Превращаем входные данные в DataFrame
    df = pd.DataFrame([data.dict()])

    # 1. Масштабируем числовые признаки
    X_num = scaler.transform(df[num_cols])

    # 2. Кодируем категориальные признаки
    X_cat = encoder.transform(df[cat_cols])

    # 3. Объединяем
    X_final = np.hstack([X_num, X_cat])

    # 4. Предсказания
    proba = model.predict_proba(X_final)[0][1]
    pred = model.predict(X_final)[0]

    return {
        "predicted_class": int(pred),
        "churn_probability": float(proba)
    }