Workout Tracker Project

This project is part of the 100 Days of Code in Python challenge (Day 20). It demonstrates the use of Python concepts such as classes, iterators, file organization, and database operations to create a functional Workout Tracker application. The project is structured into multiple files for modularity and clarity.

Project Overview

The Workout Tracker allows users to manage their workout records. Users can:

Add new workouts

View all workouts

View a limited number of workouts

Update workout dates

Delete workouts

The application uses SQLite for data persistence and employs iterators to fetch and display workout records.


1. database_connection.py

Provides a reusable DatabaseConnection class to handle SQLite database connections using Python's sqlite3 module.

2. workout.py

Defines the Workout class, which models a workout record with the following attributes:

date: Date of the workout (e.g., YYYY-MM-DD)

exercise_type: Type of exercise (e.g., Running, Yoga)

duration: Duration of the workout in minutes

calories_burned: Calories burned during the workout

3. workout_tracker.py

Implements the WorkoutTracker class to manage workout records in the SQLite database. Key methods include:

create_table(): Creates the workouts table in the database if it doesn’t exist.

add_workout(workout): Adds a new workout to the database.

view_workouts(limit=None): Displays all workouts or a limited number of records.

update_workout(workout_id, updated_date): Updates the date of a workout by its ID.

delete_workout(workout_id): Deletes a workout by its ID.

Implements Python’s __iter__() and __next__() methods to iterate over workout records.

4. main.py

Provides the user interface for interacting with the application. Includes a menu-driven approach to access the following functionalities:

Add a workout

View all workouts

View a limited number of workouts

Update a workout date

Delete a workout

Exit the application