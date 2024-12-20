from customError import InvalidRoleError
from employee import Manager, Intern, Developer

class EmployeeManager:
    def __init__(self):
        self.employee_list = {}

    
    def add_employee(self, employee):
        employee_roles = (Manager, Developer, Intern)
        if not isinstance(employee, employee_roles):
            raise InvalidRoleError(f'{employee} is not a valid Employee role. Valid roles are Manager, Developer, or Intern.')

        if employee.id in self.employee_list:
            print('Employee already exist.')
        else:
            self.employee_list[employee.id] = employee
            print(f'Employee with id {employee.id} has been added successfully.')


    # Display all the employees from employee list
    def display_employee_list(self):
        #check if employee list is empty
        if not self.employee_list:
            print('No employees in the list.')
            return 
        #looping over the employee list and printing all employees. 
        for employee in self.employee_list.values():
            print(employee)


    #Remove employee from employee list 
    def remove_employee(self, employee_id):
        if employee_id in self.employee_list:
            del self.employee_list[employee_id]
            print(f'Employee with id {employee_id} has been deleted')
        
        else:
            print(f'Employee with id {employee_id} does not exist.')
        

    # Search employee with employee id
    def search_employee(self, id):
        if id in self.employee_list:
            return self.employee_list[id] 
        else:
            print(f'Employee with Id {id} does not exist')
            return None
                

        



# Test the functionality
# Create an instance of EmployeeManager
employee_manager = EmployeeManager()


manager = Manager(1, 'George', 'Manager', 10)
developer = Developer(2, 'Reena', 'Developer', 'Python')
intern = Intern(3, 'Shaun', 'intern', '3 Months')


try:
    employee_manager.add_employee(manager)
    employee_manager.add_employee(developer)
    employee_manager.add_employee(intern)   
except TypeError as e:
    print(e)


employee_manager.display_employee_list()

employee_manager.search_employee(5)
employee_manager.remove_employee(manager.id)

employee_manager.display_employee_list()