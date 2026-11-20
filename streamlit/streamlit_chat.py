import sys

try:
    import streamlit as st
except ImportError:
    import sys, subprocess, importlib       
    subprocess.check_call([sys.executable, "-m", "pip", "install", "streamlit"])
    importlib.invalidate_caches()
    import streamlit as st
    
st.title("Streamlite Example")
st.write("This is a simple Streamlit app that demonstrates the use of a chat interface.")

with st.chat_message("user"):
    st.markdown("Hello, I am a user. How are you?")

prompt = st.chat_input("Enter message...")
if prompt:
    with st.chat_message("user"):
        st.write(f"User message: {prompt}")

    with st.chat_message("assistant"):
        st.markdown("Hello, I am an assistant. I am doing well, thank you!")