import random

# Dictionary with possible things the user can say as the keys, and the strings
# the bot could respond with as values
# Make sure keys are all lowercase
responses = {"hello": ["Hi, how are you", "Hello!", "Greetings", "Hi"],
             "hi": ["Hi, how are you", "Hello!", "Greetings", "Hi"],
             "good": ["Good to hear!", "Nice!"],
             "how are you": ["Doing alright, I'm responding to you!", "Idk, I'm just a bot", "Code worky well"]}

# If the user types these, then the bot will turn off
quiting = ["goodbye", "bye", "quit"]

# This can be whatever, its just what the bot initially says to get started
question = "Give input"

# This holds user input and inputs the question
userInput = input(question + "\n").lower()

# This will look for user input until they type one of the words in quitting
while userInput not in quiting:

    # Generates a random response from the dictionary, responses
    if userInput in responses:
        print(random.choice(responses.get(userInput)))

    userInput = input().lower()

print("Okay, shutting down")