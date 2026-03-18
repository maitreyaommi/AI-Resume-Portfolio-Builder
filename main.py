import streamlit as st
import subprocess
import sys
import os

#Streamlit Page Setup
st.set_page_config(page_title="AI Resume, Portfolio & Cover Letter Builder", layout="wide")
st.title("🤖 AI Builder Main App")

st.markdown("""
### Welcome to the AI Builder Hub!
Select what you’d like to create today 👇
""")

# User Choice
choice = st.radio(
    "Select an option:",
    [
        "📄 AI Resume Builder",
        "🌐 AI Portfolio Builder",
        "🧾 AI Cover Letter Builder"
    ]
)

# Resume Builder
if choice == "📄 AI Resume Builder":
    st.success("You selected Resume Builder!")
    if st.button("🚀 Open Resume Builder"):
        script_path = os.path.join(os.getcwd(), "resume.py")
        subprocess.Popen([sys.executable, "-m", "streamlit", "run", script_path])
        st.info("Opening Resume Builder in a new window...")

# Portfolio Builder 
elif choice == "🌐 AI Portfolio Builder":
    st.success("You selected Portfolio Builder!")
    if st.button("🚀 Open Portfolio Builder"):
        script_path = os.path.join(os.getcwd(), "portfolio.py")
        subprocess.Popen([sys.executable, "-m", "streamlit", "run", script_path])
        st.info("Opening Portfolio Builder in a new window...")

# Cover Letter Builder
elif choice == "🧾 AI Cover Letter Builder":
    st.success("You selected Cover Letter Builder!")
    if st.button("🚀 Open Cover Letter Builder"):
        script_path = os.path.join(os.getcwd(), "cover_letter.py")
        subprocess.Popen([sys.executable, "-m", "streamlit", "run", script_path])
        st.info("Opening Cover Letter Builder in a new window...")
# Footer
st.markdown("---")
st.caption("🚀 Built with Streamlit | AI Resume, Portfolio & Cover Letter Builder")
