import random
import time



def ask_question(question, answer):
    """Ask a single question and return True if the answer is correct."""
    user_answer = input(question + " ").strip().lower()
    return user_answer == answer.lower()

def run_quiz():
    """Run the quiz game."""
    questions = [
        ("What is the capital of France?", "Paris"),
        ("What is 5 + 7?", "12"),
        ("What is the color of the sky on a clear day?", "Blue"),
    ]
    score = 0

    print("Welcome to the Quiz Game!")
    print("Answer the following questions:\n")

    for question, answer in questions:
        if ask_question(question, answer):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {answer}.")

    print(f"\nYou scored {score} out of {len(questions)}.")
    return score

def main():
    """Main function to allow replay."""
    while True:
        run_quiz()
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing the Quiz Game!")
            break

if __name__ == "__main__":
    main()
