import streamlit as st
from PIL import Image
import base64
from io import BytesIO



st.title("My Certificates")




images = [
    "Pictures/CIDECODE Certificate.png",
    "Pictures/Corporate Simulation.jpg",
    "Pictures/Data Science(Intrn Forte) Certificate.jpg","Pictures/GoldmanSachs_Certificate.png","Pictures/Python course certificate great learning.png","Pictures/Hacker_rank_problem_solving_basic certificate.png","Pictures/Hacker_Rank_problem_solving_intermediate certificate.png",
    "Pictures/Investment Banking Course Certificate.png","Pictures/Hacker_rank_python_basic certificate.png","Pictures/JP Morgan Cybersecurity course.png",
    "Pictures/Weal Hackathon Certificate.png","Pictures/Workshop Web Extension Certificate.png","Pictures/Workshop Chat GPT Certificate.png","Pictures/Stocks Course Certificate.png",
    "Pictures/GO certificate.png","Pictures/Rust certificate.png","Pictures/UX certificate.png","Pictures/manas1dering-C++ for problem solving - 1-1.png"
    ,"Pictures/manas1dering-Learn C1 - Pro-1.png","Pictures/manas1dering-Learn HTML _ CSS-1.png","Pictures/manas1dering-Learn Java-1.png","Pictures/manas1dering-Learn SQL-1.png",
    "Pictures/Python_course_certificate-1.png","Pictures/UX certificate.png","Pictures/Weal Hackathon Certificate-1"
]



images = [Image.open(img_path) for img_path in images]

if 'index' not in st.session_state:
    st.session_state.index = 0

# Function to convert image to base64 for embedding in HTML with border
def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Function to display the image with a border and navigation buttons
def display_image_with_navigation(image):
    image_base64 = image_to_base64(image)
    st.markdown(f"""
    <div style="position: relative; text-align: center; width: 100%; max-width: 800px; margin: auto; border: 15px solid #586e75; padding: 8px;">
        <img src="data:image/png;base64,{image_base64}" style="width: 100%; pointer-events: none;" oncontextmenu="return false;"/>
    </div>
    """, unsafe_allow_html=True)

# Inject JavaScript to disable right-click on the whole page (optional)
st.markdown("""
    <script>
    document.addEventListener('contextmenu', event => event.preventDefault());
    </script>
""", unsafe_allow_html=True)

# Display navigation buttons at the top
col1, col2, col3, col4 = st.columns([1, 5, 5, 1])

with col1:
    if st.button("◀", key="left"):
        if st.session_state.index > 0:
            st.session_state.index -= 1

with col2:
    st.write("")  # Empty space for alignment
    
with col3:
    st.write("")  # Empty space for alignment

# Display the image
display_image_with_navigation(images[st.session_state.index])

with col4:
    if st.button("▶", key="right"):
        if st.session_state.index < len(images) - 1:
            
            st.session_state.index += 1
