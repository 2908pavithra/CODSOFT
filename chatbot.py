# Simple Rule-Based Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for case insensitivity

    # Predefined rules
    if 'hello' in user_input or 'hi' in user_input:
        return "Hello! How can I help you today?"
    elif 'how are you' in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "good" in user_input or "fine" in user_input:
        return "Sounds good."
    elif 'your name' in user_input:
        return "I'm ChatBot, your virtual assistant."
    elif 'bye' in user_input or 'goodbye' in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

# Chatbot interaction
def chat():
    print("ChatBot: Hi there! I'm ChatBot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("ChatBot:", response)
        if 'bye' in user_input.lower():
            break

# Start the chat
if __name__ == "__main__":
    chat()
