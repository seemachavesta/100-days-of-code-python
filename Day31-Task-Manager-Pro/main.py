from utils.task_manager import TaskManager
from utils.task import Task


task_manager = TaskManager()


user_menu = """Enter
 - 1 To add to task
 - 2 To view all task
 - 3 To mark task complete
 - 4 To delete Task by id
 - 5 To view recently completed task
 - 6 To update task by id
 - 7 to quit
"""

def prompt_add_tasks():
    # Get task input from user and add to database
    task_id = int(input('Enter task id: '))
    task_title = input('Enter task title: ')
    task_description = input('Enter task description: ')
    due_date = input('Enter task due date: ')
    priority = input('Enter task priority: ')
    task = Task(task_id, task_title, task_description, due_date, priority)
    task_manager.add_task(task)
    print(f'Task with id{task_id} has been added successfull7')

def prompt_mark_task_as_complete():
    # Mark a task as completed and add it to the LinkedList
    try:
        task_id = int(input('Enter task id: '))
        task_manager.mark_task_completed(task_id)
        print('Task updated successfully')
    except ValueError:
        print('Invalid input try again. ')

def prompt_delete_task_by_id():
    # Delete a task by ID from the database
    try:
        task_id = int(input('Enter task id: '))
        task_manager.delete_task(task_id)
        print(f'Task with id {id} has been delete sucessfully.')
    except ValueError:
        print('Invalid id try again. ')

def prompt_update_task():
    #Update task by ID from the database
    try:
        task_id = int(input('Enter task id: '))
        task_manager.update_task(task_id)
        print(f'Task updated successfully.')
    except ValueError:
        print('Invalid id try again. ')



def main():
    # Main user interaction loop
    print(user_menu)
    while True:
        try:
            user_input = int(input("Enter your choice: "))
        except ValueError:
            print('Invalid input try again.')
            continue

        if user_input == 1:
            prompt_add_tasks()
        if user_input == 2:
            task_manager.get_all_tasks()
        if user_input == 3:
            prompt_mark_task_as_complete()
        if user_input == 4:
            prompt_delete_task_by_id()
        if user_input == 5:
            task_manager.get_recently_completed()
        if user_input == 6:
            prompt_update_task()
        if user_input == 7:
            break




if __name__ == '__main__':
    main()
    

