import streamlit as st
import google.generativeai as genai

# Page setup
st.set_page_config(page_title="UNIBEN Lab Report AI", page_icon="🧪")

st.title("🧪 UNIBEN Lab Report AI")
st.write("Professional Chemistry Lab Reports for UNIBEN Students.")

# Sidebar for API Key
with st.sidebar:
    st.header("Settings")
    user_key = st.text_input("Enter Gemini API Key", type="password")
    st.info("Get your key at aistudio.google.com")

if user_key:
    try:
        # NEW CONFIGURE API: Using 'rest' transport to bypass network blocks
        genai.configure(api_key=user_key, transport='rest')
        
        # Standard model name
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # UI Elements
        course = st.selectbox("Select Course", ["CHM 101", "CHM 107", "CHM 211", "CHM 212"])
        title = st.text_input("Experiment Title")
        data = st.text_area("Paste your readings/observations here")
        
        if st.button("Generate Formal Report"):
            if not title or not data:
                st.error("Please provide both a title and data!")
            else:
                with st.spinner("Writing your professional report..."):
                    prompt = (
                        f"Write a professional university lab report for {course}. "
                        f"Title: {title}. Data: {data}. "
                        f"Use a formal academic tone with Abstract, Introduction, "
                        f"Method, Results, and Conclusion."
                    )
                    response = model.generate_content(prompt)
                    st.markdown("---")
                    st.markdown("### Your Generated Report")
                    st.write(response.text)
                    
    except Exception as e:
        st.error(f"Something went wrong: {e}")
        st.info("Check if your API Key is correct and try again.")
else:
    st.warning("👈 Please enter your Gemini API Key in the sidebar to begin.")

