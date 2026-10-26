import streamlit as st
import argostranslate.translate

languages = {
    "English": "en",
    "French" : "fr",
    "Spanish": "es",
    "German" : "de"
}

def translate_text(text, source_lang, target_lang):
    try:
        result = argostranslate.translate.translate(text, source_lang, target_lang)
        return result
    except Exception:
        return "Sorry, that language pair isn't available"

st.title("Language Translator")
st.write("Type some text and translate it into another language.")

user_text = st.text_area("Enter your text")

col1, col2 = st.columns(2)

with col1:
    source_choice = st.selectbox("Translate from",list(languages.keys()))
with col2:
    target_choice = st.selectbox("Translate to", list(languages.keys()))

if st.button("Translate"):
    if user_text.strip() == "":
        st.warning("Please enter some text first.")
    else:
        source_code = languages[source_choice]
        target_code = languages[target_choice]
        output = translate_text(user_text, source_code, target_code)
        st.success(output)



