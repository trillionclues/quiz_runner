import sys
from quiz_class import Quiz

def play_quiz(topic):
    quiz = Quiz(topic)

    # Add questions to the quiz based on the selected topic

    #History questions
    if topic == "History":
        quiz.add_question("Who was the first president of the United States?", ["A. George Washington", "B. Abraham Lincoln", "C. Thomas Jefferson", "D. John Adams"], "A")
        quiz.add_question("Who was the first president of the Philippines?", ["A. Manuel L. Quezon", "B. Emilio Aguinaldo", "C. Sergio Osmeña", "Manuel Roxas"], "B")
        quiz.add_question("Who was the first president of the Republic of China?", ["A. L. Li Yuanhong", "B.Yuan Shikai", "C.  Chiang Kai-shek", "Sun Yat-sen"], "D")
        quiz.add_question("Who is the current holder of the title 'World's Oldest Person'?", ["A. Kane Tanaka", "B. Jeanne Calment", "C. Sarah Knauss", "D. Nabi Tajima"], "A")
        quiz.add_question("Who was the first person to set foot on the moon?", ["A. Buzz Aldrin", "B. Neil Armstrong", "C. Alan Shepard", "D. John Glenn"], "B")
        quiz.add_question("Who was the first person to climb Mount Everest?", ["A. Reinhold Messner", "B. Tenzing Norgay", "C. George Mallory", "D. Edmund Hillary"], "D")
        quiz.add_question("Who was the first person to sail around the world?", ["A. Ferdinand Magellan", "B. Francis Drake", "C. James Cook", "D. Vasco da Gama"], "A")
        quiz.add_question("Who was the first person to reach the South Pole?", ["A. Roald Amundsen", "B. Robert Falcon Scott", "C. Ernest Shackleton", "D. Richard Byrd"], "A")
        quiz.add_question("Who was the first person to reach the North Pole?", ["A. Richard Byrd", "B. Frederick Cook", "C. Robert Peary", "D. Matthew Henson"], "C")
        quiz.add_question("Who was the first person to reach the summit of Mount Everest without supplemental oxygen?", ["A. Reinhold Messner", "B. Peter Habeler", "C. Ang Rita Sherpa", "D. Phurba Tashi Sherpa"], "A")
        # Add more history questions
    
    #Math questions
    elif topic == "Math":
        quiz.add_question("What is 1 + 1?", ["A. 1", "B. 2", "C. 3", "D. 4"], "B")
        quiz.add_question("What is 2 + 2?", ["A. 12", "B. 3", "C. 4", "D. 5"], "C")
        quiz.add_question("What is 3 + 3?", ["A. 3", "B. 4", "C. 4", "D. 6"], "D")
        quiz.add_question("What is 4 + 4?", ["A. 5", "B. 7", "C. 33", "D. 8"], "D")
        quiz.add_question("What is 5 + 5?", ["A. 10", "B. 55", "C. 15", "D. 4"], "A")
        quiz.add_question("What is 6 + 6?", ["A. 660", "B. 122", "C. 12", "D. 22"], "C")
        quiz.add_question("What is 7 + 7?", ["A. 14", "B. 22", "C. 31", "D. 29"], "A")
        quiz.add_question("What is 8 + 8?", ["A. 19", "B. 16", "C. 3", "D. 88"], "B")
        quiz.add_question("What is 9 + 9?", ["A. 90", "B. 10", "C. 44", "D. 18"], "D")
        quiz.add_question("What is 10 + 10?", ["A. 14", "B. 20", "C. 30", "D. 29"], "B")
        # Add more math questions

    #Science questions
    elif topic == "Science":
        quiz.add_question("What is the chemical symbol for gold?", ["A. Au", "B. Ag", "C. Cu", "D. Fe"], "A")
        quiz.add_question("What is the chemical symbol for silver?", ["A. Au", "B. Ag", "C. Cu", "D. Fe"], "B")
        quiz.add_question("What is the chemical symbol for copper?", ["A. Au", "B. Ag", "C. Cu", "D. Fe"], "C")
        quiz.add_question("What is the chemical symbol for iron?", ["A. Au", "B. Ag", "C. Cu", "D. Fe"], "D")
        quiz.add_question("What is the chemical symbol for magnesium?", ["A. Na", "B. Mg", "C. Al", "D. Si"], "B")
        quiz.add_question("What is the chemical symbol for sodium?", ["A. Na", "B. Mg", "C. Al", "D. Si"], "A")
        quiz.add_question("What is the chemical symbol for aluminum?", ["A. Na", "B. Mg", "C. Al", "D. Si"], "C")
        quiz.add_question("What is the chemical symbol for silicon?", ["A. Na", "B. Mg", "C. Al", "D. Si"], "D")
        quiz.add_question("What is the chemical symbol for chlorine?", ["A. Cl", "B. Br", "C. I", "D. F"], "A")
        quiz.add_question("What is the chemical symbol for bromine?", ["A. Cl", "B. Br", "C. I", "D. F"], "B")
        # Add more science questions

    users = []
    while True:
        name, score = quiz.run_quiz()
        try:
            score = int(score)
        except ValueError:
            score = 0
        users.append((name, score))
        play_again = input("Would you like to play again? (yes/no) ")

        # # Exit the program if the player selects "no"
        if play_again.lower() != "yes":
            sys.exit(0)

    print("\nFinal Scores:")
    users.sort(key=lambda x: x[1], reverse=True)
    for user in users:
        print("Name:", user[0])
        print("Score:", user[1])

    total_users = len(users)
    total_score = sum(score for _, score in users)
    average_score = total_score / total_users
    print("Total users:", total_users)
    print("Average score:", average_score)
    
    # Display all questions and correct answers
    print("\nQuestions and Correct Answers:")
    for question, answer in answers:
        print(question)
        print("Correct Answer:", answer)
        print()