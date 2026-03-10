from fastapi import FastAPI
from pydantic import BaseModel

# Initialize the API
app = FastAPI(title="Clinical ETL Pipeline API")

# Define what the incoming data should look like
class ClinicalNote(BaseModel):
    patient_id: str
    raw_text: str

# Create a test route
@app.get("/")
def read_root():
    return {"Status": "API is running. Ready for ETL."}

# Create the route where the website will send the text
@app.post("/extract")
def extract_entities(note: ClinicalNote):
    # For now, we just echo it back. We will plug the AI in here later!
    return {
        "message": "Note received",
        "patient_id": note.patient_id,
        "text_length": len(note.raw_text)
    }