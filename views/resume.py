import streamlit as st
# from forms.contact import contact_form

st.title("More About Myself")

# Uncomment this function if you want a dialog-based contact form
# @st.dialog("Contact Me")
# def show_contact_form():
#     contact_form()

# --- HERO SECTION ---
col1, col2 = st.columns([1, 3], gap="small")
with col1:
    st.image("Pictures/Profile_pic.png", width=180)

with col2:
    st.title("Manas R", anchor=False)
    st.write(
        "|| CSE Pre-Final year Student at PES University | Research Intern at ISFCR(Cybersecurity) | Member at Research Et Al | Samarpana | CMS | Weal | Core member at QQC | Kannada Koota ||"
    )
    # Uncomment the following code to add a Contact Me button
    # if st.button("✉️ Contact Me"):
    #     show_contact_form()

# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.markdown(
    """
    <h3 style="text-decoration: underline;">Experience & Qualifications</h3>
    """,
    unsafe_allow_html=True
)
st.write(
    """
    - **Research Intern at ISFCR** , Bengaluru *[Jun 2024 - Jul 2024]*
    - Strong hands-on experience and knowledge in Python and Excel
    - Researched on Forensics of AI Attack on autonomous vehicles and wrote a survey paper on this.
    - Currently working on countermeasures related to AI attacks on Autonomous vehicles.
    """
)

# --- SKILLS ---
st.write("\n")
st.markdown(
    """
    <h3 style="text-decoration: underline;">Technical Skills</h3>
    """,
    unsafe_allow_html=True
)
st.write(
    """
    - **Developer Tools:** GitHub, Visual Studio
    - **Programming:** Python, C++, C, Java, Go, R
    - **Data Visualization:** MS Excel, R
    - **Databases:** MongoDB, MySQL
    """
)

# --- POSITIONS OF RESPONSIBILITY ---
st.write("\n")
st.markdown(
    """
    <h3 style="text-decoration: underline;">Positions of Responsibility</h3>
    """,
    unsafe_allow_html=True
)
st.write(
    """
    - Design Team (Core), QQC club (National level Conquiztador Quiz)
    - Design Team, Research Et AL club (Inquisto, Articulate, Erudio podcast)
    - Design Team (Core), Kannada Koota club (Kannada Rajyotsva-2023)
    - Logistics Team, Samarpana club (Samarpana Run-2023)
    - Operations Team, CMS Club (Green Carnival)
    - Web Development Member at Weal (Health Tech Club)
    """
)

# --- RESUME LINK ---
with st.expander("##### **Resume Link**"):
    st.write("Click the link below to view my resume:")
    st.markdown(
        '<a href="https://drive.google.com/file/d/1g6QPJrjUPHyAQx9TojSrXPP-0FT_geHA/view?usp=drive_link" target="_blank">**View Resume**</a>',
        unsafe_allow_html=True
    )
