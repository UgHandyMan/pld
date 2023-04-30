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
    questions = [    {     "question": "Which sentence uses the correct article?",
        "options": ["A.  He is a European citizen.", "B. He is an European citizen.", "C. He is the European citizen.", "D. He is of European citizen."],
        "answer": "A.  He is a European citizen."
    },
    {
        "question": "Which sentence uses the correct pronoun case?",
        "options": ["A. Whom is she going to the party with?", "B. Who is she going to the party with?", "C. With who is she going to the party?", "D. Whose is she going to the party with?"],
        "answer": "B. The cake tastes good."
    },
	{
        "question": "Identify the conjunction in the following sentence: \"I ate dinner and watched TV.\"",
        "options": ["A.  I", "B. Ate", "C. And", "D. Watched"],
        "answer": "C. And"
    },
	{
        "question": "Which sentence is grammatically correct?",
        "options": ["A. She is the most prettiest girl in the class.", "B. She is the prettiest girl in the class.", "C. She is prettier than any girl in the class.", "D. She is more pretty than any girl in the class."],
        "answer": "B. She is the prettiest girl in the class."
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
        "options": ["A. The concert was great; everyone enjoyed it.", "B. I bought a new car, but I still need to get it insured.", "C. She said, \"I love you.\"", "D. We went to the beach, played in the water and ate ice cream."],
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
        "answer": "C. Chasing the ball, the dog was jogging."
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
	st.markdown(
        """
        Please read the story carefully before attempting to answer the questions.


The sun was setting over the mountains as John sat outside his cabin, sipping a cup of hot tea.
He had been living alone in the wilderness for the past three years, and he loved every minute of it. 
The silence, the fresh air, and the stunning views made him feel more alive than ever.

As he sat there, lost in thought, he heard a rustling sound coming from the bushes. 
He froze, listening intently, and heard it again. 
Slowly, he got up and walked towards the bushes, his heart racing. What could it be?

Suddenly, a small, scruffy-looking dog appeared from behind the bushes, wagging its tail. 
John breathed a sigh of relief and smiled. 
The dog looked hungry and scared, and John knew he had to help it.

He gave the dog some food and water, and soon enough, it was wagging its tail and barking happily. 
John decided to keep the dog and named it Rusty. 
Rusty became John's constant companion and soon learned to love the wilderness as much as John did.
        """
    )

    # List of questions and answers
    questions = [    {       "question": "What was John doing when the story began?",
        "options": ["A. Hunting", "B. Fishing", "C. Sitting outside his cabin", "D. None of the above"],
        "answer": "C. Sitting outside his cabin"
    },
	{
        "question": "How long had John been living alone in the wilderness?",
        "options": ["A. One year", "B. Two years", "C. Three years", "D.  Four years"],
        "answer": "C. Three years"
    },
	{
        "question": "What did John love about living in the wilderness?",
        "options": ["A. The silence", "B. The fresh air", "C. The stunning views", "D.  All of the above"],
        "answer": "D.  All of the above"
    },
	{
        "question": "What did John hear coming from the bushes?",
        "options": ["A. The wind blowing", "B. A rustling sound", "C. A river flowing", "D. None of the above"],
        "answer": "B. A rustling sound"
    },
	{
        "question": "What did John find behind the bushes?",
        "options": ["A.  A deer", "B. A bear", "C. A small, scruffy-looking dog", "None of the above"],
        "answer": "C. A small, scruffy-looking dog"
    },
	{
        "question": "How did John feel when he heard the rustling sound?",
        "options": ["A. Scared", "B. Excited", "C. Anxious", "D. Happy"],
        "answer": "A. Scared"
    },
	{
        "question": "What did John do to help the dog?",
        "options": ["A. He gave it some bread and drinks", "B. He gave it some food and water", "C. He chased it away", "D.  He ignored it"],
        "answer": "B. He gave it some food and water"
    },
	{
        "question": "What did John name the dog?",
        "options": ["A. Scruffy", "B. Rex", "C. Rusty", "D. Spot"],
        "answer": "C. Rusty"
    },
	{
        "question": "What did Rusty become for John?",
        "options": ["A.  His enemy", "B. His constant companion", "C. His prey", "D. None of the above"],
        "answer": "B. His constant companion"
    },
	{
        "question": "What did Rusty learn to love?",
        "options": ["A. The city life", "B. The countryside", "C. The Forest", "D. The wilderness"],
        "answer": "D. The wilderness"
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
