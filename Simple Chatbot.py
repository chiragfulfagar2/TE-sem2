import random

responses={   #The responses dictionary contains different categories of user input and 
                #corresponding lists of responses.

    "hello" : ["Hello! How are u ?",
               
               "Hi there! I hope you are having a good day.",
               
               "Hey! Its me your virtual friend."],
    
    "how_are_you":["I'm doing well, thankyou for asking.",
                   
                   "I'm feeling great today!",
                   
                   "I'm doing alright."],
    
    "goodbye" : ["Goodbye!",
                 
                 "See you later!",
                 
                 "Take care."],

    "anxiety":["It's important to take care of your mental health.Pls start practicing self-care."],

    "depression":["Remember that it's okay to not be okay.Share your feelings with someone."],

    "mental_health":["There is no shame in seeking help for your mental health.Do consider a therapy"],

    "default":["I'm sorry, I don't understand.Could you say that again ?",
               
               "I'm not sure what you mean."],
    
    "thank_you" :["Have a great day !"]

}

#The generate_responses function takes the user's input as an argument and generates a response based on the input. 
#It uses conditional statements to match the input with the predefined categories and 
#selects a random response from the corresponding list.

def generate_responses(input_text):

    input_text = input_text.lower() 
    #The line input_text = input_text.lower() is used to convert the user's input to lowercase. 
    # It ensures that the chatbot can recognize user input regardless of whether it is in uppercase or lowercase.

    if "hello" in input_text:

        return random.choice(responses["hello"])
    
    elif "how are you" in input_text:

        return random.choice(responses["how_are_you"])
    
    elif "goodbye" in input_text:

        return random.choice(responses["goodbye"])
    
    elif "anxiety" in input_text:

        return random.choice(responses["anxiety"])
    elif "depression" in input_text:

        return random.choice(responses["depression"])
    elif "mental health" in input_text:

        return random.choice(responses["mental_health"])
    elif "thank you" in input_text:

        return random.choice(responses["thank_you"])
    
    else:

        return random.choice(responses["default"])
    
#main function to handel the conversation

def main():

    print("Welcome to Mental Health Matters Bot. What can I do for u today?")

    while True:

        user_input = input("You: ")

        if user_input.lower() == "quit":
            
            #The main function is the entry point of the program. 
            # It initializes the conversation and continuously prompts the user for input until the user enters "quit". 
            # It calls the generate_responses function to generate a response based on the user's input and prints the response.

            print(random.choice(responses ["goodbye"]))

            break

        response = generate_responses(user_input)

        print("MENTALHEALTHMATTERS: "+  response)

if __name__=="__main__" : 

    #The main function also handles the "quit" command, which terminates the conversation and prints a random goodbye message.

    main()
