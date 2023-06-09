# from quiz_runner import play_quiz
from quiz_manager import play_quiz
from topic_choice import get_topic_choice

if __name__ == "__main__":
    topic = get_topic_choice()
    play_quiz(topic)