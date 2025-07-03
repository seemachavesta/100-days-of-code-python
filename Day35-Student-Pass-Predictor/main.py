from src.student import Student
from src.model_handler import  load_model
from src.preprocess import preprocess_input
from src.predictor import make_prediction
from src.model_handler import load_processor



def get_user_input():
    print(" Enter student information:")
    gender = input("Gender (male/female): ")
    race = input("Race/Ethnicity (e.g. group A, group B): ")
    education = input("Parental level of education: ")
    lunch = input("Lunch (standard/free): ")
    prep = input("Test preparation course (none/completed): ")
    math = int(input("Math score (0–100): "))
    reading = int(input("Reading score (0–100): "))
    writing = int(input("Writing score (0–100): "))

    return Student(
        gender=gender,
        race_ethnicity=race,
        parental_education=education,
        lunch=lunch,
        prep_course=prep,
        math_score=math,
        reading_score=reading,
        writing_score=writing
    )

def main():
    student = get_user_input()

    # prepare input
    student_data = student.to_dict()


    # load model and transformer
    model = load_model()
    transformer = load_processor()

    # preprocess input
    transformed_input = preprocess_input(student_data, transformer)

    print("Input shape:", transformed_input.shape)

    # predict
    prediction = make_prediction(model, transformed_input)

    # output
    if prediction == 1:
        print("\n Prediction: PASS")
    else:
        print("\n Prediction: FAIL")



if __name__ == "__main__":
    main()




