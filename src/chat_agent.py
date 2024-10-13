import streamlit as st

class ChatAgent:
    def __init__(self, fun):
        self.fun = fun
        self.chat_history = []
    def send_message(self,messages):
        query = messages[-1]['content']
        result= self.fun(query)
        self.chat_history.append((query, result['answer']))

        return result['answer']

    def chat_bot(self):

        if "messages" not in st.session_state:
            st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

        for msg in st.session_state.messages:
            st.chat_message(msg["role"]).write(msg["content"])


        if prompt := st.chat_input():

            message = [{"role": "user", "content":str(prompt)}]
            st.session_state.messages.append(message[0])
            st.chat_message("user").write(prompt)

            response = self.send_message(st.session_state.messages)
            response_ = [{"role": "assistant", "content":str(response)}]

            st.session_state.messages.append(response_[0])
            st.chat_message("assistant").write(response)

    def external_question(self, question):
        message = [{"role": "user", "content":str(question)}]
        st.session_state.messages.append(message[0])

        st.chat_message("user").write(question)

        response = self.send_message(st.session_state.messages)
        response_ = [{"role": "assistant", "content":str(response)}]

        st.session_state.messages.append(response_[0])
        st.chat_message("assistant").write(response)
