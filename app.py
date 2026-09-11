import streamlit as st

st.set_page_config(
    page_title="Pale Epi Konprann Kreyòl AI",
    page_icon="🇭🇹"
)

st.title("🇭🇹 Pale Epi Konprann Kreyòl AI")
st.write("Yon asistan entèlijan ki pale epi konprann kreyòl ayisyen.")

message = st.text_input("Ekri mesaj ou an an kreyòl:")

if st.button("Voye"):
    if message:
        st.write("🤖 AI a resevwa mesaj ou a:")
        st.write(message)
    else:
        st.warning("Tanpri ekri yon mesaj.")
