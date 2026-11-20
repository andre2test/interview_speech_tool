# To Run
.\.venv311\Scripts\streamlit.exe run .\Protoype\app.py



### Setup secrets.toml
Set-Location 'D:\Development\Udemy_AI\AI_ENGR\IntroSpeechRecog'
.\.venv311\Scripts\streamlit.exe run .\Protoype\app.py

### Install OPEN AI
.\.venv311\Scripts\python.exe -m pip install openai

#### Verify setup
.\.venv311\Scripts\python.exe -c "from openai import OpenAI; print('OpenAI SDK installed successfully')"

SET UP --> Setup Complete

user_message_count   \
                      \ INTERVIEW \
                      /            \ messages
chat_complete        /             /
                                  /
feedback_show --------> FEEDBACK /


# Sourcce Control
Creaated get environment with command:
Added .gitignore with commnad at project root:  New-Item -Path .gitignore -ItemType File