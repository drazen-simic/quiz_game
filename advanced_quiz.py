import random
import time

# Question bank
data = {
    "easy": [
        {"question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "answer": ["4"]},
        {"question": "What color is the sky?", "options": ["Blue", "Green", "Red", "Yellow"], "answer": ["Blue"]},
        {"question": "What are the primary colors?", "options": ["Red", "Blue", "Purple", "Pink"], "answer": ["Red", "Blue"]},
        {"question": "Which are the continents on Earth?", "options": ["Africa", "Europe", "Catalonia", "Australia"], "answer": ["Africa", "Europe", "Australia"]}
    ],
    "medium": [
        {"question": "What is the capital of France?", "options": ["Berlin", "Madrid", "Paris", "Rome"], "answer": ["Paris"]},
        {"question": "What is 5 * 6?", "options": ["30", "25", "35", "40"], "answer": ["30"]},
        {"question": "What are the names of Teletubbies Characters?", "options": ["Tinky Winky and Dipsy", "Laa-Laa and Po", "Pikachu and Charizard", "Sponge Bob Squarepants and Patrick Star"], "answer": ["Tinky Winky and Dipsy", "Laa-Laa and Po"]},
        {"question": "What are the official languages of the European union?", "options": ["English", "German", "Japanese", "Dutch"], "answer": ["English", "German", "Dutch"]}
    ],
    "hard": [
        {"question": "What is the square root of 144?", "options": ["10", "11", "12", "13"], "answer": ["12"]},
        {"question": "Who wrote '1984'?", "options": ["George Orwell", "Aldous Huxley", "Ray Bradbury", "Jules Verne"], "answer": ["George Orwell"]},
        {"question": "What types of nucleic acids are there?", "options": ["RNA", "DNA", "URL", "ATP"], "answer": ["RNA", "DNA"]},
        {"question": "What are Nikola Tesla's inventions?", "options": ["Induction motor", "Radio", "Phonograph", "Light bulb"], "answer": ["Induction motor", "Radio"]}
    ]
}

# List of best results
leaderboard = []

def display_leaderboard():
    print("\n--- Leaderboard ---")
    if not leaderboard:
        print("No scores yet. Be the first!")
    else:
        for i, entry in enumerate(sorted(leaderboard, key=lambda x: x['score'], reverse=True), 1):
            print(f"{i}. {entry['name']} - {entry['score']}")
    print("-------------------\n")

def start_quiz():
    print("Welcome to the Quiz!")
    name = input("Please enter your name: ")
    print(f"Hello, {name}! Let's start the quiz.")

    # difficulty selection
    level = input("Choose difficulty (easy, medium, hard): ").lower()
    while level not in data:
        level = input("Invalid choice. Choose difficulty (easy, medium, hard): ").lower()

    # selection of questions
    questions = data[level]
    random.shuffle(questions)  # Promiješaj pitanja

    score = 0
    
    for q in questions:
        print(f"\n{q['question']}")
        for i, option in enumerate(q['options'], 1):
            print(f"{i}. {option}")

        try:
            start_time = time.time()
            answer = input("Your answer(s) (comma-separated, e.g., 1,2): ").split(',')
            elapsed_time = time.time() - start_time

            if elapsed_time > 10:
                print("Time's up! Moving to the next question.")
                continue

            # check the answers
            user_answers = [q['options'][int(a.strip()) - 1] for a in answer if a.strip().isdigit() and int(a.strip()) in range(1, len(q['options']) + 1)]
            if set(user_answers) == set(q['answer']):
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect! The correct answers were: {', '.join(q['answer'])}")
        except (ValueError, IndexError):
            print("Invalid input. Moving to the next question.")

    print(f"\nQuiz Over! Your score: {score}/{len(questions)}")

    # add the score to the scale
    leaderboard.append({"name": name, "score": score})

    # show the scale
    display_leaderboard()

    # repeating the quiz
    replay = input("Do you want to play again? (yes/no): ").lower()
    if replay == "yes":
        start_quiz()
    else:
        print("Thank You and goodbye!")

# start the quiz
if __name__ == "__main__":
    start_quiz()
