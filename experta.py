from experta import *

class Disease(Fact):
    """
    Allergies - sneezing, blocked nose, watery eyes, red eyes, coughing, red rash
    Asthma - wheezing, shortness of breath, a tight chest
    Head Tumor - severe headaches, seizures, mental changes, vision problem
    Chronic pain - diabetes, arthritis, back pain
    Dehydration - feeling thirsty, a dry mouth, tiredness, strong smelling urine
    Food Poisoning - nausea, vomiting, weakness, loss of appetite, aching muscles, chills
    """
    pass


class Patient(KnowledgeEngine):
    @Rule(Disease(symptoms=MATCH.symptoms))
    def diagnose_disease(self, symptoms):
        print("You may have the following diseases based on your symptoms:")
        if 'sneezing' in symptoms and 'blocked nose' in symptoms:
            print("Allergies")
        if 'wheezing' in symptoms and 'shortness of breath' in symptoms:
            print("Asthma")
        if 'severe headaches' in symptoms and 'seizures' in symptoms:
            print("Head Tumor")
        if 'diabetes' in symptoms and 'arthritis' in symptoms:
            print("Chronic Pain")
        if 'feeling thirsty' in symptoms and 'dry mouth' in symptoms:
            print("Dehydration")
        if 'nausea' in symptoms and 'vomiting' in symptoms:
            print("Food Poisoning")


engine = Patient()
engine.reset()

symptoms = []
num_symptoms = int(input("Enter the number of symptoms you are experiencing: "))
for _ in range(num_symptoms):
    symptom = input("Enter a symptom: ")
    symptoms.append(symptom)

engine.declare(Disease(symptoms=symptoms))
engine.run()
