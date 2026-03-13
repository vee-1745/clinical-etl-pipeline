import streamlit as st
import requests

# 1. Page Configuration
st.set_page_config(page_title="Clinical ETL Dashboard", page_icon="🏥", layout="wide")

# 2. Header Section
st.title("🏥 Clinical NLP & ETL Pipeline")
st.markdown("""
Welcome to the Clinical Data Engine. Type a raw doctor's note below. 
Our spaCy NLP model will extract the entities and our FastAPI backend will load them into the PostgreSQL Data Warehouse.
""")
st.divider()

# 3. Input Section
col1, col2 = st.columns([1, 3])
with col1:
    patient_id = st.text_input("Patient ID", value="PT-1002")
with col2:
    raw_text = st.text_area("Doctor's Note (Raw Text)", height=150, value="Patient presents with severe chest pain and pneumonia. I am prescribing them Aspirin and Amoxicillin.")

# 4. Action Button
if st.button("🚀 Run Extraction Pipeline", type="primary"):
    if raw_text.strip() == "":
        st.warning("Please enter a doctor's note first.")
    else:
        with st.spinner("Processing through NLP Pipeline & Saving to Data Warehouse..."):
            
            # 5. Send the data to your FastAPI Backend
            api_url = "http://127.0.0.1:8000/extract"
            payload = {"patient_id": patient_id, "raw_text": raw_text}
            
            try:
                response = requests.post(api_url, json=payload)
                
                if response.status_code == 200:
                    result = response.json()
                    st.success(f"✅ {result['message']}")
                    
                    # 6. Display the Results Beautifully
                    st.subheader("🧠 AI Extraction Results")
                    res_col1, res_col2 = st.columns(2)
                    
                    with res_col1:
                        st.info("🦠 Extracted Conditions")
                        conditions = result["extracted_data"].get("Conditions", [])
                        if conditions:
                            for c in conditions:
                                st.write(f"- **{c}**")
                        else:
                            st.write("None found.")
                            
                    with res_col2:
                        st.warning("💊 Extracted Medications")
                        meds = result["extracted_data"].get("Medications", [])
                        if meds:
                            for m in meds:
                                st.write(f"- **{m}**")
                        else:
                            st.write("None found.")
                else:
                    st.error(f"API Error: {response.text}")
                    
            except requests.exceptions.ConnectionError:
                st.error("🚨 Could not connect to the Backend API. Is your FastAPI server running on port 8000?")