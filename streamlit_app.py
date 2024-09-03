import streamlit as st


# --- PAGE SETUP ---
home_page = st.Page(
    "views/home.py",
    title="Home",
    icon="🏠",
    default=True,
)

about_page = st.Page(
    "views/about_me.py",
    title="About and Contact",
    icon="👨🏻‍🦱",
    # default=True,
)


resume_page = st.Page(
    "views/resume.py",
    title="Resume",
    icon="📄",
)

project_2_page = st.Page(
    "views/chatbot.py",
    title="Chat Bot",
    icon="🤖",
)

certificate_page = st.Page(
    "views/certificate.py",
    title="Certificates",
    icon="🪪",
)
project_page=st.Page(
    "views/project.py",
    title="Projects",
    icon="💼",
)


# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Basic Info": [home_page,about_page,resume_page],
        "Projects and Certificates": [project_page, project_2_page,certificate_page],
    }
)


# --- SHARED ON ALL PAGES ---
st.logo("Pictures/Logo.png")
# icon_image="©️",
# )



# --- RUN NAVIGATION ---
pg.run()

st.markdown("""
<div style='text-align: center; font-size: 20px; margin-top: 50px;'>
    © Copyright 2024 . All rights reserved.
</div>
""", unsafe_allow_html=True)
