import streamlit as st
from PIL import Image

st.title("Projects")

# Function to display project information in a box with a styled GitHub button
def display_project(title, description, image_path, github_link):
    with st.container():
        st.write(f"## {title}")
        cols = st.columns([2, 1])  # Two columns, with the first one taking twice the space
        with cols[0]:
            st.write(f"#### **Description:**\n{description}")
            # Styled "View on GitHub" button
            st.markdown(f"""
                <a href="{github_link}" target="_blank">
                    <button style="
                        background-color:#4CAF50; 
                        border:none; 
                        color:white; 
                        padding:10px 20px; 
                        text-align:center; 
                        text-decoration:none; 
                        display:inline-block; 
                        font-size:16px; 
                        margin:10px 2px; 
                        cursor:pointer; 
                        border-radius:8px;">
                        View on GitHub
                    </button>
                </a>
            """, unsafe_allow_html=True)
        with cols[1]:
            image = Image.open(image_path)  # Replace with the actual path to your image
            st.image(image, caption=f" {title}", use_column_width=True)
        st.write("---")

# Project 1
display_project(
    "Project 1: Stock-Price-Predictor-using-ML",
    """
   - This project involves developing an end-to-end web application to predict stock market prices using machine learning techniques in Python.
   - The application leverages historical stock data to forecast future prices, providing users with valuable insights into potential stock performance.
   - Tools & Technologies used: TensorFlow, Matplotlib, yfinance, Scikit-Learn, Pandas & NumPy, Streamlit
    """,
    "Pictures/stock_img.png",
    "https://github.com/manas1331/Stock-Price-Predictor-using-ML/tree/main"
)

# Project 2
display_project(
    "Project 2: Depression-Detector-Website",
    """
   - Created an interactive website for the weal 24hrs health hackathon with the help of HTML ,CSS, Javascript and used Flask for the backend.
   - This project uses large language models and fine tuning to create a chatbot which can speak with a user, determine whether or not they are depressed and suggests verbal countermeasures which helps the user.
   - Tools & Technologies used: HTML, CSS, JavaScript, Flask and LLM (llama model).
    """,
    "Pictures/login_img.png",
    "https://github.com/manas1331/Depression-Detector-Website/tree/main"
)

# Project 3
display_project(
    "Project 3: FTP-Server-with-SSL-Implementation",
    """
- This is a FTP server which has features like Authentication, Directory Listing, Uploading ,Downloading, Quitting out .
- We have also implemented SSL(Secure Socket Layer) so that the information sent is encrypted and safety of user's details is preserved.
 - Tools & Technologies used: Python ,OpenSSL
    """,
    "Pictures/FTP_img.png",
    "https://github.com/manas1331/FTP-Server-with-SSL-Implementation"
)

# Project 4
display_project(
    "Project 4: Car Price Predictor using ML",
    """
- This is a Car Price predictor using Machine Learning with an interactive UI built using streamlit(python framework).
- This site offers an interactive and user-friendly experience.
 - Tools & Technologies used: Python ,Streamlit
    """,
    "Pictures/portfolio.png",
    "https://github.com/manas1331/Car-Price-Predictor"
)


# Project 5
display_project(
    "Project 5: Portfolio-Website",
    """
- This is my portfolio website built using streamlit(python framework) with home, about & contact,resume,chatbot and projects sections.
- This site offers an interactive and user-friendly experience.
 - Tools & Technologies used: Python ,Streamlit
    """,
    "Pictures/portfolio.png",
    "https://github.com/manas1331/Portfolio-Website"
)

# Continue adding projects in the same format as above
