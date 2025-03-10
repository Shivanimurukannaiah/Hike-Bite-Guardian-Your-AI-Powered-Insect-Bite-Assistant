import streamlit as st
from openai import OpenAI

# Sidebar for API Key input
with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")

st.title("🦟 Hike Bite Guardian")
st.write("Identify insect bites and get first-aid guidance.")

# User input
prompt = st.text_input("Describe your symptoms and the insect bite.")

if prompt:
    if not openai_api_key:
        st.warning("Please enter your OpenAI API Key to continue.")
        st.stop()

    # Initialize OpenAI Client
    client = OpenAI(api_key=openai_api_key)

    # Define the system prompt for better results
    system_prompt = """You are a bot that helps identify insect bites. 
    When given a description of symptoms and insect appearance, return the following structured response:
    - Identified Bug: (Possible insect name)
    - Symptoms: (Expected symptoms of this bite)
    - Severity: (Mild, Moderate, Severe)
    - Bug Information: (Brief details about the insect)
    - First Aid: (Recommended first-aid treatment)
    """

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Symptoms and description: {prompt}"}
    ]

    # Call OpenAI API
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    # Extract the response
    bot_reply = response.choices[0].message.content

    # Display results
    st.write("### Results:")
    st.write(bot_reply)
