from workout import Workout
from workoutTracker import WorkoutTracker

tracker = WorkoutTracker()

user_menu = """Workout Tracker Menu
- 1. Add a new workout
- 2. View all workouts
- 3. View limited number of workouts
- 4. Update workout date
- 5. Delete a workout
- 6. Exit
Your choice: """

def prompt_add_workout():
    """
    Prompts the user to input workout details and adds the workout using the tracker.
    """
    date = input("Enter the date (e.g., YYYY-MM-DD): ")
    exercise_type = input("Enter the exercise type: ")   
    duration = int(input("Enter the duration (in minutes): "))
    calories_burned = int(input("Enter the calories burned: "))

    workout = Workout(date, exercise_type, duration, calories_burned)
    tracker.add_workout(workout)
    print("Workout added successfully!")


def prompt_view_limited_workouts():
    try:
        limit = int(input("Enter the number of workouts to view: "))
        print(f"\nViewing the first {limit} workouts:")
        print()
        tracker.view_workouts(limit=limit)
    except ValueError:
        print("Invalid input. Please enter a number.")  


def prompt_update_workout():
    workout_id = int(input("Enter the ID of the workout to update: "))
    updated_date = input("Enter the new date (e.g., YYYY-MM-DD): ")
    tracker.update_workout(workout_id, updated_date)


def prompt_delete_workout():
    workout_id = int(input("Enter the ID of the workout to delete: "))
    tracker.delete_workout(workout_id)



def main():
    while True:
        try:
            choice = int(input(user_menu))
        except ValueError:
            print('Invalid value try again')
            continue
        if choice == 1:
            prompt_add_workout()
        elif choice == 2:
            tracker.view_workouts()
        elif choice == 3:
            prompt_view_limited_workouts()
        elif choice == 4:
            prompt_update_workout()
        elif choice == 5:
            prompt_delete_workout()
        elif choice == 6:
            print("Exiting the Workout Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 6.")


if __name__ == "__main__":
    main()      

