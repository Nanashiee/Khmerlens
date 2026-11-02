# KhmerLens

A weekend-sized Khmer text analyzer project built with Python and Streamlit.

## Current status

This is a small working **boundary and glossary** MVP, not a trained NLP analyzer.
Paste Khmer text and the app splits it at spaces, zero width spaces (U+200B),
and punctuation. It shows each span with its position, an exact match against a
three-entry sample glossary, and an explicit missing-definition label when no
match exists. You can download the results as CSV. Uninterrupted Khmer text may
contain several words; the app does not predict where they start or end.
Formula-like CSV cells receive a leading apostrophe so spreadsheet software
does not execute them.

Part-of-speech tagging, automatic word segmentation, full-text translation,
and morphological analysis are **not implemented**. The sample glossary in
`glossary.json` is manually authored starter content, not model output or a
comprehensive dictionary.

## Windows / VS Code setup

1. Extract the ZIP and open the `khmerlens` folder in VS Code.
2. Install Python 3.11, 3.12, or 3.13 if needed, plus the recommended VS Code extensions.
3. In the VS Code PowerShell terminal, run:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
```

If `python` does not point to your installed interpreter, use the Python launcher
instead (for example, `py -3.12 -m venv .venv`). The current MVP was smoke tested with Python
3.13 and Streamlit 1.66.1 on Windows.
Using the executable directly avoids PowerShell activation-policy problems.
Open the local URL printed by Streamlit. Stop the server with Ctrl+C.

Select `.venv` using **Python: Select Interpreter** in the command palette.
Press F5 to run the included Streamlit debug configuration after setup.

Try `សួស្តី ខ្មែរ` to see two exact glossary matches. Try `សួស្តីខ្មែរ`
without a boundary to see one unmatched span; the app will not invent a split.

Run the core and Streamlit UI tests with:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

## macOS / Linux

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m streamlit run app.py
.venv/bin/python -m unittest discover -s tests -v
```

## Git and GitHub

The ZIP includes a local `.git` repository on `main` and an initial scaffold
commit authored by Codex. There is no remote repository configured yet.
Set your own identity before making your commits:

```bash
git config user.name "YOUR NAME"
git config user.email "YOUR GITHUB EMAIL"
```

In VS Code's Source Control panel, choose **Publish Branch**, sign in to GitHub,
and select a private or public repository named `khmerlens`.

Alternatively, create an empty GitHub repository (without a README or license)
and run, replacing YOUR_USERNAME:

```bash
git remote add origin https://github.com/YOUR_USERNAME/khmerlens.git
git push -u origin main
```

If your extraction software omits `.git`, run `git init -b main`, then
`git add .` and `git commit -m "Initialize KhmerLens scaffold"` after setting
Git identity.

## Next milestones

- [x] Split only on explicit boundaries; show span offsets and missing definitions.
- [x] Add a tiny manually authored glossary and CSV download.
- [ ] Review and expand the glossary with sources and linguistic review.
- [ ] Resolve model-data license questions and verify `khmer-nltk` on Python 3.11/3.12 before integration.
- [ ] Connect real word segmentation and part-of-speech predictions.
- [ ] Add color-coded labels and explain the tag set when tagging exists.
- [ ] Check a small set of reviewed sentences and document errors.
- [ ] Add screenshots and deploy a demo.

`khmer-nltk` itself is labeled Apache-2.0, but its POS model references the
Khmer ALT corpus, whose official site lists the tagged Khmer data as
CC BY-NC-SA 4.0. That model is intentionally not bundled here pending a clear
data-use decision and a compatibility test. See the
[package documentation](https://pypi.org/project/khmer-nltk/),
[POS model documentation](https://github.com/VietHoang1512/khmer-nltk/tree/main/khmernltk/pos_tag),
and [ALT license page](https://www2.nict.go.jp/astrec-att/member/mutiyama/ALT/).
Dependencies currently use a version range; pin a tested environment before deployment.
