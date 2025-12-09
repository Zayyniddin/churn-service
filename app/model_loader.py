import pickle

with open("../models/churn_xgb_model.pkl", "rb") as f:
    artifacts = pickle.load(f)

model = artifacts["model"]
scaler = artifacts["scaler"]
encoder = artifacts["encoder"]
num_cols = artifacts["num_cols"]
cat_cols = artifacts["cat_cols"]