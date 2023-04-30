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
ft = """
<style>
a:link , a:visited{
color: #BFBFBF;
background-color: transparent;
text-decoration: none;
}

footer{
    visibility:hidden;
}

.footer {
position: relative;
left: 2px;
top: 480px;
bottom: 0;
width: 100%;
background-color: transparent;
color: #808080; 
text-align: center; 
}
</style>



<div class="footer">
<p style='font-size: 1em;'><b><i> Made for Evans</i></b></p>
</div>

</div>
"""
st.write(ft, unsafe_allow_html=True)

# Run the main app function
if __name__ == "__main__":
    main()
