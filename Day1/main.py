# Finds if the number is prime or not
def isPrime(user_input):
    for n in range(2, int(user_input ** 0.5) + 1):
        if user_input % n == 0:
            print(f"{user_input} equals {n} * {user_input // n}")
            print("Composite")
            break
    else:
        print("Prime")


while True:
    print("Welcome to the Prime or Composite Number Checker!")
    try:
        user_input = int(input("Enter a number: "))
    except ValueError:
        print("Not a valid number, try again.")
        continue

    # Handle numbers less than or equal to 1
    if user_input <= 1:
        print("Numbers less than or equal to 1 are not prime or composite.")
        continue

    # Check if the number is prime or composite
    isPrime(user_input)

    # Ask the user if they want to continue
    choice = input("Would you like to continue? (y/n): ").lower()
    if choice != 'y':
        print("Thanks, Goodbye!")
        break

        
    





    