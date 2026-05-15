# Elementary Chatbot
## Artificial Intelligence Practical
## Aim

# Develop an elementary chatbot for customer interaction application.
# ## Theory

# A chatbot is a software application that interacts with users using text or voice.

# This chatbot is rule-based and responds to predefined user inputs using conditional statements.
# Simple Chatbot Program

print("Chatbot: Hello! I am your assistant.")
print("Type 'bye' to exit.")

while True:

    user = input("You: ").lower()

    if user == "hi" or user == "hello":
        print("Chatbot: Hello! How can I help you?")

    elif user == "how are you":
        print("Chatbot: I am fine. Thank you!")

    elif user == "your name":
        print("Chatbot: I am an AI Chatbot.")

    elif user == "courses":
        print("Chatbot: We offer AI, Data Science, and Python courses.")

    elif user == "fees":
        print("Chatbot: Please contact the administration office for fee details.")

    elif user == "bye":
        print("Chatbot: Goodbye!")
        break

    else:
        print("Chatbot: Sorry, I don't understand.")
## Conclusion

# The elementary chatbot was developed successfully.
# The chatbot responds to user queries using predefined rules and conditions.
