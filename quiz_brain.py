class QuizBrain:
    # Constructor to initialize the QuizBrain object with the list of questions
    def __init__(self, q_list):
        self.score = 0  # Initialize score to 0
        self.question_number = 0  # Initialize the question number to 0
        self.question_list = q_list  # Store the list of questions

    # Method to check if there are still questions left to be answered
    def still_has_questions(self):
        return self.question_number < len(self.question_list)  # Return True if there are more questions

    # Method to ask the next question in the quiz
    def next_question(self):
        # Get the current question based on the question number
        current_question = self.question_list[self.question_number]
        self.question_number += 1  # Increment the question number
        # Prompt the user for an answer
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")  
        # Check if the user's answer is correct
        self.check_answer(user_answer, current_question.answer)

    # Method to check the user's answer against the correct answer
    def check_answer(self, user_answer, correct_answer):
        # If the user's answer matches the correct answer, increase the score
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it Right")
        else:
            print("That's wrong")
        # Print the correct answer and the current score
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")  # Print a new line for better readability



