class Quiz:
    def __init__(self, topic):
        self.topic = topic
        self.questions = []
        self.answers = []
        self.correct_answers = []
        self.user_responses = []

    def add_question(self, question, answer, correct_answer):
        # Add new question, answer options, and correct answer to the quiz
        self.questions.append(question)
        self.answers.append(answer)
        self.correct_answers.append(correct_answer)

    def run_quiz(self):
        # Run the quiz
        print("Welcome to the " + self.topic + " quiz!")
        name = input('Please enter your name: ')
        score = 0

        # Loop through each question in the quiz
        for i in range(len(self.questions)):
            # print("\nQuestion " + str(i + 1) + ": " + self.questions[i])
            print("\nQuestion ", i+1, ": ", self.questions[i])
            print("Answers:", self.answers[i])
            
            # Validate user response
            while True:
                user_answer = input("Your answer (Enter the corresponding letter or press Enter to skip): ")
                if user_answer == "" or user_answer.lower() in ["a", "b", "c", "d"]:
                    break
                else:
                    print("Please enter a valid answer or press Enter to skip!")

           # If skipped, print text
            if user_answer == "":
                print("Question skipped!")
                self.user_responses.append(None)
                continue

            self.user_responses.append(user_answer)

           # Update score if the response is correct
            if self.user_responses[i] is not None and self.user_responses[i].lower() == self.correct_answers[i].lower():
                print("Correct!")
                score += 1
            else:
                print("Incorrect!")

        # Print the user's score
        print("\nQuiz completed!")
        print("Name: " + name)
        print("Score:", score, "out of", (len(self.questions)))
        print("Percentage score:", (score / len(self.questions)) * 100, "%")

        #Return incorrect and correct quiz results
        print("\nQuestion Results:")
        for i in range(len(self.questions)):
            print("\nQuestion " + str(i + 1) + ": " + self.questions[i])
            if self.user_responses[i] is not None:
                print("Your answers:", self.answers[i][ord(self.user_responses[i].lower()) - ord('a')])
            else:
                print("Skipped!")
            print("Correct answer:", self.correct_answers[i])

        return score, name


# UNIT TESTS
### Test adding a question:
# quiz = Quiz("History")
# quiz.add_question("Who was the first president of the United States?",
# ["A. George Washington", "B. Abraham Lincoln", "C. Thomas Jefferson",
# "D. John Adams"], "A")
# assert len(quiz.questions) == 1
# assert len(quiz.answers) == 1
# assert len(quiz.correct_answers) == 1

# ## Test running the quiz with correct answers and skipping a question:
# quiz = Quiz("Math")
# quiz.add_question("What is 1 + 1?", ["A. 1", "B. 2", "C. 3", "D. 4"], "B")
# quiz.add_question("What is 2 + 2?", ["A. 2", "B. 4", "C. 6", "D. 8"], "B")
# score, name = quiz.run_quiz()
# assert score == 2
# assert score == 0
# assert name != ""