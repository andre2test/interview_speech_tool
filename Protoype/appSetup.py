# Importing necessary libraries

from unicodedata import name

from openai import OpenAI
import streamlit as st

# Setting up the Streamlit page configuration
debug = False
st.set_page_config(page_title="Streamlit Chat", page_icon="💬")

# Initialize session state variable to track setup completion
if "setup_complete" not in st.session_state:
    st.session_state.setup_complete = False
    
if "user_message_count" not in st.session_state:
    st.session_state.user_message_count = 0
    
if "feedback_shown" not in st.session_state:
    st.session_state.feedback_shown = False 

if "messages" not in st.session_state:
    st.session_state.messages = []
    
if "chat_complete" not in st.session_state:
    st.session_state.chat_complete = False

    
# Helper functions to update states
def complete_setup():
    st.session_state.setup_complete = True
    
def show_feedback():
    st.session_state.feedback_given = True

#Setup stage for collecting user details
if not st.session_state.setup_complete:

    st.subheader('Personal information', divider='rainbow')

    if "name" not in st.session_state:
        st.session_state["name"] = ""
    if "experience" not in st.session_state:
        st.session_state["experience"] = ""
    if "skills" not in st.session_state:
        st.session_state["skills"] = ""
        
    st.session_state["name"] = st.text_input(label = "Name", max_chars = 40, value = st.session_state["name"], placeholder="Enter your name")
    st.session_state["experience"] = st.text_area(label = "Experience", value = st.session_state["experience"], max_chars = 200, placeholder="Describe your experience")
    st.session_state["skills"] = st.text_area(label = "Skills", value = st.session_state["skills"], max_chars = 200, placeholder="List your skills")

    # Enter Position and Company Info
    st.subheader('Company and Position', divider='rainbow')
    col1, col2 = st.columns(2)
    with col1:
        st.session_state["level"] = st.radio("Choose Level", key="visibility", options=["Entry-level", "Mid-level", "Senior-level"])
    with col2:
        st.session_state["position"] = st.selectbox("Choose a Position", ["Data Engineer", "Software Engineer", "Product Manager", "Data Scientist"])

    st.session_state["company"] = st.selectbox("Choose a Company", ["Google", "Microsoft", "Amazon", "Facebook", "Apple", "Meta"])

    # Echo back the user's input
    if debug:
        st.write(f"**Name**: {st.session_state['name']}")
        st.write(f"**Your Experience**: {st.session_state['experience']}")
        st.write(f"**Your Skills**: {st.session_state['skills']}")
        st.write(f"**Level**: {st.session_state['level']}")
        # Test labels for company and position information
        st.write(f"**Your information**: {st.session_state['level']} {st.session_state['position']} at {st.session_state['company']}")

# A button to complete the setup stage and start the interview
if st.button("Start Interview", on_click=complete_setup):
    st.write("Setup complete. Starting interview...")

# Interview stage
if st.session_state.setup_complete and not st.session_state.feedback_shown and not st.session_state.chat_complete:
    # Display a welcome message and prompt the user to introduce themselves
    st.info(
        """
        Start by introducing yourself.
        """,
        icon = "👋"
    )

    # Initializing the OpenAI client using the API key from Streamlit's secrets
    openai_api_key = st.secrets["OPENAI_API_KEY"]
    if not openai_api_key:
        print("OpenAI API Key not set - please head to the troubleshooting guide in the setup folder")

    client = OpenAI(api_key=openai_api_key)

    # Setting up the OpenAI model in session state if it is not already defined
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-4o"

    # Initializing the 'messages' list 
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "system", 
             "content":(f"You are an HR executive interviewing {st.session_state['name']} "
                        f"with experience in {st.session_state['experience']} "
                        f"and skills in {st.session_state['skills']}. "
                        f"The candidate is applying for a {st.session_state['level']}" 
                        f"{st.session_state['position']} position" 
                        f"at {st.session_state['company']}. "
                        f"Please conduct the interview accordingly")
             }]

    # Looping through the 'messages' list to display each message except system messages
    for message in st.session_state.messages:
        if message["role"] != "system":
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        
    # Input field for the user to send a new message
    if prompt := st.chat_input("Your answer.", max_chars = 400):
        # Appending the user's input to the 'messages' list in session state
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display the user's message in a chat bubble
        with st.chat_message("user"):
            st.markdown(prompt)
    
        # Assistant's response
        with st.chat_message("assistant"):
            stream = client.chat.completions.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True, # This line enables streaming for real-time response
            )
            # Display the assistant's response as it streams
            response = st.write_stream(stream)
        # Append the assistant's full response to the 'messages' list
        st.session_state.messages.append({"role": "assistant", "content": response})