
def make_prediction(model, transformed_input):
    return model.predict(transformed_input)[0]


