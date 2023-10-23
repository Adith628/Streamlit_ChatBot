import openai

def get_initial_message():
    messages = [
        {"role":"system","content":"You are helpful AI buddy. Who cares about him and give helpful tips"},
        {"role":"user","content":"Talk to me friendly"},
        {"role":"system","content":"I will help you to get out of your problems"},
    ]
    return messages

def get_chatgpt_response(messages):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages,
    )
    return response['choices'][0]['message']['content']

def update_chat(messages,role,content):
    messages.append({"role":role,"content":content})
    return messages