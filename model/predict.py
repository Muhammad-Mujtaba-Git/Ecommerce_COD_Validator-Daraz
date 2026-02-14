import pandas as pd
import joblib
import os

# Model Path
MODEL_PATH = os.path.join('model', 'Daraz.pkl')
model = joblib.load(MODEL_PATH)


def predictions(data_dict):

    input_df = pd.DataFrame([{
        "price": float(data_dict["price"]),
        "qty_ordered": float(data_dict["qty_ordered"]),
        "category_name_1": data_dict["category_name_1"],
        "Month": float(data_dict["Month"]),
        "date": float(data_dict["date"]),

    }])

    pred = model.predict(input_df)[0]
    gross_index = list(model.classes_).index('Gross')
    prob_gross = model.predict_proba(input_df)[0][gross_index]

   # prob_gross = model.predict_proba(input_df)[0][1]

    threshold = 0.30
    is_gross = prob_gross >= threshold
    status = "Gross (Cancellation Risk )" if is_gross else "Net (Safe )"
    return {
        "prediction": status,
        "probability_of_cancellation": f"{prob_gross:.2%}",
    
    }
    # return round(float(pred), 2)
