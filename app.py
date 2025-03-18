import streamlit as st
from openai import OpenAI
import utils
import sys
import os
sys.path.append(os.path.dirname(__file__))  # Ensures local module search

# Sidebar for API key
with st.sidebar:
    openai_api_key = st.text_input("Enter your OpenAI API Key", type="password")
    st.markdown("[Get an OpenAI API key](https://platform.openai.com/account/api-keys)")

st.title("🦟 Hike Bite Guardian")
st.write("Identify insect bites and get first-aid guidance.")

# Session state for storing messages
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Describe your symptoms and the insect bite."}]

# Display chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# User input handling
if prompt := st.chat_input("Describe your symptoms and the insect"):
    if not openai_api_key:
        st.warning("Please enter your OpenAI API key.")
        st.stop()

    # Append user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Identify bug and generate response
    bug_info = utils.identify_bug(prompt)
    if bug_info["Identified Bug"] != "Unknown":
        response = utils.generate_bug_response(bug_info)

        # Generate images for the insect and bite
        insect_image = utils.generate_image(f"{bug_info['Identified Bug']} insect", openai_api_key)
        bite_image = utils.generate_image(f"{bug_info['Identified Bug']} insect bite on human skin", openai_api_key)
    else:
        response = "I'm sorry, I couldn't identify the bug. Try providing more details."
        insect_image = None
        bite_image = None

    # Append assistant message
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)

    # Show images if available
    if insect_image:
        st.image(insect_image, caption=f"{bug_info['Identified Bug']} Insect")
    if bite_image:
        st.image(bite_image, caption=f"{bug_info['Identified Bug']} Bite Reaction")
