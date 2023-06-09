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