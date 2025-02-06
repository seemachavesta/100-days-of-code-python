import json

class QuizManager:
   
    def __init__(self, file_name="quiz.json"):
        self.file_name = file_name
        self.questions = self.load_questions()
        
        
    def load_questions(self):
        """
        Loads the quiz questions from a JSON file.

        If the file is not found, displays an error message and returns an empty list.

        Returns:
        list: A list of quiz questions if the file exists, otherwise an empty list.
        """
        try:
            with open(self.file_name, 'r') as file:
                result = json.load(file)
                return result
        except FileNotFoundError:
            print("Error: Quiz file not found!")
            return []
            
    def ask_question(self, data):
        """
        Displays a question and its answer options to the user.
        prompts the user user for answer

        Returns:
        str: The user's selected answer.
        """
        question = data['question']
        options = data['options']
            
        print("\n" + question)  # Print question
        for option in options:
            print(option)
        print()
        answer = input('Your answer: ')
        return answer
       
            
    def start_quiz(self):
        """
        Loops through the list of quiz questions.

        Checks if each answer is correct and updates the results accordingly.

        At the end of the quiz, displays the total count of correct and wrong answers.
        """
        if not self.questions:
            print('There is data in file')
            return
        results = {"correct": 0, "wrong": 0}
        for data in self.questions:
    
            answer =  self.ask_question(data)
            if data['answer'] == answer.lower():
                results['correct'] += 1
            else:
                results['wrong'] += 1
                
        print(f"You have guessed {results['correct']} Correct and {results['wrong']} Wrong answers.")
        
    
                
                
            
quiz = QuizManager()
quiz.start_quiz()