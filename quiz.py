import random

def generate_question():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(['+', '-', '*', '/'])
    question = f"What is {num1} {operator} {num2}?"
    if operator == '/':
        answer = num1 / num2
        answer = round(answer, 2)  # Limit decimal places to 2
    else:
        answer = eval(f"{num1}{operator}{num2}")
    return question, answer

def quiz():
    score = 0
    for i in range(5):
        question, answer = generate_question()
        user_answer = input(question + " ")
        try:
            user_answer = float(user_answer)  # Convert input to float
            if user_answer == answer:
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect! The correct answer is {answer}.")
        except ValueError:
            print("Invalid input! Please enter a number.")
    print(f"Quiz completed! Your score is {score}/5.")

if __name__ == "__main__":
    quiz()
