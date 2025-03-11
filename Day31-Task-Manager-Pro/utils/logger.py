import logging

class Logger:
    @staticmethod
    def setup_logger():
        #Set up logging configuration with a file named 'task_manager.log'
        logging.basicConfig(filename="task_manager.log", level=logging.INFO)

    @staticmethod
    def log_task_added(task):
        # Log information when a task is added
        logging.info(f"Task Added: {task.to_dict()}")
        

    @staticmethod
    def log_task_updated(task):
        # Log information when a task is updated
        logging.info(f"Task Updated: {task.to_dict()}")

    @staticmethod
    def log_task_completed(task):
        # Log information when a task is marked as completed
        logging.info(f"Task Completed: {task}")

    @staticmethod
    def log_task_deleted(id):
        # Log information when task is deleted by id
        logging.info(f"Task Deleted with Id: {id}")



