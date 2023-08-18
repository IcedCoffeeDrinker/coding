from Question import Question

question_prompts = [
    "How high is the Mount Everest?\n(a) 9683 meters\n(b) 8849 meters\n(c) 8657 meters\nanswer: ",
    "How many states has the Earth?\n(a) 195 states\n(b) 211 states\n(c) 263 states\nanswer: ",
    "How difficult ist this pogram to write?\n(a) easy\n(b) hard\n(c) I don't know\nanswer: "
]

questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "c")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " answers correct.")

run_test(questions)