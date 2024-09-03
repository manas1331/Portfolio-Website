import random
import time

import streamlit as st


# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Welcome to my portfolio! How can I assist you today?",
"Feel free to explore my projects and let me know if you have any questions.",
"Looking for specific information? Just ask!",
"I can help you navigate through my work and experiences.",
"Need details about a particular project? I'm here to help.",
"Check out my latest work and let me know if you need more information.",
"Curious about my skills? I can provide you with all the details.",
"Let's find the perfect project that matches your interests.",
"Have a question about my background or expertise? Just let me know.",
"I'm here to make your visit to my portfolio as smooth as possible.","I’d love to hear from you! Whether you have questions about my work, want to discuss potential collaborations, or just want to connect, feel free to reach out."
            "I’m excited to share some of the projects I’ve worked on.", "Each project represents a unique challenge and an opportunity for growth.","Hi there! How can I help you with my portfolio today?",
"Explore my work and let me know if you have any questions!",
"Need help finding something specific? Just ask!",
"I'm here to assist you with any information about my projects.",
"Want to know more about a particular piece of work? I can provide details.",
"Check out my achievements and let me know if you need further information.",
"Have a query about my skills or experience? I'm ready to help!",
"Looking for inspiration? Explore my projects and see what interests you.",
"If you need any help navigating my portfolio, feel free to ask!",
"Let me assist you in finding the right project that fits your needs."
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


st.title("Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})