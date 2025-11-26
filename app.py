import streamlit as st
import joblib
import pandas as pd

model = joblib.load(r"D:\Users\hp\canoe\backend\best_xgb_model (2).pkl")

# mapping: UI_name → model_feature_name
feature_map = {
    "Lines of Code": "loc",
    "Cyclomatic Complexity": "v(g)",
    "Essential Complexity": "ev(g)",
    "Design Complexity": "iv(g)",
    "Operands Count": "n",
    "Volume": "v",
    "Length": "l",
    "Difficulty": "d",
    "Intelligence": "i",
    "Effort": "e",
    "Estimated Bugs": "b",
    "Time to Program": "t",
    "Code Lines": "lOCode",
    "Comment Lines": "lOComment",
    "Blank Lines": "lOBlank",
    "Code + Comment Lines": "locCodeAndComment",
    "Unique Operators": "uniq_Op",
    "Unique Operands": "uniq_Opnd",
    "Total Operators": "total_Op",
    "Total Operands": "total_Opnd",
    "Branch Count": "branchCount"
}

inputs = {}

st.title("Software Detection UI (Simple Names)")

for ui_label in feature_map.keys():
    inputs[feature_map[ui_label]] = st.number_input(ui_label, value=0.0)

if st.button("Predict"):
    df = pd.DataFrame([inputs])
    pred = model.predict(df)[0]
    st.success(f"Prediction: {pred}")