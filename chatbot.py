print("=" * 40)
print("🤖 Welcome to Rule-Based AI Chatbot")
print("Type 'bye' to exit.")
print("=" * 40)

while True:
    user = input("\nYou: ").lower()

    if user == "hello" or user == "hi":
        print("Bot: Hello! Nice to meet you.")

    elif user == "how are you":
        print("Bot: I'm doing great. Thanks for asking!")

    elif user == "what is your name":
        print("Bot: My name is DecodeBot.")

    elif user == "who created you":
        print("Bot: I was created by Srujan during the Decode Labs AI Internship.")

    elif user == "good morning":
        print("Bot: Good Morning! Have a wonderful day!")

    elif user == "good evening":
        print("Bot: Good Evening! Hope you had a great day!")

    elif user == "thank you":
        print("Bot: You're welcome!")

    elif user == "bye" or user == "exit" or user == "quit":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")