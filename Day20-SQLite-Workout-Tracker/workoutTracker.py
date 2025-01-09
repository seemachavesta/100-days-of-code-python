from utils.database_connection import DatabaseConnection
from workout import Workout

class WorkoutTracker:
    
    def __init__(self, table_name='workouts'):
        """
            Initializes the WorkoutTracker instance.
            Sets up the database table name and database connection.
        """
        self.table_name = table_name
        self.db_connection = DatabaseConnection()
        self.current_index = 0
        # self.workouts = []
    

    def create_table(self):
        """ 
            Creates a table in the database for storing workout records.
            Ensures the table is created only if it does not already exist.
        """
        query = f'''CREATE TABLE IF NOT EXISTS {self.table_name} (
            id INTEGER PRIMARY KEY,
            date TEXT,
            exercise_type TEXT,
            duration INTEGER,
            calories_burned INTEGER
        )'''

        with self.db_connection as connection:
            cursor = connection.cursor()
            cursor.execute(query)


    def __iter__(self):
        """
            Makes the WorkoutTracker iterable by fetching all workouts
            from the database and resetting the current index.
        """
        query = f'SELECT * FROM {self.table_name}'
        with self.db_connection as connection:
            cursor = connection.cursor()
            cursor.execute(query)
            self.workouts = cursor.fetchall()

        self.current_index = 0
        return self
    
    
    def __next__(self):
        """
            Implements the iteration logic. Returns the next workout
            in the list or raises StopIteration when the end is reached.
        """
        if self.current_index >= len(self.workouts):
            raise StopIteration
        
        workout = self.workouts[self.current_index]
        self.current_index += 1
        return workout
    

    def add_workout(self, workout):
        """
            Adds a new workout to the database.
            Ensures that duplicate workouts (same date and exercise type) are not added.
        """
        query_check = f'''SELECT * FROM {self.table_name} 
                        WHERE date = ? AND exercise_type = ?'''
        insert_query = f'''INSERT INTO {self.table_name}
                        (date, exercise_type, duration, calories_burned)
                        VALUES (?, ?, ?, ?)'''
        
        with self.db_connection as connection:
            cursor = connection.cursor()
            cursor.execute(query_check, (workout.date, workout.exercise_type))
            existing_workout = cursor.fetchone()
            
            if existing_workout:
                print('Workout already exists')
                return
            
            # Insert the new workout
            cursor.execute(insert_query, (workout.date, workout.exercise_type, workout.duration, workout.calories_burned))


    #Deletes a workout from the database using its unique ID.
    def delete_workout(self, workout_id):
        query = f'DELETE FROM {self.table_name} WHERE id = ?'
        with self.db_connection as connection:
            cursor = connection.cursor()
            cursor.execute(query, (workout_id,))


   # Updates the date of a workout identified by its unique ID.
    def update_workout(self,workout_id, updated_date):
        query = f"UPDATE {self.table_name} SET date=? WHERE id = ?"
        with self.db_connection as connection:
            cursor = connection.cursor()
            cursor.execute(query,(updated_date, workout_id))

        if cursor.rowcount == 0:
             print(f"No workout found with ID {workout_id}.")
        else:
            print(f'Workout date with ID {workout_id} has been updated successfully.')


    
    def view_workouts(self, limit=None):
        """
            Retrieves and displays workouts from the database.
            Optionally limits the number of displayed entries
       """
        query = f"SELECT * FROM {self.table_name} LIMIT ?" if limit else f"SELECT * FROM {self.table_name}"
        
        with self.db_connection as connection:
            cursor = connection.cursor()
            if limit:
                cursor.execute(query, (limit,))
            else:
                cursor.execute(query)
            workouts = cursor.fetchall()

        if not workouts:
            print("No workouts found.")
            return

        
        for workout in workouts:
            id, date, exercise, duration, calories = workout
            print(f'Id: {id}, Date: {date}, Exercise: {exercise}, Duration: {duration}, Calories Burned: {calories}')
            print('-' * 30)





    
# day1 = Workout('1/1/2025', 'Running', 30, 300)
# day2 = Workout('1/2/2025', 'Yoga', 60, 200)
# day3 = Workout('1/3/2025', 'Cycling', 45, 300)
# day4 = Workout('1/4/2025', 'Strength', 60, 400)

# tracker = WorkoutTracker()
# tracker.create_table()
# tracker.add_workout(day1)
# tracker.add_workout(day2)
# tracker.add_workout(day3)
# tracker.add_workout(day4)
# tracker.view_workouts()
# tracker.update_workout(1, '2/2/22025')
# tracker.view_workouts()

