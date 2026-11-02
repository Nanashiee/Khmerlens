"""KhmerLens starter interface. NLP integration is the next milestone."""
import streamlit as st

st.set_page_config(page_title="KhmerLens", page_icon="🔎", layout="centered")
st.title("KhmerLens")
st.caption("Explore Khmer text, one word at a time.")
st.info("Project scaffold ready. Word segmentation and grammatical tagging are not connected yet.")
text = st.text_area("Khmer text", height=160, placeholder="Paste Khmer text here…")
if st.button("Preview input", type="primary"):
    if text.strip():
        st.subheader("Your text")
        st.text(text.strip())
        st.caption("Next milestone: connect the Khmer NLP engine and display word labels.")
    else:
        st.warning("Enter some text first.")
