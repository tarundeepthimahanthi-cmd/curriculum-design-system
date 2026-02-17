import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv

# ----------------------------
# Load Environment Variables
# ----------------------------
load_dotenv()

# Correct way to fetch API key
api_key = os.getenv("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")

# Validate API key
if not api_key:
    st.error("❌ GROQ API key not found. Please add it to .env file")
    st.stop()

# Initialize Groq client
client = Groq(api_key=api_key)

# ----------------------------
# Streamlit Page Config
# ----------------------------
st.set_page_config(
    page_title="CurricuForge",
    page_icon="🎓",
    layout="wide"
)

# ----------------------------
# Header Section
# ----------------------------
st.title("🎓 CurricuForge")
st.subheader("Generative AI – Powered Curriculum Design System")

st.write("""
This system generates structured academic curriculum including:
- Course Structure
- Topic Recommendations
- Learning Outcomes
- Curriculum Optimization
""")

# ----------------------------
# Sidebar Inputs
# ----------------------------
st.sidebar.header("📋 Course Requirements")

domain = st.sidebar.text_input("Course Domain", "Artificial Intelligence")
level = st.sidebar.selectbox("Difficulty Level", ["Beginner", "Intermediate", "Advanced"])
duration = st.sidebar.text_input("Course Duration", "12 Weeks")
audience = st.sidebar.text_input("Target Audience", "Undergraduate Students")
focus = st.sidebar.text_area("Special Focus (Optional)", "Industry oriented skills")

generate_btn = st.sidebar.button("🚀 Generate Curriculum")

# ----------------------------
# Groq LLM Function
# ----------------------------
def generate_curriculum():

    prompt = f"""
    Design a complete academic curriculum based on the following:

    Domain: {domain}
    Level: {level}
    Duration: {duration}
    Target Audience: {audience}
    Special Focus: {focus}

    Generate:

    1. Course Overview
    2. Structured Module Breakdown
    3. Weekly Topic Plan
    4. Learning Outcomes Mapping
    5. Suggested Tools & Technologies
    6. Industry Alignment Explanation
    7. Assessment Strategy
    """

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": "You are an expert academic curriculum designer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content

# ----------------------------
# Output Section
# ----------------------------
if generate_btn:
    with st.spinner("Generating Curriculum..."):
        result = generate_curriculum()

    st.success("✅ Curriculum Generated Successfully")
    st.markdown("### 📚 Generated Curriculum")
    st.write(result)

# ----------------------------
# Footer
# ----------------------------
st.markdown("---")
st.caption("CurricuForge | Generative AI Curriculum Design System")
