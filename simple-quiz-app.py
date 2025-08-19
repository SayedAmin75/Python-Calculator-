def quiz_app():
    questions = {
        "What is the capital of France? ": "Paris",
        "What is 5 + 7? ": "12",
        "What is the color of the sky? ": "Blue",
    }

    score = 0
    for question, answer in questions.items():
        user_answer = input(question)
        if user_answer.strip().capitalize() == answer:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is {answer}.")

    print(f"\nYour final score: {score}/{len(questions)}")

quiz_app()
