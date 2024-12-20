Employee Management System

This is a Python-based Employee Management System that allows users to manage employees of different roles, such as Managers, Developers, and Interns. The system supports adding, removing, searching, and displaying employees with detailed role-specific information.

Features

Employee Roles:

Manager: Includes id, name, designation, and team_size.

Developer: Includes id, name, designation, and programming_language.

Intern: Includes id, name, designation, and duration.

Custom Exception:

InvalidRoleError: Raised when attempting to add an invalid employee type

Core Functionalities:

Add employees.

Display all employees.

Remove an employee by ID.

Search for an employee by ID.

Error Handling:

Handles invalid employee types.

Provides informative messages for non-existent employee IDs.

Classes and Methods

Classes

Employee (Base Class):

Attributes: id, name, designation.

Subclasses:

Manager: Adds team_size.

Developer: Adds programming_language.

Intern: Adds duration.

EmployeeManager:

Manages a list of employees and provides utility methods.

InvalidRoleError:

Custom exception for invalid employee types.