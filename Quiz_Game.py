
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
    {
        "question": "What language is used to create Android apps?",
        "options": ["A. Python", "B. Swift", "C. Kotlin", "D. Ruby"],
        "answer": "C"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["A. Charles Dickens", "B. William Shakespeare", "C. Mark Twain", "D. Jane Austen"],
        "answer": "B"
    }
]


def run_quiz():
    print("\n🎯 Welcome to the Quiz Game!")
    score = 0

    for index, q in enumerate(questions, start=1):
        print(f"\nQ{index}: {q['question']}")
        for option in q['options']:
            print(option)

        user_answer = input("Your answer (A/B/C/D): ").upper()

        if user_answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}")

    print("\n📊 Quiz Completed!")
    print(f"Your final score is: {score}/{len(questions)}")


# Run the quiz
if __name__ == "__main__":
    run_quiz()
