quiz_questions = [
    {"question": "A set of rules which defines the ways in which words can be coupled in sentences is called:", "choices": ["lexis", "syntax", "semantics", "dictionary"], "answer": "syntax"},
    {"question": "Which of the following expressions evaluate to a non-zero result? (Select two answers.)", "choices": ["2**3-2", "4/2**3-2", ".1**3/4-1", "1*4//2**3"], "answer": ["2**3-2", "4/2**3-2"]}
]

for question_dict in quiz_questions:
    print(question_dict["question"])
    for idx, choice in enumerate(question_dict["choices"], start= 1):
        print(f"{idx}. {choice}")
        
    answer_correct = False
    
    while not answer_correct: 
        try:
            user_answer = int(input("Enter the number of your answer: ")) -1
            if question_dict["choices"][user_answer] == question_dict["answer"]:
                print("Correct!")
                answer_correct = True
            else:
                print("Incorrect.")
        except (ValueError, IndexError):
                print("Invalid input.")