from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Krishna's CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Krishna Agarwal"
PAGE_ICON = ":wave:"
NAME = "Krishna Agarwal"
DESCRIPTION = """
Data Analyst, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "iamkagarwal@email.com"
PHONE = "9219722728"
LinkedIn = "https://www.linkedin.com/in/iamkrishnaagarwal012/"

# SOCIAL_MEDIA = {
#     "LinkedIn": "https://www.linkedin.com/in/iamkrishnaagarwal012/",
#     # "GitHub": "https://github.com/iamkrishnaagarwal",
#     # "Kaggle": "https://kaggle.com",
# }
PROJECTS = {
    "🏆 Taxing Relaxing (GSTIN Filling & Billing Software) - A full fledge web app for taxing solutions": "https://youtu.be/AL9wQ18l1VQ",
    "🏆 ME Care (Make Your Own Skincare Kit Recommender) - Web app which recommend make your ownself pesonalized skincare products": "https://youtu.be/MKN6caDaTW8",
    "🏆 Drag Easy Trading (Tools for Stock Market Trading) - Design your own custom trading dashboard": "https://youtu.be/VR9fl8q828Q",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    
col1, col2, col3 = st.columns(3, gap="small")
with col1:
    st.write("📫", EMAIL)
with col2:
    st.write("📱", PHONE)
with col3:
    st.write("[LinkedIn](%s)" % LinkedIn)


 # --- SOCIAL LINKS ---
# st.write('\n')
# cols = st.columns(5, gap="small")
# for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
#     cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 1.5+ Years experience in extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python and Machine Learning
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
"""
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, OpenCV), C++, VBA
- 📊 Data Visulization: MS Excel, Plotly, Power Bi
- 📚 Modeling: Logistic regression, linear regression, decition trees, etc
- 🗄️ Databases: MongoDB, MySQL
- ☁️ Cloud: Firebase, Delta
- 🗃️ Data Collection: API Handling and Web Scrapping, Selinium, Quantitative Research 
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Data Analyst | Ayur2Veda**")
st.write("Feb 2023 - Present")
st.write(
    """
- ► Efficiently organize and analyze patient medical data using Python for insights & also ensuring data integrity and compliance while employing statistical methods.
- ► Tailor marketing efforts by identifying patterns in patient data.
- ► Optimizing quarterly plan features and pricing for increased subscribers.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Analyst | Carrers360**")
st.write("Nov 2021 - Dec 2021")
st.write(
    """
- ► Employ natural language processing techniques to analyze the chat interactions between students and company executives on the blog site.
- ► Utilize sentiment analysis tools to categorize and evaluate the sentiment expressed in the conversations.
- ► Identify areas of improvement and potential issues, providing actionable insights to enhance the overall user experience on the platform.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Data Analyst | Happygifting.co**")
st.write("March 2021 - July 2021")
st.write(
    """
- ► Thoroughly analyze data collected through Google Forms, categorizing information such as product requests, complaints, and other relevant data points.
- ► Creating a detailed report summarizing the key findings and trends identified during the analysis of Google Forms data.
- ► Provide the upper team with actionable recommendations based on the analysis, enabling informed decision-making.
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Education")
st.write("---")
st.write( "##### 🏫 **Maharishi Institute of Informational Technology, Noida**")
st.markdown(" &nbsp;&nbsp;&nbsp;&nbsp;<i> B.Tech in Data Science", unsafe_allow_html=True)
st.write("July 2019 - May 2023")


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
