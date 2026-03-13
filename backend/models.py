from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.sql import func
from database import Base

# Dimension: Patient
class DimPatient(Base):
    __tablename__ = "dim_patient"
    patient_key = Column(Integer, primary_key=True, index=True)
    patient_id = Column(String, unique=True)
    age_group = Column(String)
    gender = Column(String)

# Dimension: Condition
class DimCondition(Base):
    __tablename__ = "dim_condition"
    condition_key = Column(Integer, primary_key=True, index=True)
    condition_name = Column(String, unique=True)

# Dimension: Medication
class DimMedication(Base):
    __tablename__ = "dim_medication"
    medication_key = Column(Integer, primary_key=True, index=True)
    medication_name = Column(String, unique=True)

# Fact Table: The central event connecting everything
class FactExtraction(Base):
    __tablename__ = "fact_clinical_extraction"
    extraction_id = Column(Integer, primary_key=True, index=True)
    patient_key = Column(Integer, ForeignKey("dim_patient.patient_key"))
    condition_key = Column(Integer, ForeignKey("dim_condition.condition_key"))
    medication_key = Column(Integer, ForeignKey("dim_medication.medication_key"))
    raw_text = Column(Text)
    extraction_date = Column(DateTime, server_default=func.now())