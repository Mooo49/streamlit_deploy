import streamlit as st
from openai import OpenAI

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    "[![Open in GitHub Codespaces](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.title("The University Chatbot 🤖🧠 ")

if "messages" not in st.session_state:
    # Initialize the session with a system message to guide the assistant
    st.session_state["messages"] = [
        {"role": "system", "content": "You are a French helpful assistant for Moroccan university . You are fine-tuned on chat examples with students and you have the perfect answers. Your job is to answer student questions  in French. your responses must be in French language .le service de scolarité via https://www.education.gouv.fr/le-portail-scolarite-services-326158 . le portail pédagogique https://portail.edu-vd.ch/ . le service informatique via https://www.itaia.fr/les-services-informatiques-indispensable-a-toutes-les-entreprises/ . le site web du service d'aide à l'emploi des étudiants via https://www.1jeune1solution.gouv.fr/jobs-etudiants .la sécurité du campus via https://naspa.org/division/campus-safety-and-violence-prevention .le lien du portail étudiant https://etu.univ-lyon1.fr/ .le calendrier pédagogique https://unidauphine.eu/vie-etudiante/calendrier-pedagogique-2022-2023/ . time  allowed for  license thesis defense presentation is 45 min"},
        {"role": "assistant", "content": "Comment puis-je t'aider?"}
    ]

# Display only the user and assistant messages
for msg in st.session_state.messages:
    if msg["role"] != "system":
        st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    response = client.chat.completions.create(
        model="ft:gpt-3.5-turbo-0125:personal::9RVtR8QG",
        messages=st.session_state.messages
    )
    
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
