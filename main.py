# Importing the necessary classes and data
from question_model import Question  # Import the Question class
from data import question_data  # Import the question data
from quiz_brain import QuizBrain  # Import the QuizBrain class

# Create an empty list to store questions
question_bank = []

# Loop through each question in the question data
for question in question_data:
    # Extract the question text and answer
    question_text = question["text"]
    question_answer = question["answer"]
    # Create a new Question object with the extracted text and answer
    new_question = Question(question_text, question_answer)
    # Add the new question object to the question_bank list
    question_bank.append(new_question)

# Create a QuizBrain object with the list of questions
quiz = QuizBrain(question_bank)

# Ask the first question
quiz.next_question()

# Loop through the remaining questions as long as there are questions left
while quiz.still_has_questions():
    quiz.next_question()

# Print a message indicating the quiz is complete
print("\n")
print("You have completed the quiz")
# Print the final score of the user
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
