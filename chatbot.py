# chatbot.py

print("=" * 50)
print("🤖 Welcome to the Rule-Based AI Chatbot")
print("Type 'bye', 'exit', or 'quit' to end the chat.")
print("=" * 50)

responses = {
    # Greetings
    "hello": "Hello! How can I help you today?",
    "hi": "Hi! Nice to meet you.",
    "hey": "Hey! What's up?",

    # Bot Information
    "who are you": "I am a Rule-Based AI Chatbot created using Python.",
    "what is your name": "My name is DecodeBot.",

    # Personal Information
    "who made you": "I was created by P. Laxmi Kanth Reddy.",
    "college": "I study at ICFAI Foundation for Higher Education.",
    "course": "I am pursuing B.Tech in Computer Science Engineering.",

    # Help
    "help": "You can ask me greetings, my name, who made me, college, course, or say bye to exit.",

    # Polite Responses
    "thanks": "You're welcome!",
    "thank you": "Happy to help!",
    "good morning": "Good Morning! Have a wonderful day!",
    "good evening": "Good Evening!",
    "good night": "Good Night! Take care."
}

while True:
    user_input = input("\nYou: ").lower().strip()

    # Exit Commands
    if user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a great day. 👋")
        break

    # Dictionary Lookup
    response = responses.get(
        user_input,
        "Sorry, I don't understand that. Type 'help' to know what you can ask."
    )

    print("Bot:", response)
