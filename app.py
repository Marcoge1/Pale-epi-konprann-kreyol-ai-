import streamlit as st
st.set_page_config(page_title="Vi'n Aprann Kreyòl Ayisyen")

import requests

st.set_page_config(
    page_title="Vi'n apran'n Kreyòl Ayisyen",
    page_icon="🇭🇹"
)

st.title("🇭🇹 Vi'n apran'n Kreyòl Ayisyen")
st.write("Yon asistan entèlijan ki pale epi konprann kreyòl ayisyen.")

message = st.text_input("Ekri mesaj ou an kreyòl:")

if st.button("Voyel"):
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
                    "instructions": """Ou se yon asistan entèlijan ki pale epi konprann kreyòl ayisyen.

Reponn natirèlman tankou yon moun k ap fè yon vrè konvèsasyon an kreyòl ayisyen.

Pa repete kesyon itilizatè a sèlman.
Pa poze menm kesyon itilizatè a ankò san rezon.
Si itilizatè a di: "Bonjou, kijan ou ye jodi a?", reponn pa egzanp: "Bonjou! Mwen byen, mèsi. E ou menm, kijan ou ye?"
Lè itilizatè a pale de aprann anglè pou jwenn travay, sèvi ak ekspresyon natirèl tankou: "Mwen vle aprann pale anglè paske mwen vle jwenn yon bon job."
Si itilizatè a pale fransè oswa anglè, ou ka reponn nan lang li itilize a.
Ou ka ede ak mo, fraz, tradiksyon ak ekspresyon kreyòl.""",
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
