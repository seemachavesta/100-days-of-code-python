
#Calculate the factorial of a number
def calculate_factorial(n):
  if n < 0:
    print("Factorial is not defined for negative numbers.")
    return 
  
  if n == 0:
    print("The value of factorial is 1 (0! = 1).")
    return

  # Initialize: Set factorial = 1.
  factorial = 1
  for number in range(1, n + 1):
    factorial *= number
    
  print(f'The value of factorial is {factorial}')
  


while True:
  
  print("Welcome to the Factorial Calculator!")
  print("This program allows you to calculate the factorial of any non-negative number.")
  print("Enter a number to get started, and you can calculate as many factorials as you'd like!")
  print("-" * 50)
  
  try:
    user_input = int(input("Enter a number: "))
    print()# Adds a blank line to separate sections
  except ValueError:
    print('Not a valid number')
    continue
  
  calculate_factorial(user_input)
  
  # Choice validation loop
  while True:
    print()
    choice = input("Would you like to calculate another factorial? (y/n): ").lower()
    if choice in ['y', 'n']:
      break  # Exit the choice loop if valid input is provided
    else:
      print("Invalid choice. Please enter 'y' for yes or 'n' for no.")
    
  if choice == 'n':
    print("Goodbye!")
    break
  