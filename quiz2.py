def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in question:
        print("--------------------------------------------")
        print(key)
        for i in Options[question_num-1]:
            print(i)
        guess = input("Enter A, B, C OR D: ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(question.get(key), guess)
        question_num +=1

    display_score(correct_guesses, guesses)
#--------------------------------------------
def check_answer(answers, guess):
    if answers == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0

#--------------------------------------------
def display_score(correct_guesses, guesses):
    print("--------------------------------------------")
    print("Results: ")
    print("--------------------------------------------")

    print("Answers: ", end=" ")
    for i in question:
        print(question.get(i),end= " ")
    print()

    print("Guess :",end= " ")
    for i in guesses:
        print(i,end= " ")
    print()

    score = int((correct_guesses/len(question))*100)
    print("Your score is : "+str(score) + "% ")



#--------------------------------------------
def play_again():
    responese = input("Do You want to play again? (Y/N) : ")
    responese.upper()

    if responese == "Y":
        return True
    else:
        return False
#--------------------------------------------





question = {"What come after A ?: ": "B",
            "Is the Earth round ? :": "A",
            "Is the moon round? :": "C",
            "what sound does the dog make?: ":"D"}

Options = [["A. a", "B. b", "C. c", "D. d"],
           ["A. Yes", "B. No", "C. maybe", "D. idk"],
           ["A. No", "B. idk", "C. Yes", "D. maybe"],
           ["A. meow", "B. chirp ", "C. Quack ", "D. woof"]]

new_game()
while play_again():
    new_game()

print("Bye!")