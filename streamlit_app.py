import streamlit as st
import google.generativeai as genai
import os

st.set_page_config(page_title="UNIBEN Lab Report AI", page_icon="🧪")

# This is a 'Version Bump' - it forces Streamlit to refresh
# Current Version: 1.0.2

st.title("🧪 UNIBEN Lab Report AI")
st.write("Professional Chemistry Lab Reports for UNIBEN Students.")

with st.sidebar:
    st.header("Settings")
    user_key = st.text_input("Enter Gemini API Key", type="password")
    st.info("Get your key at aistudio.google.com")

if user_key:
    try:
        # FORCE THE STABLE API VERSION
        os.environ["GOOGLE_API_VERSION"] = "v1" 
        genai.configure(api_key=user_key, transport='rest')
        
        # Use the most basic model name
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        course = st.selectbox("Select Course", ["CHM 101", "CHM 107", "CHM 211"])
        title = st.text_input("Experiment Title")
        data = st.text_area("Paste your readings/observations here")
        
        if st.button("Generate Formal Report"):
            if not title or not data:
                st.error("Please provide both a title and data!")
            else:
                with st.spinner("Connecting to Google AI..."):
                    response = model.generate_content(f"Format this as a UNIBEN lab report: {title}. Data: {data}")
                    st.markdown("---")
                    st.markdown("### Your Generated Report")
                    st.write(response.text)
    except Exception as e:
        st.error(f"Connection Error: {e}")
else:
    st.warning("👈 Please enter your Gemini API Key in the sidebar.")

