class Student:
    def __init__(self, gender, race_ethnicity, parental_education, lunch, prep_course, math_score, reading_score, writing_score):
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_education = parental_education
        self.lunch = lunch
        self.prep_course = prep_course
        self.math_score = math_score
        self.reading_score = reading_score
        self.writing_score = writing_score


    # Convert into dictionary
    def to_dict(self):

        return {
            "gender": self.gender,
            "race/ethnicity": self.race_ethnicity,
            "parental level of education": self.parental_education,
            "lunch": self.lunch,
            "test preparation course": self.prep_course,
            "math score": self.math_score,
            "reading score": self.reading_score,
            "writing score": self.writing_score
        }


