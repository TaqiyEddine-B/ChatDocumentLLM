""" This module contains utility functions for the chatbot. """
import sys
import os
import json
import streamlit as st

def chat_bot(fun):
    chat_history = []
    while True:
        query = input('Prompt: ')
        if query.lower() in ["exit", "quit", "q"]:
            print('Exiting')
            sys.exit()
        result = fun(query)
        print('Answer: ' + result['answer'] + '\n')
        chat_history.append((query, result['answer']))


def upload_file():
    """ Upload a file and return the path."""
    uploaded_file = st.sidebar.file_uploader("Choose a file")
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        string_data = bytes_data.decode("utf-8")
        file_path = os.path.join(os.getcwd(), 'my_file.txt')
        # Save the file in the current directory
        # with open(file_path, "w") as file:
        #     file.write(string_data)
        return file_path
    return None


def load_questions(chat_bot, file_name: str):
    """ Load questions from a json file and send the selected question to the chatbot."""

    question_file = os.path.join(os.getcwd(), 'data', 'data.json')
    # check if file exists
    if not os.path.exists(question_file):
        with open(question_file, encoding="utf-8") as json_file:
            questions = json.load(json_file)
        questions_list = ['']

        if file_name in questions.keys():
            questions_list.extend(questions[file_name])
        if len(questions_list) > 1:
            st.sidebar.write("## Questions of the selected file")
            question = st.sidebar.selectbox(
                'Select a question', questions_list)
            last_question = st.session_state.get('question', '')

            if len(question) > 1 and last_question != question:
                chat_bot.external_question(question)
                st.session_state['question'] = question

def load_markdown_file(markdown_file):
    with open(markdown_file, 'r') as file:
        content = file.read()
    return content
