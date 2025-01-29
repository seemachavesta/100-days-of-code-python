Article Manager

This project, Article Manager, was created as part of my 100-day Python code challenge (Day 25). The goal was to practice working with SQLite databases, higher-order functions, and user input handling while managing a collection of articles.

Features

Add Articles: Store articles with a title, URL, category, date, and read status.

Display Articles: View all stored articles in a formatted list.

Filter Articles: Search for articles by category, read status, or date.

Update Read Status: Mark articles as read or unread.

Delete Articles: Remove an article by its title.

Technologies Used

Python

SQLite (via DatabaseConnection)

Higher-Order Functions for filtering and processing articles

How It Works

Articles are stored in an SQLite database (data.db).

The ArticleManager class handles database interactions.

The Article class represents individual articles.

A command-line menu allows users to manage their articles easily.

Lessons Learned

This project helped reinforce:

Working with SQLite databases in Python

Using higher-order functions for filtering and processing

Handling user input and database queries efficiently

Next Steps

Improve error handling and input validation.

Enhance the user interface with better formatting.

Possibly integrate a simple web interface in the future.