import streamlit as st

# Define colors
color_bg = "#f9f9f9"
color_text = "#333333"
color_primary = "#ff6347"

# Define page style
def page_style():
    st.markdown(
        f"""
        <style>
            .reportview-container {{
                background-color: {color_bg};
                color: {color_text};
            }}
            .css-1aumxhk {{
                font-size: 30px;
                color: {color_primary};
            }}
            .css-1aumxhk {{
                font-size: 24px;
                color: {color_text};
            }}
            .css-1t42vg9 {{
                background-color: {color_primary};
                color: white;
                border-radius: 20px;
                padding: 10px 20px;
                font-size: 24px;
                font-weight: bold;
                transition: background-color 0.3s ease;
            }}
            .css-1t42vg9:hover {{
                background-color: #e52d06;
                cursor: pointer;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# Define main app function
def main():
    # Set page style
    page_style()

    # Set app title and instructions
    st.title("Aptitude Test")
    st.markdown(
        """
        This is a test of your abilities in grammar, comprehension, and logical reasoning. 
        Please select the test you would like to take from the menu on the left.
        """
    )

    # Set menu options
    menu = ["Grammar Test", "Comprehension Test", "Logical Reasoning Test"]
    choice = st.sidebar.selectbox("Select Test", menu)

    # Render selected test page
    if choice == "Grammar Test":
        grammar_test()
    elif choice == "Comprehension Test":
        comprehension_test()
    elif choice == "Logical Reasoning Test":
        logical_reasoning_test()

# Define grammar test page
def grammar_test():
    st.title("Grammar Test")
    st.write("This is the grammar test page")
    # List of questions and answers
    questions = [    {     "question": "Which sentence is grammatically correct?",
        "options": ["A. I should of gone to the store.", "B. I should have gone to the store.", "C. I should of went to the store.", "D. I should of been gone to the store."],
        "answer": "B. I should have gone to the store."
    },
    {
        "question": "Which sentence is grammatically correct?",
        "options": ["A. The cake tastes goodly.", "B. The cake tastes good.", "C. The cake tastes well.", "D. The cake tastes deliciously."],
        "answer": "Answer: B. The cake tastes good.
    },
	{
        "question": "Which sentence is grammatically correct?",
        "options": ["A. My parents bought my brother and I a new car.", "B. My parents bought my brother and me a new car.", "C. My parents bought a new car for my brother and I.", "D. My parents bought a new car for my brother and me."],
        "answer": "Answer: D. My parents bought a new car for my brother and me."
    },
	{
        "question": "Which sentence is grammatically correct?",
        "options": ["A. She is the most prettiest girl in the class.", "B. She is the prettiest girl in the class.", "C. She is prettier than any girl in the class.", "D. She is more pretty than any girl in the class."],
        "answer": "Answer: B. She is the prettiest girl in the class."
    },
	{
        "question": "Identify the sentence that contains an error in subject-verb agreement:",
        "options": ["A. The group of students is studying hard for the exams.", "B. The book on the table belong to me.", "C. The dog barks loudly every morning.", "d. The choir sings beautifully during the concert."],
        "answer": "B. The book on the table belong to me."
    },
	{
        "question": "Choose the correct form of the verb to complete the sentence:\n The committee _____ to hold an emergency meeting next week.\n",
        "options": ["A. decides", "B. decide", "C. decided", "D. has decided"],
        "answer": "D. has decided"
    },
	{
        "question": "Which sentence is in the passive voice?",
        "options": ["A. The teacher graded the papers.", "B. The papers were graded by the teacher.", "C. The student wrote the essay.", "D. The essay was written by the student."],
        "answer": "B. The papers were graded by the teacher."
    },
	{
        "question": "Identify the sentence that contains an error in parallel structure:",
        "options": ["A. She enjoys hiking, swimming, and biking.", "B. He likes to eat pizza, pasta, and drinking soda.", "C. My sister is smart, funny, and kind.", "D. We need to focus on reducing costs, improving quality, and increasing efficiency."],
        "answer": "B. He likes to eat pizza, pasta, and drinking soda."
    },
	{
        "question": "Choose the correct form of the verb to complete the sentence:\n The team _____ the championship last year.\n",
        "options": ["A. win", "B. won", "C. have won", "D. had won"],
        "answer": "B. won"
    },
	{
        "question": "Identify the sentence that contains an error in pronoun agreement:\n ",
        "options": ["A. Everyone should do their part to help the environment.", "B. Each student must bring his or her own supplies to class.", "C. Someone left their umbrella in the hallway.", "D. Either of the options has its own advantages and disadvantages."],
        "answer": "C. Someone left their umbrella in the hallway."
    },
	{
        "question": "Choose the correct form of the verb to complete the sentence:\n The sun _____ in the east and _____ in the west.\n",
        "options": ["A. rises, set", "B. rose, setted", "C. rise, sets", "D. rises, sets"],
        "answer": "D. rises, sets"
    },
	{
        "question": "Identify the sentence that contains an error in punctuation:",
        "options": ["A. The concert was great; everyone enjoyed it.", "B. I bought a new car, but I still need to get it insured.", "C. She said, "I love you."", "D. We went to the beach, played in the water and ate ice cream."],
        "answer": "D. We went to the beach, played in the water and ate ice cream."
    },
	{
        "question": "Identify the sentence that contains an error in capitalization:",
        "options": ["A. I live on Main Street.", "B. My favorite color is blue.", "C. In the summer, we like to go to the beach.", "D. The statue of Liberty is a symbol of freedom."],
        "answer": "D. The statue of Liberty is a symbol of freedom."
    },
	{
        "question": "Choose the correct pronoun to complete the sentence:\n She gave the present to _____.\n",
        "options": ["A. he and I", "B. him and me", "C. he and me", "D. him and I"],
        "answer": "B. him and me"
    },
	{
        "question": "Choose the sentence that contains a misplaced modifier:",
        "options": ["A. While jogging, the dog chased the ball.", "B. The dog chased the ball while jogging.", "C. Chasing the ball, the dog was jogging.", "D. The jogging dog chased the ball."],
        "answer": "Answer: C. Chasing the ball, the dog was jogging."
    },
	
]

    # Function to show the questions and options
    def show_question(question_dict):
        st.write(question_dict["question"])
        user_answer = st.radio("Select an answer:", question_dict["options"], key=question_dict["question"])
        return user_answer

    # Function to calculate and display the score
    def calculate_score(answers):
        score = 0
        for i, ans in enumerate(answers):
            if ans == questions[i]["answer"]:
                score += 1
        st.write("Your score is: ", score)

    # Main App
    st.title("Aptitude Test")
    st.write("Answer the following questions:")

    answers = []
    for i, question in enumerate(questions):
        st.write(f"Question {i+1}")
        answers.append(show_question(question))

    if st.button("Submit"):
        calculate_score(answers)

# Define comprehension test page
def comprehension_test():
    st.title("Comprehension Test")
    st.write("This is the comprehension test page")
    # List of questions and answers
    questions = [    {        "question": "What is the capital of France?",        "options": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "What is the highest mountain in the world?",
        "options": ["Mount Kilimanjaro", "Mount Everest", "Mount Fuji", "Mount McKinley"],
        "answer": "Mount Everest"
    },
    {
        "question": "What is the currency of Japan?",
        "options": ["Dollar", "Pound", "Yen", "Euro"],
        "answer": "Yen"
    }
]

     # Function to show the questions and options
    def show_question(question_dict):
        st.write(question_dict["question"])
        user_answer = st.radio("Select an answer:", question_dict["options"], key=question_dict["question"])
        return user_answer

    # Function to calculate and display the score
    def calculate_score(answers):
        score = 0
        for i, ans in enumerate(answers):
            if ans == questions[i]["answer"]:
                score += 1
        st.write("Your score is: ", score)

    # Main App
    st.title("Aptitude Test")
    st.write("Answer the following questions:")

    answers = []
    for i, question in enumerate(questions):
        st.write(f"Question {i+1}")
        answers.append(show_question(question))

    if st.button("Submit"):
        calculate_score(answers)

# Define logical reasoning test page
def logical_reasoning_test():
    st.title("Logical Reasoning Test")
    st.write("This is the logical reasoning test page")
     # List of questions and answers
    questions = [    {        "question": "What is the capital of France?",        "options": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "What is the highest mountain in the world?",
        "options": ["Mount Kilimanjaro", "Mount Everest", "Mount Fuji", "Mount McKinley"],
        "answer": "Mount Everest"
    },
    {
        "question": "What is the currency of Japan?",
        "options": ["Dollar", "Pound", "Yen", "Euro"],
        "answer": "Yen"
    }
]
 
    # Function to show the questions and options
    def show_question(question_dict):
        st.write(question_dict["question"])
        user_answer = st.radio("Select an answer:", question_dict["options"], key=question_dict["question"])
        return user_answer

    # Function to calculate and display the score
    def calculate_score(answers):
        score = 0
        for i, ans in enumerate(answers):
            if ans == questions[i]["answer"]:
                score += 1
        st.write("Your score is: ", score)

    # Main App
    st.title("Aptitude Test")
    st.write("Answer the following questions:")

    answers = []
    for i, question in enumerate(questions):
        st.write(f"Question {i+1}")
        answers.append(show_question(question))

    if st.button("Submit"):
        calculate_score(answers)

#Add a footer
 # Add footer
    with st.container():
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("Sample Aptitude test for evans")
        st.write("Copyright © 2023")
        st.write("")
        st.write("")
        st.write("")

# Run the main app function
if __name__ == "__main__":
    main()
