import sys

try:
    import streamlit as st
except ImportError:
    import sys, subprocess, importlib       
    subprocess.check_call([sys.executable, "-m", "pip", "install", "streamlit"])
    importlib.invalidate_caches()
    import streamlit as st
    #print("Streamlit is not installed. Please install it using 'pip install streamlit'.")
    #sys.exit(1)

st.title("Streamlite Example")
st.write("This is a simple Streamlit app that demonstrates the use of buttons and session state.")
st.title('_This_ is :blue[a title] : :speech_balloon: :sunglasses: :blue[with emojis]')
st.title('$E = mc^2$')
st.subheader("This is a subheader")

# TEXT  MESSAGES
st.text("This is a text element with no formatting")   
st.markdown("### List Follows: \n This is a markdown element with **bold** and *italic* formatting \n  just a plain line item \n")
st.write("This is a write element that can handle multiple types of content, including text, numbers, and even dataframes.")
data = {"Name": ["Alice", "Bob", "Charlie"], "Age": [25, 30, 35]}
st.write("Here is some sample data:")
st.write(data)
