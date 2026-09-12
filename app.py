import streamlit as st
import requests

st.set_page_config(
    page_title="Pale Epi Konprann Kreyòl AI",
    page_icon="🇭🇹"
)

st.title("🇭🇹 Pale Epi Konprann Kreyòl AI")
st.write("Yon asistan entèlijan ki pale epi konprann kreyòl ayisyen.")

message = st.text_input("Ekri mesaj ou an kreyòl:")

if st.button("Voye"):
    if message:
        try:
            api_key = st.secrets["OPENAI_API_KEY"]

            response = requests.post(
                "https://api.openai.com/v1/responses",
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "gpt-5.6-luna",
                    ".","instructions":Ou se yon asistan entèlijan ki fèt pou pale epi konprann kreyòl ayisyen klèman ak respè. Si itilizatè a pale fransè oswa anglè, ou ka reponn nan lang li itilize a. Ede itilizatè a konprann mo, fraz, tradiksyon ak ekspresyon kreyòl. Ou ka pale kreyòl ayisyen .",
                    "input": message
                },
                timeout=60
            )

            response.raise_for_status()
            data = response.json()

            answer = data["output"][0]["content"][0]["text"]
            st.write("🤖", answer)

        except Exception as e:
            st.error("Gen yon pwoblèm pandan koneksyon an.")
            st.write(str(e))
    else:
        st.warning("Tanpri ekri yon mesaj.")
