-- Dimension Tables
CREATE TABLE Dim_Patient (
    Patient_Key SERIAL PRIMARY KEY,
    Patient_ID VARCHAR(50),
    Age_Group VARCHAR(20),
    Gender VARCHAR(10)
);

CREATE TABLE Dim_Condition (
    Condition_Key SERIAL PRIMARY KEY,
    Condition_Name VARCHAR(255) UNIQUE
);

CREATE TABLE Dim_Medication (
    Medication_Key SERIAL PRIMARY KEY,
    Medication_Name VARCHAR(255) UNIQUE
);

-- Fact Table
CREATE TABLE Fact_Clinical_Extraction (
    Extraction_ID SERIAL PRIMARY KEY,
    Patient_Key INT REFERENCES Dim_Patient(Patient_Key),
    Condition_Key INT REFERENCES Dim_Condition(Condition_Key),
    Medication_Key INT REFERENCES Dim_Medication(Medication_Key),
    Raw_Text TEXT,
    Extraction_Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);