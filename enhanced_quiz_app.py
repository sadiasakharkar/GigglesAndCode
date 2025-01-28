import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# List of questions, options, correct answers, explanations, and categories
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "correct_answer": "Paris",
        "explanation": "Paris is the capital city of France, known for landmarks like the Eiffel Tower.",
        "category": "Geography"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Mars", "Jupiter", "Saturn"],
        "correct_answer": "Mars",
        "explanation": "Mars is called the Red Planet because of its reddish appearance due to iron oxide (rust) on its surface.",
        "category": "Science"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Homer"],
        "correct_answer": "William Shakespeare",
        "explanation": "William Shakespeare is the famous playwright who wrote 'Romeo and Juliet'.",
        "category": "Literature"
    },
    {
        "question": "What is the value of Pi (π) up to 2 decimal places?",
        "options": ["3.14", "3.15", "3.16", "3.17"],
        "correct_answer": "3.14",
        "explanation": "Pi (π) is approximately 3.14 and is used in calculations involving circles.",
        "category": "Math"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["Oxygen", "Osmium", "Ozone", "Oganesson"],
        "correct_answer": "Oxygen",
        "explanation": "Oxygen is a chemical element with the symbol 'O' and is essential for breathing.",
        "category": "Science"
    },
    {
        "question": "Which artist painted the 'Mona Lisa'?",
        "options": ["Pablo Picasso", "Leonardo da Vinci", "Vincent van Gogh", "Claude Monet"],
        "correct_answer": "Leonardo da Vinci",
        "explanation": "Leonardo da Vinci is famous for painting the 'Mona Lisa,' one of the most well-known artworks.",
        "category": "Art"
    },
    {
        "question": "What is 25 + 75?",
        "options": ["100", "150", "200", "50"],
        "correct_answer": "100",
        "explanation": "25 + 75 equals 100.",
        "category": "Math"
    },
    {
        "question": "Who was the first President of the United States?",
        "options": ["George Washington", "Abraham Lincoln", "Thomas Jefferson", "John Adams"],
        "correct_answer": "George Washington",
        "explanation": "George Washington was the first President of the United States and one of the Founding Fathers.",
        "category": "History"
    },
]

# Function to display question with graphics and feedback
def display_question(question_data, question_number, question_count, answers):
    st.subheader(f"Question {question_number + 1}: {question_data['question']}")
    options = question_data['options']
    
    # Remove the index parameter to avoid pre-selection
    answer = st.radio("Choose your answer:", options, key=question_number)
    
    # Show progress bar
    progress = (question_number + 1) / question_count
    st.progress(progress)

    # Only show feedback after an answer is selected
    if answer:
        if answer == question_data['correct_answer']:
            st.success("Correct!")
            answers[question_data['category']] += 1  # Increment category score
        else:
            st.error("Incorrect!")
        st.write(f"Explanation: {question_data['explanation']}")
        
    return answer == question_data['correct_answer']

# Function to show performance analytics with graphics
def show_performance(answers):
    st.write("### Performance Analytics")
    
    # Pie chart for performance across categories
    categories = list(answers.keys())
    correct_answers = list(answers.values())
    incorrect_answers = [len(questions) // len(categories) - correct for correct in correct_answers]
    
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(correct_answers, labels=categories, autopct='%1.1f%%', startangle=90, colors=['#66b3ff', '#ff6666'])
    ax.axis('equal')
    st.pyplot(fig)
    
    st.write("### Detailed Feedback")
    for category, score in answers.items():
        st.write(f"Category: {category} - Correct Answers: {score}")

# Function to run the quiz
def run_quiz():
    st.title("Interactive Quiz App with Real-Time Feedback")
    question_count = len(questions)
    answers = {category: 0 for category in set([q["category"] for q in questions])}  # Initialize category scores

    # Loop through the questions
    for question_number, question_data in enumerate(questions):
        correct = display_question(question_data, question_number, question_count, answers)
        st.write("---")

    # Show the final performance results
    st.subheader(f"Your final score:")
    total_score = sum(answers.values())
    st.write(f"Total Correct Answers: {total_score} out of {len(questions)}")

    # Show detailed performance analytics
    show_performance(answers)

# Run the quiz
if __name__ == "__main__":
    run_quiz()
