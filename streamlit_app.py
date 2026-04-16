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
    try:
        genai.configure(api_key=user_key)
        # Using the absolute standard model name to avoid 404/v1beta errors
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        course = st.selectbox("Select Course", ["CHM 101", "CHM 107", "CHM 211", "CHM 212"])
        title = st.text_input("Experiment Title")
        data = st.text_area("Paste your readings/observations here")
        
        if st.button("Generate Formal Report"):
            if not title or not data:
                st.error("Please provide both a title and data!")
            else:
                with st.spinner("Writing report..."):
                    prompt = f"Write a professional university lab report for {course}. Title: {title}. Data: {data}. Use a formal academic tone with Abstract, Introduction, Method, Results, and Conclusion."
                    response = model.generate_content(prompt)
                    st.markdown("---")
                    st.markdown("### Your Generated Report")
                    st.write(response.text)
    except Exception as e:
        st.error(f"Setup Error: {e}. Try checking your API key or refreshing the page.")
else:
    st.warning("👈 Please enter your Gemini API Key in the sidebar to begin.")

