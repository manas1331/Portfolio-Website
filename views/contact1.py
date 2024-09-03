import streamlit as st
# import re
# import requests
# from forms.contact import contact_form

st.title("Contact ")


st.write(
    """ ### **I will be happy to hear from you! Whether you have a project in mind, a question, or just want to say hello, feel free to reach out.** 
    ### **Your thoughts and inquiries are always welcome, and I'll do my best to respond promptly. Let's connect and create something amazing together !** """  )



st.markdown("""
<style>
a {
    text-decoration: none;
    # color: black;
    font-size: 15px;
    margin-right: 30px;
}
</style>


<a href="mailto:manas.contact17@gmail.com" target="_blank" style="font-size:60px;"><i class="fas fa-envelope"></i></a>
<a href="https://github.com/manas1331" target="_blank" style="font-size:60px;"><i class="fab fa-github"></i></a>
<a href="https://www.linkedin.com/in/manas1331" target="_blank" style="font-size:60px;"><i class="fab fa-linkedin"></i></a>

""", unsafe_allow_html=True)

st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
""", unsafe_allow_html=True)