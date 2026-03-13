import spacy

# 1. Load the stable English NLP model we successfully downloaded
print("Loading NLP Model...")
nlp = spacy.load("en_core_web_sm")

# 2. Add an Entity Ruler to "teach" the AI medical terms
# (We put it *before* the standard NER so our medical rules take priority)
ruler = nlp.add_pipe("entity_ruler", before="ner")

# 3. Define our custom clinical dictionary (You can add to this later!)
patterns = [
    {"label": "CONDITION", "pattern": [{"LOWER": "hypertension"}]},
    {"label": "CONDITION", "pattern": [{"LOWER": "diabetes"}]},
    {"label": "CONDITION", "pattern": [{"LOWER": "pneumonia"}]},
    {"label": "CONDITION", "pattern": [{"LOWER": "chest"}, {"LOWER": "pain"}]},
    {"label": "MEDICATION", "pattern": [{"LOWER": "aspirin"}]},
    {"label": "MEDICATION", "pattern": [{"LOWER": "metoprolol"}]},
    {"label": "MEDICATION", "pattern": [{"LOWER": "amoxicillin"}]},
    {"label": "MEDICATION", "pattern": [{"LOWER": "lisinopril"}]}
]
ruler.add_patterns(patterns)

def extract_clinical_data(raw_text: str):
    """
    Takes a raw doctor's note and extracts structured conditions and medications.
    """
    # Feed the text to the AI
    doc = nlp(raw_text)
    
    # Create an empty dictionary to store our findings
    extracted_data = {
        "Conditions": [],
        "Medications": []
    }
    
    # Loop through all the entities the AI found
    for ent in doc.ents:
        # If it's a condition and not already in our list, add it
        if ent.label_ == "CONDITION" and ent.text.title() not in extracted_data["Conditions"]:
            extracted_data["Conditions"].append(ent.text.title())
            
        # If it's a medication and not already in our list, add it
        elif ent.label_ == "MEDICATION" and ent.text.title() not in extracted_data["Medications"]:
            extracted_data["Medications"].append(ent.text.title())
            
    return extracted_data

# --- Quick Test Block ---
# This only runs if you execute this specific file directly
if __name__ == "__main__":
    sample_note = "Patient is a 45-year-old male presenting with severe chest pain and a history of hypertension. Prescribed 100mg of Metoprolol and daily Aspirin."
    
    print("\n--- Raw Doctor's Note ---")
    print(sample_note)
    
    print("\n--- AI Extraction Results ---")
    results = extract_clinical_data(sample_note)
    print(results)
    print("\n")