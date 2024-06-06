import joblib

model_prediction = joblib.load('graboostcla_model.joblib')
target_result = joblib.load('encoding_target.joblib')

def prediction(data):
    result = model_prediction.predict(data)
    final_result = target_result.inverse_transform(result)[0]
    return final_result