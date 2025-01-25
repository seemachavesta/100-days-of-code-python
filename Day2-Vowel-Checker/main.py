# This function checks how many vowels are in a word or sentence
def vowel_checker(user_input):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    counter = 0
    # Looping over each letter in the user's input
    for letter in user_input:
        if letter in vowels:
            counter += 1
           
    print(f'There are {counter} vowels.')

# This loop keeps repeating until the user chooses to stop
while True:
    print('Welcome to the vowel checker!')

    # Taking input from the user and converting it to lowercase
    user_input = input('Enter a word or sentence: ').lower()

    # Check if the user input is empty or only contains spaces
    if not user_input.strip():
        print("Input cannot be empty. Please try again.")
        continue

    # Call the function to count vowels in the user's input
    vowel_checker(user_input)

    # Asking the user if they want to play again
    choice = input('Would you like to play again? (y/n): ').lower()
    if choice != 'y':
        print('Thanks for playing. Goodbye!')
        break



    
