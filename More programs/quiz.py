# List of quiz questions. Each question is a dictionary with 'question', 'choices', and 'answer' keys.
quiz_questions = [
    {"question": "A set of rules which defines the ways in which words can be coupled in sentences is called:", "choices": ["lexis", "syntax", "semantics", "dictionary"], "answer": "syntax"},
    {"question": "Which of the following expressions evaluate to a non-zero result? (Select two answers.)", "choices": ["2**3-2", "4/2**3-2", ".1**3/4-1", "1*4//2**3"], "answer": ["2**3-2", "4/2**3-2"]},
    {"question": "Python is an example of which programming language category?", "choices": ["interpreted", "assembly", "compiled", "machine"], "answer": "interpreted"},
    {"question": "How many hashes (+) does the code output to the screen?", "choices": ["one", "zero (the code outputs nothing)", "five", "three"], "answer": "five"},
    {"question": "What happens when the user runs the following code?", "choices": ["The code outputs 3.", "The code outputs 2.", "The code enters an infinite loop.", "The code outputs 1."], "answer": "The code outputs 2."},
    {"question": "What is the expected output of the following code?", "choices": ["The code produces no output.", "***", "**", "*"], "answer": "**"},
    {"question": "What is the expected output of the following code?", "choices": ["The code is erroneous and cannot be run.", "20", "10", "30"], "answer": "The code is erroneous and cannot be run."},
    {"question": "Which of the following functions can be invoked with two arguments?", "choices": ["Option A", "Option B", "Option C", "Option D"], "answer": "Option B"},
    {"question": "Which of the following are the names of Python passing argument styles? (Select two answers.)", "choices": ["keyword", "reference", "indicatory", "positional"], "answer": ["keyword", "positional"]},
    {"question": "What is the expected output of the following code?", "choices": ["2", "0", "3", "1"], "answer": "1"}
]

# Iterate through each question in the quiz_questions list
for question_dict in quiz_questions:
    # Print the question
    print(question_dict["question"])
    
    # Print all the possible choices for the current question
    for idx, choice in enumerate(question_dict["choices"], start=1):
        print(f"{idx}. {choice}")
        
    # Flag to track whether the user has given the correct answer
    answer_correct = False
    
    # Keep asking for user input until the correct answer is given
    while not answer_correct:
        try:
            # Ask user for their answer and attempt to convert it to an integer
            user_answer = int(input("Enter the number of your answer: ")) - 1
            
            # Check if the user's answer matches the correct answer
            if question_dict["choices"][user_answer] == question_dict["answer"]:
                print("Correct!")
                answer_correct = True  # User got the answer right, exit the loop
            else:
                print("Incorrect.")
        except (ValueError, IndexError):
            # Handle any errors caused by invalid input
            print("Invalid input. Please enter a valid choice number.")
