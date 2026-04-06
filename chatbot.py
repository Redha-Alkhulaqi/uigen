from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic

client = Anthropic()
model = "claude-sonnet-4-0"

def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

def chat(messages):
    message = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
    )
    return message.content[0].text

messages = []

print("Chatbot started! Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")

    if user_input.strip().lower() == "quit":
        print("Goodbye!")
        break

    add_user_message(messages, user_input)

    response = chat(messages)
    print(f"\nClaude: {response}\n")

    add_assistant_message(messages, response)
