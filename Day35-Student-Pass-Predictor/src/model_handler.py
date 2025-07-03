import pickle


# load the model and processor
def load_model():
    with open('models/model.pkl', 'rb') as file:
        return pickle.load(file)


def load_processor():
    with open('models/preprocessor1.pkl', 'rb') as file:
        return pickle.load(file)