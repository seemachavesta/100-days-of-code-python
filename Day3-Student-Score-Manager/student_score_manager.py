print('Welcome to Student Score Management Program!')

#List of name and scores 
student_names = ['Priyanka', 'Rexy', 'Shonita', 'Jack', 'George', 'Maria', 'Ali']
student_scores = [74, 65, 45, 87, 96, 45, 58]

# Combine names and scores into a dictionary
student_information = dict(zip(student_names, student_scores))

# Filter graduated students (score >= 75) into a list of dictionaries
graduated_students = [{
  'name': name, 
  'Scores': score 
}
for name, score in student_information.items() if score >= 75
]

# Modifying the score and adding 5 points as bonus
score_with_bonus_mark = [
  score + 5 if score + 5 <= 100 else 100 for score in student_scores 
]

# Assigning grades based on bonus-modified scores
student_grades = [
  {'Score': score, 
    'Grade': 'A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'D'
  }
  for score in score_with_bonus_mark 
 ]

# Calculating the average scores
average = sum(score_with_bonus_mark) / len(score_with_bonus_mark)
print("Average Score:", average)

# Filtering out below average students
student_below_average = [name for name, score in student_information.items() if score < average]

print("Graduated Students:", graduated_students)
print("Students below average:", student_below_average)
