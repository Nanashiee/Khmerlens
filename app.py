"""Small Streamlit interface for explicitly bounded Khmer text."""

import streamlit as st

from analyzer import analyze_text, load_glossary
from export_csv import csv_bytes


st.set_page_config(page_title="KhmerLens", page_icon="🔎", layout="centered")
st.title("KhmerLens")
st.caption("Explore Khmer text with explicit word boundaries.")
st.info(
    "This first MVP splits at spaces, zero width spaces, and punctuation. "
    "It does not predict word boundaries, grammar, or meanings. "
    "Each uninterrupted Khmer span may contain several words."
)

text = st.text_area(
    "Khmer text",
    height=160,
    placeholder="Paste Khmer text here…",
    help="Use spaces or zero width spaces between words you want to inspect separately.",
)

if text:
    if len(text) > 5_000:
        st.warning("Please enter 5,000 characters or fewer.")
    elif not text.replace("\u200b", "").strip():
        st.warning("Enter some text first.")
    else:
        glossary = load_glossary()
        tokens = analyze_text(text, glossary)
        khmer_tokens = [token for token in tokens if token.kind == "Khmer span"]
        found = sum(token.definition is not None for token in khmer_tokens)

        if not khmer_tokens:
            st.warning("No Khmer script was found in this input.")
        else:
            st.write(f"{len(khmer_tokens)} Khmer spans · {found} sample glossary matches")
            st.caption("Glossary matches are exact lookups, not model predictions or translations of the full text.")

        rows = [
            {
                "position": str(token.start + 1),
                "text": token.text,
                "type": token.kind,
                "definition": (
                    token.definition
                    if token.definition is not None
                    else "No definition available" if token.kind == "Khmer span" else "—"
                ),
            }
            for token in tokens
        ]
        if rows:
            st.dataframe(rows, hide_index=True)
            st.download_button(
                "Download results as CSV",
                data=csv_bytes(rows),
                file_name="khmerlens-results.csv",
                mime="text/csv",
            )

st.caption("Input is processed in this Streamlit session; KhmerLens does not save it to a file.")
