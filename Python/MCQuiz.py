#Building a Multiple Choice Quiz
from Question import Question

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\nAnswer: ",
    "What color are Banana?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\nAnswer: ",
    "What color are Strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\nAnswer: "
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

def run_test(questions):
    score = 0 
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    if score >= len(questions)/2:       
        print("You got " + str(score) + "/" + str(len(questions)) + " correct, congrats you've passed.")
    else:
        print("You've only gotten " + str(score) + "/" + str(len(questions)) + " correct, sorry you've failed.")

run_test(questions)