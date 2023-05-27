import nltk
from nltk.chat.util import Chat,reflections

#Chat: The Chat class is provided by NLTK and is used to create a chatbot instance. 
    # It takes pairs of patterns and responses as input and provides methods for conversing with the user.

#reflections: The reflections module is a predefined dictionary in NLTK that contains a set of input reflections. 
# These reflections are used to transform the user's input into a more appropriate response. 
# For example, if the user says "I am happy," the reflection dictionary will replace "I" with "you" and "am" with "are" to generate a response like "You are happy."

pairs=[
    [
        r"my name is (.*)", 
        #The use of (.*?) allows the chatbot to extract and utilize specific information from the user's input, enhancing the conversational experience.
        ["Hello %1, how can i help you"]
    ],
    [
        r"hi|hey|hello",
        ["Hello","Hey there"]
    ],
    [
        r"what is your name?",
        ["I am chatbot created with NLTK."]
    ],
    [
        r"sorry(.*)",
        ["No problem","Don't worry"]
    ],
    [
        r"quit",
        #Raw string literals are often used when working with regular expressions, file paths, or any situation where the backslash character itself needs to be preserved without being interpreted as an escape character.
        ["Bye-bye. Take care!"]
    ]
]

# create a chatbot
def chatbot():
    print("Hi ! I am an AI chatbot.Chat with me.Type 'quit' to exit.")
    chat=Chat(pairs,reflections)
    chat.converse()
    #The chat.converse() method is used to start the conversation between the user and the chatbot. Once the chatbot is initialized using the Chat class and the pairs list, you can call the converse() method to begin the interaction.

#run the chatbot
if __name__ == "__main__":
    chatbot()
