import streamlit as st
from chatbot_backend import generate_response_with_doc, load_document

st.set_page_config(page_title="Chatbot Démo", layout="centered")
st.title("Chatbot avec Mini-RAG")

# --- Historique ---
if "history" not in st.session_state:
    st.session_state.history = []

# --- Upload optionnel de document ---
uploaded_file = st.file_uploader("Choisis un document texte pour le chatbot", type=["txt"])
if uploaded_file is not None:
    with open(f"documents/{uploaded_file.name}", "wb") as f:
        f.write(uploaded_file.getbuffer())
    load_document(f"documents/{uploaded_file.name}")
    st.success("Document chargé avec succès !")

# --- Input utilisateur ---
user_input = st.text_input("Votre question :")
if st.button("Envoyer") and user_input:
    response = generate_response_with_doc(user_input)
    st.session_state.history.append(("Vous", user_input))
    st.session_state.history.append(("Chatbot", response))

# --- Afficher l'historique ---
for role, msg in st.session_state.history:
    st.markdown(f"**{role}** : {msg}")
