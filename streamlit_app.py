import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="UNIBEN Lab Report AI", page_icon="🧪")

st.title("🧪 UNIBEN Lab Report AI")
st.write("Professional Chemistry Lab Reports for UNIBEN Students.")

with st.sidebar:
    st.header("Settings")
    user_key = st.text_input("Enter Gemini API Key", type="password")
    st.info("Get your key at aistudio.google.com")

if user_key:
    genai.configure(api_key=user_key)
    model = genai.GenerativeModel('gemini-1.5-flash-latest') 
    
    course = st.selectbox("Select Course", ["CHM 101", "CHM 107", "CHM 211", "CHM 212"])
    title = st.text_input("Experiment Title")
    data = st.text_area("Paste your readings/observations here")
    
    if st.button("Generate Formal Report"):
        if not title or not data:
            st.error("Please provide both a title and data!")
        else:
            with st.spinner("Writing report..."):
                prompt = f"Write a professional university lab report for {course}. Title: {title}. Data: {data}. Use a formal tone with Abstract, Introduction, Method, Results, and Conclusion."
                response = model.generate_content(prompt)
                st.markdown("---")
                st.markdown(response.text)
else:
    st.warning("👈 Please enter your Gemini API Key in the sidebar to begin.")
