import requests
import random
api_url = "http://127.0.0.1:5000"  # Replace with your API URL
api_url = api_url + "/conversation"

# Function to start a conversation
def start_conversation():
    conversation = [{"role":"system", "content": "YOUR_CHATBOT_ROLE."}]
    initial_message = "SOME_INITIAL_MESSAGE_WHATEVER_YOU_WANT"
    first_message = True
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        if first_message:
            user_input = initial_message + user_input
            first_message = False
        conversation.append({"role": "user", "content": user_input})
        response = send_message(conversation)
        print(f"Assistant: {response}")

# Function to send a message to the API
def send_message(messages):
    data = {"messages": messages}
    response = requests.post(api_url, json=data)

    if response.status_code == 200:
        return response.json()["response"]
    else:
        print(response)
        return f"Error: {response.status_code} - {response.json()}"

if __name__ == "__main__":
    print("Welcome to the conversation! Type 'exit' to end the conversation.")
    start_conversation()