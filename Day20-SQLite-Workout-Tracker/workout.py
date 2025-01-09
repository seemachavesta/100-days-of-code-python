
class Workout:
    def __init__(self, date:str, exercise_type: str, duration: int, calories_burned: int):
        self.date = date
        self.exercise_type = exercise_type
        self.duration = duration
        self.calories_burned = calories_burned

    def __repr__(self):
        return f'Date: {self.date}, Exercise: {self.exercise_type}, Duration: {self.duration}, Calories burned: {self.calories_burned}'
    
    
 
