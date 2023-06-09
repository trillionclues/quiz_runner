from quiz_class import Quiz

# List of available quiz topics
topics = ["History", "Math", "Science"]

from quiz_class import Quiz

# List of available quiz topics
topics = ["History", "Math", "Science"]

def get_topic_choice():
    # Print available topics for selection
    print("Available quiz topics:")
    for index, topic in enumerate(topics):
        print(f"{index + 1}. {topic}")
    
    while True:
        try:
            choice = int(input("Choose a topic number: "))
            if choice < 1 or choice > len(topics):
                print("Invalid choice. Please enter a valid topic number.")
            else:
                return topics[choice - 1]
        except ValueError:
            print("Invalid input. Please enter a valid topic number.")
