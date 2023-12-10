import sys

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
