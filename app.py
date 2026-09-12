import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="Pale Epi Konprann Kreyòl AI",
    page_icon="🇭🇹"
)

st.title("🇭🇹 Pale Epi Konprann Kreyòl AI")
st.write("Yon asistan entèlijan ki pale epi konprann kreyòl ayisyen.")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

message = st.text_input("Ekri mesaj ou an an kreyòl:")

if st.button("Voye"):
    if message:
        response = client.responses.create(
            model="gpt-5.6-luna",
            instructions="Ou se yon asistan entèlijan ki pale epi konprann kreyòl ayisyen. Reponn natirèlman an kreyòl ayisyen, sof si itilizatè a mande yon lòt lang.",
            input=message
        )

        st.write("🤖", response.output_text)
    else:
        st.warning("Tanpri ekri yon mesaj.")
