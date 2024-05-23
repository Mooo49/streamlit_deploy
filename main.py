import streamlit as st
from openai import OpenAI

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
#    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
#    "[![Open in GitHub Codespaces](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.title("The University Chatbot 🤖🧠 ")

if "messages" not in st.session_state:
    # Initialize the session with a system message to guide the assistant
    st.session_state["messages"] = [
        {"role": "system", "content": "You are a French helpful assistant for Moroccan university . Your job is to help the students in French. languages  offered as learning options in the university are English and French .Average class sizes for upper division courses hover around 200 students. registration for first years starts on September 1st and the expected date for the start of the university can be found on the university website.these are the websites that you must to send to the user based on his demand: le service de scolarité and the university website via https://www.education.gouv.fr/le-portail-scolarite-services-326158 , le portail pédagogique https://portail.edu-vd.ch/ , le service informatique via https://www.itaia.fr/les-services-informatiques-indispensable-a-toutes-les-entreprises/  ,  le site web du service d'aide à l'emploi des étudiants via https://www.1jeune1solution.gouv.fr/jobs-etudiants  , la sécurité du campus via https://naspa.org/division/campus-safety-and-violence-prevention  , le lien du portail étudiant https://etu.univ-lyon1.fr/ , The dates of the catch-up sessions will be available on the educational calendar https://unidauphine.eu/vie-etudiante/calendrier-pedagogique-2022-2023/ .time  allowed for  license thesis defense presentation is 45 min.The documents are needed to finalize  registration once the application has been approved and the deadlines for new doctoral students to register can be found on the university website.To obtain an official evaluation of  transferable credits, the student must submit official transcripts from all universities attended to the hosted university . University working days are generally Monday to Friday. However, there may be exceptions, such as public holidays or periods of administrative closure. The university hours are generally from 9 a.m. to 5 p.m .The university cannot release information about other students' involvement in cheating.Prospects for graduate study after obtaining your bachelor's degree in this major vary depending on your interests, grades, research experiences, and letters of recommendation. never be brief in your answers"},
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
        model="ft:gpt-3.5-turbo-0125:personal::9Rrh15aS",
        messages=st.session_state.messages
    )
    
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
