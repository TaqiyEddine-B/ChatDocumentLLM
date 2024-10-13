""" This module contains utility functions for the chatbot. """
import json
import os
import sys

import streamlit as st


def load_openai_key()->str:
    """
    Load the OpenAI API key from the environment variable or user input.

    This function checks for the OpenAI API key in the following order:
    1. Streamlit secrets (secrets.toml file)
    2. User input via Streamlit sidebar

    Returns:
        tuple[str, bool]: A tuple containing:
            - str: The OpenAI API key
            - bool: A flag indicating whether a valid key was provided
    """
    key =""
    is_provided = False
    secrets_file = os.path.join(".streamlit", "secrets.toml")
    if  os.path.exists(secrets_file) and "OPENAI_API_KEY" in st.secrets.keys():
        key = st.secrets["OPENAI_API_KEY"]
        st.sidebar.success('Using OpenAI Key from sectrets.toml')
        is_provided = True
    else:
        key = st.sidebar.text_input('Add OpenAI API key and press \'Enter \'', type="password")
        if len(key) > 0:
            st.sidebar.success('Using the provided OpenAI Key')
            is_provided = True
        else:
            st.sidebar.error('No OpenAI Key')
    return key, is_provided


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
